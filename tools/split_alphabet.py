#!/usr/bin/env python3
"""Split one long recording into per-letter MP3 clips.

Say the items in the same order as the chosen list in _data/alphabet.yml,
leaving a pause (about 1-2 s) between them. The script finds the pauses with
ffmpeg, cuts the recording into clips, and names each clip from the list.

    python3 tools/split_alphabet.py recording.m4a              # 2.0 base letters
    python3 tools/split_alphabet.py recording.m4a --list digraphs

Requires ffmpeg (macOS: `brew install ffmpeg`). If the number of clips found
does not match the list, nothing is written; adjust --noise / --min-silence.
"""
import argparse, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def expected_files(list_name):
    """Return the `file:` values of one top-level list in _data/alphabet.yml."""
    files, current = [], None
    for line in (ROOT / "_data" / "alphabet.yml").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\w+):\s*$", line)
        if m:
            current = m.group(1)
        elif current == list_name:
            m = re.match(r"\s+file:\s*(\S+)", line)
            if m:
                files.append(m.group(1))
    return files


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def find_segments(src, noise, min_silence):
    r = run(["ffmpeg", "-hide_banner", "-i", str(src), "-af",
             f"silencedetect=noise={noise}:d={min_silence}", "-f", "null", "-"])
    if r.returncode != 0:
        sys.exit("ffmpeg failed:\n" + r.stderr[-800:])
    dur = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    total = int(dur[1]) * 3600 + int(dur[2]) * 60 + float(dur[3])
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    # Sound runs from the end of one silence to the start of the next.
    seg_starts = [0.0] + ends
    seg_ends = starts + [total]
    segs = [(max(a, 0), b) for a, b in zip(seg_starts, seg_ends) if b - a > 0.05]
    return segs, total


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("recording")
    ap.add_argument("--list", default="letters", help="list in alphabet.yml (default: letters)")
    ap.add_argument("--out", default=str(ROOT / "assets" / "audio" / "alphabets"))
    ap.add_argument("--noise", default="-35dB", help="silence threshold (raise, e.g. -30dB, if room noise is loud)")
    ap.add_argument("--min-silence", type=float, default=1.0, help="shortest pause between items, seconds")
    ap.add_argument("--pad", type=float, default=0.15, help="seconds kept before/after each clip")
    ap.add_argument("--dry-run", action="store_true", help="only report what was found")
    a = ap.parse_args()

    names = expected_files(a.list)
    if not names:
        sys.exit(f"No list called '{a.list}' in _data/alphabet.yml")
    src = Path(a.recording).expanduser()
    segs, total = find_segments(src, a.noise, a.min_silence)

    print(f"Found {len(segs)} sounds; expected {len(names)} ({a.list}).")
    if len(segs) != len(names):
        for i, (s, e) in enumerate(segs, 1):
            print(f"  {i:2d}. {s:7.2f}s - {e:7.2f}s  ({e - s:.2f}s)")
        sys.exit("Count mismatch, nothing written. Too many: raise --noise or --min-silence. "
                 "Too few: lower --noise (e.g. -40dB) or --min-silence.")

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for i, ((s, e), name) in enumerate(zip(segs, names)):
        prev_end = segs[i - 1][1] if i else 0
        next_start = segs[i + 1][0] if i + 1 < len(segs) else total
        start = max(s - a.pad, (prev_end + s) / 2 if i else 0)
        end = min(e + a.pad, (e + next_start) / 2 if i + 1 < len(segs) else total)
        print(f"  {name:12s} {start:7.2f}s - {end:7.2f}s")
        if a.dry_run:
            continue
        r = run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src),
                 "-ss", f"{start:.3f}", "-to", f"{end:.3f}", "-ac", "1", "-ar", "44100",
                 "-b:a", "96k", str(out / name)])
        if r.returncode != 0:
            sys.exit(f"ffmpeg failed on {name}:\n{r.stderr}")
    print("Dry run only." if a.dry_run else f"Wrote {len(names)} clips to {out}")


if __name__ == "__main__":
    main()

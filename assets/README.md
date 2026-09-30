# Audio assets

This folder holds short pronunciation clips that play next to each letter and
diacritic on the [main page](../index.md). The page already has a slot ready
for every item below — drop in a correctly named file and its player appears
automatically on the next site build. Nothing else needs to change.

## Folder layout

```
assets/audio/
├── alphabets/    one clip per letter and digraph, e.g. a.mp3, ch.mp3, ng.mp3
└── diacritics/   one clip per diacritic, demonstrated on an example word
```

The full, current list of expected filenames lives in
[`_data/alphabet.yml`](../_data/alphabet.yml) and
[`_data/diacritics.yml`](../_data/diacritics.yml).

## Recording guide

- **Format:** MP3, mono, 44.1 kHz is plenty. Keep files small (a few hundred
  KB) — this is a static site with no build pipeline to compress audio.
- **Content, alphabets:** just the letter/digraph's sound in isolation,
  the way you'd say it when teaching someone to read, ~1 second.
- **Content, diacritics:** the example word listed for that mark in
  `_data/diacritics.yml`, spoken naturally, ~1-2 seconds.
- **Naming:** must exactly match the `file:` value in the data file
  (lowercase, `.mp3`) — the site checks for that exact path.
- **Speaker credit:** feel free to add your name/initials to the PR
  description; a `CONTRIBUTORS.md` crediting voices can follow once a few
  clips are in.

## Adding a clip

1. Record the clip and export as `.mp3`.
2. Save it under `assets/audio/alphabets/` or `assets/audio/diacritics/`
   using the exact filename from the data file.
3. Open a pull request. No other files need to change.

If a letter or mark you want to record isn't listed yet, add it to the
relevant `_data/*.yml` file in the same PR.

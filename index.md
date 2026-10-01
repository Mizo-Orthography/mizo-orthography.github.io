---
layout: default
---

Mizo is normally written today without marking **tone** (pitch) or **vowel length** — so the same spelling can stand for words that sound quite different when spoken. **Mizo Orthography 2.0** is a community proposal that adds a small set of accent marks to make tone and length visible on the page, while keeping every letter you already know.

This page shows the two systems, lets you hear each new mark, and links to where you can weigh in.

<div class="callout" markdown="1">
**Familiar letters, clearer marks.** Orthography 2.0 keeps the letters you already know and adds marks on top of them — if you can read Mizo now, you can already read most of a 2.0 text; the marks just remove the guesswork. Use the tabs below to compare the proposed alphabet with the legacy one.
</div>

---

## What's Actually Changing?

* **Today:** tone and vowel length are usually left unmarked, so a reader has to already know a word to say it with the right pitch and rhythm.
* **Orthography 2.0:** each vowel gets one of four small marks (or none) to show its exact tone and length, and a few consonants get a matching mark for tone.
* **Why bother:** clearer reading for learners, more consistent hymn/scripture and dictionary spelling, and better accuracy for text-to-speech, transcription, and other digital tools.

## See the Difference

Here's one word, spelled both ways:

| | Spelling |
| :--- | :---: |
| **Today's spelling** | <span class="old-spelling">duhâm</span> |
| **Orthography 2.0** | <span class="new-spelling">dùħäm</span> |

The consonant that used to just be `h` is now written `ħ` to make the glottal stop explicit, and the vowels carry their tone/length marks instead of leaving them to guesswork. {% include audio.html dir="diacritics" file="barred_h.mp3" label="ħ example" %}

Have a clearer or more everyday example word? Suggest it in [Discussions](https://github.com/Mizo-Orthography/mizo-orthography.github.io/discussions).

---

<div class="tabs" id="tabs">
<div class="tab-list" role="tablist" aria-label="Orthography version">
<button type="button" role="tab" id="tab-new" aria-controls="panel-new" aria-selected="true">Mizo 2.0 (proposed)</button>
<button type="button" role="tab" id="tab-legacy" aria-controls="panel-legacy" aria-selected="false" tabindex="-1">Legacy Mizo</button>
</div>

<div class="tab-panel" role="tabpanel" id="panel-new" aria-labelledby="tab-new" markdown="1">

## The Alphabet

The proposed base alphabet has **{{ site.data.alphabet.letters | size }} letters and no digraphs** — every sound is built from single letters. Press play to hear each one; clips are added by volunteers, so some are still marked "not recorded yet."

| Letter | Listen |
| :---: | :---: |
{%- for item in site.data.alphabet.letters %}
| **{{ item.symbol }}** | {% include audio.html dir="alphabets" file=item.file label=item.symbol %} |
{%- endfor %}

## Tone & Length: The New Marks

The table below shows the same five vowels the way they're written **today** (one plain spelling, tone left to context) next to the **four** specific forms Orthography 2.0 gives them.

| Vowel | Today (ambiguous) | Short, low tone | Long, level tone | Long, low tone |
| :---: | :---: | :---: | :---: | :---: |
| **A** | <span class="old-spelling">a</span> | à | ā | ä |
| **E** | <span class="old-spelling">e</span> | è | ē | ë |
| **I** | <span class="old-spelling">i</span> | ì | ī | ï |
| **O** | <span class="old-spelling">o</span> | ò | ō | ö |
| **U** | <span class="old-spelling">u</span> | ù | ū | ü |

In other words: whenever today's spelling would look identical for four different-sounding words, 2.0 gives each one its own mark. Here's what each mark sounds like and where it's used:

| Mark | Looks like | Used on | Meaning | Example | Listen |
| :--- | :---: | :--- | :--- | :---: | :---: |
{%- for item in site.data.diacritics %}
| {{ item.name }} | {{ item.mark }} | {{ item.used_on }} | {{ item.meaning }} | {{ item.example }} | {% include audio.html dir="diacritics" file=item.file label=item.name %} |
{%- endfor %}

---

## Consonants That Carry Tone

A few consonants can also carry a low-tone mark:

| Consonant | Today (level tone / ambiguous) | Low tone |
| :---: | :---: | :---: |
| **L** | <span class="old-spelling">l</span> | l̀ |
| **M** | <span class="old-spelling">m</span> | ṃ / m̀ |
| **N** | <span class="old-spelling">n</span> | ň |
| **R** | <span class="old-spelling">r</span> | ř |

> **Rendering note:** on platforms where `m̀` doesn't display cleanly, the dot-below form `ṃ` is the recommended, more compatible alternative.

</div>

<div class="tab-panel" role="tabpanel" id="panel-legacy" aria-labelledby="tab-legacy" markdown="1">

## The Alphabet

The legacy Mizo alphabet has **{{ site.data.alphabet.legacy | size }} letters**, three of which — **aw**, **ch** and **ng** — are digraphs (two characters, one letter).

| Letter | Type | Listen |
| :---: | :---: | :---: |
{%- for item in site.data.alphabet.legacy %}
| **{{ item.symbol }}** | {% if item.digraph %}digraph{% else %}letter{% endif %} | {% include audio.html dir="alphabets" file=item.file label=item.symbol %} |
{%- endfor %}

## Tone & Length

Legacy spelling does not mark **tone** or **vowel length**, so one written form (for example <span class="old-spelling">a</span>, <span class="old-spelling">e</span>, <span class="old-spelling">i</span>, <span class="old-spelling">o</span>, <span class="old-spelling">u</span>, or <span class="old-spelling">duhâm</span>) can stand for several differently-sounding words. Readers rely on context and prior knowledge of the word.

</div>
</div>

<script>
(function () {
  var root = document.getElementById('tabs');
  if (!root) return;
  var tabs = [].slice.call(root.querySelectorAll('[role=tab]'));
  var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute('aria-controls')); });
  var hashes = { 'tab-new': 'mizo-2', 'tab-legacy': 'legacy' };
  function select(i, focus, updateHash) {
    tabs.forEach(function (t, j) {
      t.setAttribute('aria-selected', j === i);
      t.tabIndex = j === i ? 0 : -1;
      panels[j].hidden = j !== i;
    });
    if (focus) tabs[i].focus();
    if (updateHash && history.replaceState) history.replaceState(null, '', '#' + hashes[tabs[i].id]);
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(i, false, true); });
    t.addEventListener('keydown', function (e) {
      var k = e.key, n = tabs.length;
      if (k === 'ArrowRight') select((i + 1) % n, true, true);
      else if (k === 'ArrowLeft') select((i + n - 1) % n, true, true);
      else if (k === 'Home') select(0, true, true);
      else if (k === 'End') select(n - 1, true, true);
      else return;
      e.preventDefault();
    });
  });
  root.classList.add('js');
  select(location.hash === '#legacy' ? 1 : 0, false, false);
})();
</script>

---

<details markdown="1">
<summary>Full technical summary (for linguists &amp; developers)</summary>

| Feature | Diacritic | Notes |
| :--- | :--- | :--- |
| **Short tone** | None / Grave (`◌̀`) | Bare for short level, grave accent for short low. |
| **Long tone** | Macron (`◌̄`) / Diaeresis (`◌̈`) | Macron for long level, diaeresis for long low. |
| **Glottal stop** | `ħ` | Replaces implicit or context-dependent glottal stops. |

**2.0 alphabet (no digraphs):** `a` `b` `c` `d` `e` `f` `g` `h` `i` `j` `k` `l` `m` `n` `o` `p` `r` `s` `t` `ṭ` `u` `v` `z`
**Legacy alphabet (digraphs *aw*, *ch*, *ng*):** `a` `aw` `b` `ch` `d` `e` `f` `g` `ng` `h` `i` `j` `k` `l` `m` `n` `o` `p` `r` `s` `t` `ṭ` `u` `v` `z`

All source data for the tables on this page (letters, legacy letters, and diacritics) lives in [`_data/alphabet.yml`](https://github.com/Mizo-Orthography/mizo-orthography.github.io/blob/main/_data/alphabet.yml) and [`_data/diacritics.yml`](https://github.com/Mizo-Orthography/mizo-orthography.github.io/blob/main/_data/diacritics.yml) — propose a change there and it updates every table on the page.

</details>

---

## 💬 Community Feedback & Discussion

We welcome input from linguists, educators, developers, and native speakers — this proposal isn't final, and it won't get better without your eyes on it.

To participate:
1. Go to the [**Discussions**](https://github.com/Mizo-Orthography/mizo-orthography.github.io/discussions) tab in this repository.
2. Select or start a thread about a specific mark, an example word, rendering compatibility, or anything else.
3. Share your suggestions, objections, or questions — or just leave a comment below.

Want to help with audio? See [`assets/README.md`](https://github.com/Mizo-Orthography/mizo-orthography.github.io/blob/main/assets/README.md) for how to record and add a pronunciation clip.

<script src="https://giscus.app/client.js"
        data-repo="Mizo-Orthography/mizo-orthography.github.io"
        data-repo-id="R_kgDOU0OfDw"
        data-category="Ideas"
        data-category-id="DIC_kwDOU0OfD84DGs1h"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="preferred_color_scheme"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>

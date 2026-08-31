# Session Handoff

**Project** ANTZ Command Centre — customizable module home page
**Session ended** 31 August 2026
**Head** `f9efdb2` on `main`

---

## 1 · Where things are

| | |
|---|---|
| Live | <https://antz-module-selection-home.vercel.app> |
| Repository | <https://github.com/naveen-lset/Module_Selection-Home-page-> |
| Vercel project | `naveen-lsets-projects/antz-module-selection-home` |
| Working copy | `~/Desktop/Module Selection` |
| Figma source | [Antz Modules → Home](https://www.figma.com/design/CqCR8vdtWyasWENyA02Khv/Antz-Modules?node-id=55476-32828) · node `55476:32828` |

```
index.html      7,376 lines — the whole application, no build step
tools/          foliage.py + the supplied header artwork it processes
assets/img/     7 photographs from Figma, avatar, foliage.png
assets/icon/    27 SVGs — 25 from Figma, plus Approvals and Communication
References/     design screenshots (in git, excluded from the deploy)
README.md       the decisions, the measurements, and what was got wrong
```

Everything but the images lives in `index.html`: the stylesheet is in a series
of `<style>` blocks, the application is one `<script>` at the foot holding 18
modules behind a small `__def`/`__req` shim (there is no bundler, and `file://`
will not serve ES modules).

---

## 2 · What the product is now

**17 modules · 74 card variations · 12 layouts.** A module is a place; a
variation is one way of putting that place on the home page. Counts per module
range from 3 (Mortality, Fetal Death, Communication) to 6 (Medical) — modules
expose only the cards their work actually has.

The twelve layouts, each with its own markup rather than a shared template:

`door` · `compact` · `photo` · `stat` · `metrics` · `chart` · `queue` ·
`status` · `progress` · `timeline` · `recent` · `actions`

Two fills: the module's gradient, or a photograph. **Colour does not vary
between a module's cards** — see §5.

The home page is arranged by the user (drag, resize, add, remove) and saved to
`localStorage`. Every action they can take on it hangs off their own avatar.

---

## 3 · How to work on it

```bash
open index.html                 # no server, no install, no build

python3 tools/foliage.py        # regenerate the header artwork
vercel deploy --prod --yes      # redeploy (see the caveat in §6)
```

Console helpers, all on `window.antz`:

```js
antz.state()           // the live layout
antz.columns()         // how many columns the viewport resolves to
antz.reset()           // back to the default home page
antz.allVariants()     // every card at every size it declares, on the grid
antz.checkDefaults()   // assert the catalogue and the default page agree
```

### The verification loop used all session

Screenshots are not enough on a card system this size. The reliable method was
to drive a headless browser and **measure**:

```bash
# render every variation at every size, then check each composition root for
# vertical overflow and every label for truncation
antz.allVariants() → compare scrollHeight/clientHeight and scrollWidth/clientWidth
```

Run it at 1920 / 1024 / 900 / 768 / 640 / 500. It renders ~165 cards and it
found nine real defects this session that no screenshot showed.

**Use `--headless=new`.** The legacy headless renderer silently drops SVG
`<img>` children inside scaled subtrees — it cost an hour chasing a
"missing icon" bug that did not exist.

---

## 4 · Two invariants that will bite

**`priority: 'primary'` means exactly "on the default home page".** There is no
third state and no exception list. `DEFAULT_LAYOUT` in `layoutStore.js` and the
catalogue in `cardVariants.js` must agree in both directions, and
`antz.checkDefaults()` asserts it. It has caught a real mismatch every single
time the seeded page changed. Run it after touching either file.

**Bump `VERSION` in `layoutStore.js` when the catalogue changes shape.**
Currently **4**. A saved layout from an older schema is still *readable* —
`repair()` drops retired ids and keeps the rest — but it is not *wanted*: anyone
who has opened the site before will keep looking at the old page and conclude
nothing changed. The cost is that a genuinely customised arrangement is
discarded, so do not bump it lightly.

---

## 5 · Decisions worth not re-litigating

**Colour is the one thing that does not vary between a module's cards.** Data
cards were briefly given a "soft" fill — the module gradient under an 84% white
veil, dark text — reading the brief's *"stats: softer gradient / clean
surface"*. It works on a vivid module and fails on a desaturated one: Follow
Up's petrol and Approvals' slate came out **grey**, on a page whose premise is
that a module is recognisable by its fill. The variety comes from composition —
a queue looks nothing like a timeline whatever colour they are — and the fill's
job is the opposite one, holding a module's cards together. Reverted in
`f9efdb2`.

**No "View →" on informational cards.** The whole card is the link. Those rows
repeated what clicking already did, cost a line, and competed with the data.
Quick Actions is the exception; its controls are the content.

**Add Module is a header action, not a grid tile.** It was packed after the last
card, which on a fifteen-card page put the primary action of the mode below the
fold. Now: `Edit Modules · ＋ Add Module · Done`, wrapping to a full-width row
on a phone, still above the grid.

**The palette is closed at 16 gradients, all from the Figma file.** Approvals
wears Users' slate and Communication wears Follow Up's petrol. An earlier pass
invented an indigo and an amber; both were reverted. *Which* two was a
legibility decision — Administer's sage is the lightest fill in the set and was
close to unreadable behind a data card.

**The page is capped at 1024px on every screen** — 960 of content inside 32px
margins, the Figma frame exactly. Two things are pinned with it and breaking
either breaks the page: the **column count** (`--grid-cols` is set by viewport
media queries while the grid divides the *page*; a 1920px monitor would ask for
12 columns inside 960px) and the **type** (every `--fs-` token is a `clamp()` on
`vw` that would keep growing past a page that has stopped).

**The header planting is a CSS mask, not a gradient overlay.** The page wash is
a translucent double gradient that changes down the document, so any
background-coloured block would be chasing a moving target; and an overlay fades
leaves and gaps alike, which reads as fog. `mask-image` removes the artwork's own
alpha so leaves dissolve individually.

---

## 6 · Open items

**⚠ Unresolved conflict — the responsive column ladder.** The master refinement
brief (§15) asks for 8 columns on desktop and 12 at 1600px+. That is
incompatible with the 1024px content cap requested two turns earlier, and the
cap won because it was the more recent and more specific instruction. **This was
flagged, not agreed.** If the wide ladder is wanted, it is `--max-content` plus
restoring two `@media` blocks — and the 8/12 rows are still in `SPAN_TABLE`
precisely so that lifting the cap does not silently resolve every span to 1×1.

**⚠ Accessibility audit is stale.** The "23 of 30 text runs below AA" figure in
the README was measured on the original fifteen-card page and has **not** been
re-run against the 74-card catalogue. The finding is structural — white text on
the light end of a gradient — so it applies to every new card on those fills,
and there are far more text runs now. A fresh pass is a screenshot-and-sample
over `antz.allVariants()`. The standing fix (darken the light end of each
gradient until white clears 4.5:1) would lift the semantic tones with it.

**⚠ Vercel is not connected to GitHub.** `vercel link` could not attach the repo
— that needs the Vercel GitHub App installed on it, which is a browser step.
**Pushing to GitHub does not deploy.** Deploys are currently manual from the
working copy (`vercel deploy --prod`). Fix under Vercel → Project → Settings →
Git.

**Minor.** A real mouse-drag of a linked card (Species Management) is worth a
manual check — the pointer-drag simulation moved neither it nor a control button
card, so the harness is incomplete there; the keyboard reorder path is verified.

---

## 7 · Traps found the hard way

**CSS transitions do not advance under `--virtual-time-budget`.** Any computed
value read mid-transition returns the *start* value. The edit-mode header
reported `height: 0px` at every width; disabling transitions showed the correct
44px. Nearly fixed a bug that did not exist — and the real bug underneath was
`.edit-hint`'s `margin-top: -12px`, tuned for a header that never wrapped.

**`curl` hits Vercel's CDN cache.** Two post-deploy verifications appeared to
show the old build. Add a cache-buster (`?v=$(date +%s)`) and
`-H "Cache-Control: no-cache"` when checking a fresh deploy.

**`git push` of the initial ~10 MB pack fails with HTTP 400.** That is git's
default 1 MB `http.postBuffer`, not credentials. Already configured in this
clone; a fresh clone will need it again.

**Grepping served HTML for runtime state proves nothing.** `data-layout` and
`data-fill` are set by JS, so they never appear in the HTML. Verify by running
the page, not by reading it.

---

## 8 · If you are picking this up cold

1. `open index.html`, then `antz.checkDefaults()` in the console — it should
   print that the catalogue and the default page agree.
2. Read the README's *"Twelve layouts, two fills, one design language"* and
   *"The default home page is a balance"*. They carry the reasoning; this file
   carries the state.
3. The catalogue is `js/data/cardVariants.js` inside `index.html`. Adding a card
   is a data edit — pick a layout, give it content, choose its sizes. Adding a
   *layout* means a function in `ModuleCard.js` and a section in `cards.css`.
4. Before shipping anything: `antz.allVariants()` and the overflow sweep at six
   widths, `antz.checkDefaults()`, and a console-error check.

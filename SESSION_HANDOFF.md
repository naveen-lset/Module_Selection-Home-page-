# Session Handoff

**Project** ANTZ Command Centre — module home page + a three-level Site Command Centre
**Session ended** 1 September 2026 (third session)
**Working copy** `~/Desktop/Module Selection` — committed on `main`, not yet deployed

---

## 0 · What this session did

**A second workspace, on the same engine.**

`Module Selection` and `Site Command Centre` are now two views of the same page,
switched by a segmented control under the search field. The home page is
byte-identical; the new surface is a configurable operating view of the whole
hierarchy — **Housing → Site → Section → Enclosure** — with 163 widgets over 25
domains, fifteen role × level defaults, permission-aware at every depth, and
personalisable with the drag/resize/add machinery that already existed.

**Depth is not a third tab.** The switcher stays two-way and `level` sits under
it, with the breadcrumb as the spine — a five-way switcher would have flattened a
hierarchy into five peers and thrown away the one thing the reader needs most,
that *this* Section is inside *that* Site.

**The catalogues get smaller and sharper with depth, not bigger.** 84 widgets at
the Site, 41 at a Section, 38 at an Enclosure. Four domains are absent from the
Section level by design (a section has no budget, contract, risk register or
quarterly insight) and five exist only at the Enclosure. §12 of the brief is
explicit that copying the same widgets down the hierarchy is the failure, and it
is a very easy failure to reach — a `sectionId` filter over the Site catalogue
would have shipped three identical-looking levels carrying smaller numbers.

**Where the "no individual animals" rule inverts.** A Site widget that names an
animal is a small copy of Species Management. That rule is about ALTITUDE, and at
the enclosure it turns over: §12 lists the level's subjects as occupancy,
condition, husbandry, veterinary and assessments, all of which are about the
specific creatures in the specific space. So `enc.occ.list` names individuals and
`enc.assess.welfare` is the **Five Domains** model — the framework zoo welfare
assessment actually uses, and the one place in this build where the widget
followed the profession rather than the layout.

**The framing came first.** `docs/framing-site-command-centre.md` — the problem
separated from its symptoms, seven stakeholder roles, **eleven recurring
decisions** in Decision → Question → Insight → Action form, success criteria, an
explicit scope boundary, and a **YELLOW** readiness verdict with its risk named
in writing (the five roles are inferred; the real ANTZ taxonomy lives in a system
this prototype cannot read — mitigated by holding role defaults as pure data).

**The important finding, before any code:** of the eleven widget *types* the
brief asks for, **nine already existed** as layouts in `cardVariants.js`. So the
build was catalogue data, a role layer, and two new compositions — not a second
application. `health` (a gauge and the domains its index is made of) and
`insight` (measured change, in sentences) are the only new ones.

**Zero components were forked, across all three levels.** ONE grid, ONE edit
mode, ONE drag controller, ONE size popover, ONE header, ONE widget gallery.
What swaps when the level changes is three pieces of data — the catalogue, the
store and the subject. Three components were generalised rather than copied:

    the STORE became createWorkspaceStore({...}), instantiated three times
    the SITE HEADER became a workspace header with one level-aware subject()
    the GALLERY's search index became rebuildable, keyed on src.revision

The original three seams still hold: `createModuleGrid({ isCore })`,
`createModulePicker({ source })`, `createEditMode({ labels })`.

**Eight bugs the build found in itself** — all by driving the page, none by
reading it. See §7.

---

## 1 · Where things are

| | |
|---|---|
| Live (home only — **not yet redeployed**) | <https://antz-module-selection-home.vercel.app> |
| Repository | <https://github.com/naveen-lset/Module_Selection-Home-page-> |
| Vercel project | `naveen-lsets-projects/antz-module-selection-home` |
| Working copy | `~/Desktop/Module Selection` |
| Figma source (home) | [Antz Modules → Home](https://www.figma.com/design/CqCR8vdtWyasWENyA02Khv/Antz-Modules?node-id=55476-32828) · node `55476:32828` |
| Figma (pushed screens) | [Desktop-Navigation](https://www.figma.com/design/CNhiaOGCLdnlNxj7x2Ohrd/Desktop-Navigation) · page *Claude Screens* — **home flow only; the Site Workspace is not in Figma yet** |

```
index.html      ~16,400 lines — the whole application, no build step
docs/           the ARCHITECT framing document for the Site Command Centre
tools/          cdp.py (CDP client) · verify.py (pre-ship checks) · foliage.py
assets/         7 photographs, avatar, foliage, 27 module SVGs
README.md       the decisions, the measurements, and what was got wrong
```

**⚠ Not deployed and not committed.** `vercel deploy --prod --yes` from the
working copy. Vercel is still not connected to GitHub (§6), so pushing does not
deploy.

---

## 2 · What the product is now

**Two workspaces, four levels, one card engine.**

| | Module Selection | Site | Section | Enclosure |
|---|---|---|---|---|
| Question | which function? | how is my Site doing? | how is this area running? | how is this animal housed? |
| Groups | 17 modules | 18 domains | 15 domains | 11 domains |
| Cards | 74 · 150 combos | 84 · 207 | 41 · 97 | 38 · 90 |
| Store | `antz.home.layout` v4 | `antz.site.layout.<role>` | `antz.section.layout.<role>` | `antz.enclosure.layout.<role>` |
| Locked cards | Species, Medical | **none** | **none** | **none** |
| Defaults | one arrangement | five, one per role | five | five |

**163 widgets, 25 domains, 394 widget × size combinations, 15 role × level
defaults.** Four Sites, 31 sections, 139 enclosures.

**The counts reconcile.** Section records sum exactly to their Site's `counts` —
enclosures, staff, species, animals — on all four Sites, and
`antz.checkHierarchy()` asserts it in both directions. It would be tidier to
derive the Site totals and delete the Site's own numbers; it would also be wrong,
because a Site has staff who belong to no section.

**The summary and the detail agree.** Three enclosures are authored explicitly and
they are the ones a Site-level card already promised: Welfare Alerts names CAR-02
and HRB-03, Restricted Areas names REP-04. Drill in and the condition is there.
The other 136 are generated from their section's seeds with every varying number
hashed from the enclosure code, so they are stable across reloads and identical
on every machine.

Four Sites, and the fourth is load-bearing: **Hesaraghatta Field Station** was
commissioned three weeks ago and genuinely has no asset register, budget line or
compliance history. Seven of a Manager's twenty-two Site widgets render a real
empty state there, two of twenty at Grassland Plot A, and three of sixteen at
HGA-01 — emptiness travels down the hierarchy because the reason for it does.
That is how §15 is satisfied without an `isEmpty` flag, which would have been the
fake it forbids.

---

## 3 · How to work on it

```bash
open index.html                 # no server, no install, no build

python3 tools/verify.py         # the home page: defaults, sweep, drag, console
vercel deploy --prod --yes      # redeploy (see the caveat in §6)
```

Console helpers:

```js
antz.state() / columns() / reset() / allVariants() / checkDefaults()

antz.site.view()             // { view, level, siteId, sectionId, enclosureId, roleId }
antz.site.state()            // the live workspace layout, at the live level
antz.site.go('site')         // switch workspace
antz.site.site('hg-field')   // switch Site — this is the one with the empty states
antz.site.section('car')     // into a Section
antz.site.enclosure('car.2') // into an Enclosure — the authored welfare case
antz.site.children()         // what is under the current subject
antz.site.up() / .down()     // move through the hierarchy
antz.site.role('vet')        // switch role
antz.site.allWidgets()       // every widget of the CURRENT level, at every size
antz.checkSiteDefaults()     // all 15 role x level arrangements, AND they pack without gaps
antz.checkHierarchy()        // the counts reconcile and the enclosure promises hold
```

### The verification loop, extended

`tools/verify.py` covers the home page and is unchanged. The three workspaces were
verified the same way, and the scripts are worth rebuilding rather than trusting a
screenshot — the sweep is **394 combinations × 11 subjects × 9 widths, about
8,900 renders**, and it found eleven real clipping defects that no screenshot
showed.

Four checks are specific to this surface and every one of them caught something:

- **Header ↔ widget cross-check.** Staff, animals, enclosures, sections, health
  and attention, read from the header and from the widgets, on all four Sites.
  This is what found the derivation bug (§7).
- **Gap check inside `antz.checkSiteDefaults()`.** Pack each of the fifteen seeds
  at five columns and count the cells no card claimed. Defaults are composed from
  blocks that fill two rows exactly, and it is very easy to break that by
  changing one widget's `supportedSizes` in passing.
- **`antz.checkHierarchy()`.** Section counts against Site counts in both
  directions, generated enclosure counts against their section record, and that
  every enclosure code a Site card names actually exists.
- **Coherence sweep.** Across six enclosures, that the clinical history names no
  animal the occupant list does not contain. This found two of the eight bugs.

---

## 4 · Invariants that will bite

**The two from before still hold, unchanged.** `priority: 'primary'` means
exactly "on the default home page", and `VERSION` in `layoutStore.js` (still
**4**) is bumped only when the module catalogue changes shape.

**Each level has its own version, and that is the point.** The three stores in
`siteWorkspaceStore.js` are all at version **1** and are three separate numbers.
Sharing `layoutStore`'s key would have meant a change to a site widget discarding
everyone's arranged *home page*; sharing one key across levels would mean a change
to the enclosure catalogue discarding their Section workspace. Nine keys — three
levels × role — and every one of them versions on its own.

**`antz.checkSiteDefaults()` after touching `roles.js` or a widget's
`supportedSizes`.** It asserts four things the eye cannot: no unknown widget, no
unsupported size, no permission violation, and **no empty grid cells**.

**Every widget must trace to a decision.** `decision` on each widget names a row
in the framing document. It is never rendered, and the rule is that a widget
tracing to none is cut however easy its data is — three were.

**A level needs at least one 1×1 widget per domain a role can see.** On the
five-column grid a pair of 2×2 cards leaves exactly one column, so a domain with
no small card cannot take part in a default that fills its rows. That is why each
deeper catalogue carries a KPI per domain — structural, not decoration. See the
block note in `roles.js`.

**Deeper is smaller.** If a new widget would work equally well one level up, it
belongs one level up. The Section and Enclosure catalogues earn their existence by
being *more specific*, and the moment they start carrying general cards the
hierarchy stops being worth navigating.

**A count that appears twice must have one source.** Anything the Site record
already knows is computed in `derive()`; anything it does not know is authored
per Site in `figures`. Do not re-type a staff count into widget data.

---

## 5 · Decisions worth not re-litigating

**Colour identifies the domain**, exactly as it identifies the module on the home
page. Eighteen domains onto **the same closed sixteen gradients**, with four
deliberate sibling pairs (Safety/Emergency, Work/Upcoming, Assets/Vendors,
Space/Insights). The palette is not re-opened. Still.

**An empty card gets a neutral outlined surface, not the domain gradient under a
veil.** The veiled-gradient treatment was tried on this product before, for data
cards, and reverted because on a desaturated fill it removes the colour rather
than softening it. This sidesteps that entirely: an empty card is not a quiet
version of a full one, it is a different thing.

**Nothing is locked in the Site Workspace.** Which widget is indispensable is
precisely what differs between a veterinarian and a facility manager, so the only
honest answer is that none of them is.

**One saved layout per role, not per Site.** An arrangement is a statement about
how a person works; Sites differ in their *data*, and the empty states handle a
Site that has none.

**Five roles, one workspace — not five dashboards.** Identical on day one, five
products by the end of the quarter. A role contributes a permission set and an
ordered list of ids, both plain data.

**The switch is a segment under the search field, not a left rail.** A rail costs
72–88px of a 960px content width permanently, and 179.2px columns are
(960 − 4×16) ÷ 5 *exactly*. A rail would have made every card the wrong size on
the one page whose fidelity is measured in units.

**The Manager default is the brief's §20 order, and §20's "optional" row is
deliberately not seeded.** A default carrying everything has no hierarchy left to
offer.

---

## 6 · Open items

**⚠ Not deployed.** Everything below is committed and unpushed to production.
`vercel deploy --prod --yes`.

**⚠ None of the Site Command Centre is in Figma.** The home flow's seven frames
are in *Desktop-Navigation*, page *Claude Screens*. The three workspaces are not:
that is Site (manager / veterinarian / facility / the empty-state Site), Section
(manager / veterinarian / facility) and Enclosure (manager / veterinarian /
facility), plus the widget gallery at each depth. Build them from the running app
over CDP rather than from re-reading CSS, and keep the constraints the user set:
no local styles, no variables, 1024 fixed wide, height HUG, native GRID layout at
5 columns with real `gridColumnSpan` / `gridRowSpan`. **The 25 domain glyphs are
sprite symbols rather than exported files**, so they will need exporting from the
running page before the frames can use instances.

**⚠ The role taxonomy is inferred.** The named YELLOW risk in the framing
document. Five roles, their permission sets and their default orders are a design
inference; the real definitions live in ANTZ v5. Held as data in `roles.js`
specifically so a correction is two array edits rather than a redesign.

**⚠ The cards still do not meet AA, and that is still a recorded decision.**
472 of 530 gradient-card text runs below AA on the home page, worst 1.49:1. The
Site widgets inherit the same palette and the same condition. A conforming remedy
was built and reverted in the previous session. **Do not re-open the palette for
contrast.** If the fills must change, that belongs in the Figma file.

**⚠ The responsive column ladder conflict is unresolved and untouched.** 8
columns at desktop / 12 at 1600px+ versus the 1024px content cap. The cap won as
the more recent and more specific instruction. `SPAN_TABLE` still carries the 8
and 12 rows so lifting the cap does not silently resolve every span to 1×1.

**⚠ Vercel is not connected to GitHub.** Pushing does not deploy. Fix under
Vercel → Project → Settings → Git; it needs the Vercel GitHub App installed on
the repo, which is a browser step.

**Deferred by design.** Section Workspace and Enclosure Workspace. The philosophy
is set — widgets get *more specific* with depth — and copying the Site's widgets
down the hierarchy is the thing that would wreck it.

---

## 7 · The eight bugs this build found in itself

All eight were found by driving the page, none by reading it.

### The Site level

**Switching Site showed the previous Site's figures.** The grid reconciles by uid
and rebuilds a card only when its variantId or span changed — correct for every
other update and exactly wrong for this one, because a subject change alters
neither. It rendered Bannerghatta's numbers under Hesaraghatta's name, which is
the worst failure this page can have **because it is the one that looks like it
worked**. Fixed with `wsGrid.destroy()` on a subject change: moving through the
hierarchy is a navigation, so there is no continuity to preserve and no FLIP worth
running. The same fix now covers Section and Enclosure moves, which have the
identical shape.

**The Site header and the People widget disagreed on the same screen** — "19
Staff" from the record, "86 Staff" from the catalogue. Fixed by deriving every
figure the record already holds and authoring only the judgements per subject.
Re-typing the numbers into four Sites' data would have moved the bug, not fixed
it. `derive()` now exists at all three levels for the same reason.

**Two galleries wrote the same element id.** `aria-labelledby="picker-title"`
resolves to the *first* match in the document, so the widget sheet announced
itself as "Add Module" to a screen reader. Ids are now per instance.

**A health card's rows went two-column on an iPad in portrait.** The threshold was
a `max-width`, and `large` is two columns on the reference grid but *three* at the
768px band — so a card that had gone single-column at 1024 came back as two 164px
columns, and "Maintenance / Attention" does not fit in 164.

### The deeper levels

**Two animals in one enclosure with the same name.** The generator indexed the
name table with a hash slice per position, and slices collide — HRB-03 came out
holding two animals called Shakti. It walks forward from a collision now, so the
result is still deterministic. Nobody would have crashed over it and every reader
who looked twice would have stopped believing the page.

**The clinical history named an animal that was not an occupant.**
`enc.vet.history` was authored copy (Bhima, Kaveri) while the occupant list is
derived, so on most enclosures the history named animals the Individuals card two
rows away did not contain. Both come from the same function now. The same pass
moved `enc.assess.history`, `enc.assess.behaviour` and `enc.assess.trend` onto
derived values, because they had the same problem waiting.

**REP-04's note contradicted its own occupant count** — "occupants moved to
REP-05" on a card reporting six occupants.

**Two status rows clipped at the 900px band**, which is the narrowest the
reference grid ever gets: five columns inside 836px, so a one-row status card's
two columns are 138px each. `"6 days"` became `"6 d"` and `"Pacing logged"` became
`"Pacing"`.

### And one pre-existing

`chev-right` and `chev-left` were being called by the gallery's rail rows and its
phone-width back button, and had never been defined in the sprite — both rendered
an empty box. Found while wiring the switcher, which needs the same three
chevrons.

---

## 8 · Traps found the hard way

**All of the previous session's traps still apply** and are still the fastest way
to waste an hour: CSS transitions do not advance under `--virtual-time-budget`;
WAAPI promises never settle under it, so the grid *looks* like it leaks card
nodes; a synthesised `PointerEvent` cannot hold pointer capture; `curl` hits
Vercel's CDN cache; `git push` of a large pack needs `http.postBuffer`; and
grepping served HTML for runtime state proves nothing.

**New, and specific to two catalogues in one document:** a `querySelector` for
anything inside "the sheet" now matches the *module* gallery, because it is
mounted first. Scope to `.sheet.is-open`. This is what made three interaction
checks report failures that were the test's fault, not the product's — and it is
also how the duplicate-id bug was found, so it was worth the confusion.

**`CARD_VARIANTS` is deliberately not extended.** Widgets from all three levels
register into the shared *lookup* but not into that array, because three things
read it as specifically the module catalogue: `primaryVariants()` decides the
default home page, the module gallery builds its search index from it, and
`antz.allVariants()` stress-tests it. Adding 163 widgets would have put them into
all three.

**`antz.site.allWidgets()` sweeps the CURRENT LEVEL only.** It reads `cat()`, so a
sweep has to set the level first and the level's subject second. A sweep that
forgets is not an error — it silently re-tests the level you were already on, and
reports a clean pass for a catalogue it never rendered.

---

## 9 · If you are picking this up cold

1. `open index.html`. In the console: `antz.checkDefaults()`,
   `antz.checkSiteDefaults()` and `antz.checkHierarchy()` — all three should
   print that things agree.
2. Click **Site Command Centre**. Work the role chip through all five roles, the
   Site caret through all four Sites, and then go **down**: tap the Sections count
   in the header, then the Enclosures count. Hesaraghatta is the Site with the
   empty states; Mysuru is the one that is actually in trouble; `CAR-02` is the
   enclosure the Site's Welfare Alerts card promises you.
3. Read the README's *The Site Command Centre* and *Down the hierarchy* sections
   for the reasoning, and `docs/framing-site-command-centre.md` for what the thing
   is *for*. This file carries the state.
4. Adding a widget is a data edit in the right level's catalogue —
   `siteWidgets.js`, `sectionWidgets.js` or `enclosureWidgets.js`. Pick a layout,
   give it content, choose its sizes, and name the decision it serves. Ask first
   whether it belongs one level up: deeper catalogues earn their existence by
   being *more specific*.
5. Adding it to a default is a data edit in `roles.js`, composed with `pair()` and
   `wide()` — and then `antz.checkSiteDefaults()`, which will tell you if you have
   left a hole.
6. Before shipping: `python3 tools/verify.py`, the three-level sweep at nine
   widths across the eleven subjects, all three console assertions, and a
   console-error check.

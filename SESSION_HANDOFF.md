# Session Handoff

## Close-out — 1 September 2026

If a fresh session opens this next, here is the minimum to keep going.

The Site Workspace was rebuilt from a dashboard into a Site home screen — 83
widgets to 40, a Manager's 29 cards to 12, every `View X ›` CTA removed, no
record ever named on a Site page. Housing became a module on the home page and
opens a new Sites listing above the Site. Everything is verified and **entirely
uncommitted.**

**The single most important next move:** `docs/Modules.md Files/` appeared in the
repo mid-session — 40 files of the real ANTZ v5 specification, with real routes,
dataKeys, widget catalogues and per-role layouts. Nothing built this session was
checked against it. It names the **twelve real roles**, which closes the YELLOW
risk in the framing document, and its `level-site.md` includes an *Operational
score* gauge that the user's own brief forbids. Read it before touching a
catalogue again.

> **DONE — see §0, the sixth session.** The 34 topic modules are a menu in the
> Site header and 34 cards in the Site catalogue; the twelve roles are closed
> and bridged to our five. `level-site.md`'s *Operational score* was **not**
> built: the prohibition holds, and `antz.checkSiteDefaults()` would not have
> caught it, so it is worth restating — the documents are a source, not an
> instruction that outranks the brief.

### How to accept what shipped

| Try this | You should see | If not |
|---|---|---|
| Scroll the home page to the foot, tap **Housing** | The Sites listing, four Sites ranked worst-first, Mysuru at the top | `localStorage.clear()` — a v4 layout has no Housing tile |
| On the listing, tap **Mysuru Rescue Centre** | Its workspace: 96 assets / 4 critical, 18 open jobs / 7 overdue, 19 of 25 compliance | If you see Bannerghatta's 248 assets, `applySite()` is not landing the per-Site figures |
| Read any Site card to its bottom edge | A name, a figure, a label, one short clause — and nothing else | Any `View …` text means the CTA floor came back |
| Tap anywhere on a card, including the whitespace | It navigates | If only part of it responds, something was nested inside the button |
| Site → **Sections** card, then back, then **Enclosures** | Section level, then Enclosure level — Enclosures goes two levels | — |
| Switch the role chip through all five | Different first screens, 10–12 cards each, no empty grid cells | `antz.checkSiteDefaults()` will name the hole |
| Open **Hesaraghatta** | 8 of 12 cards in a real empty state, each naming what is missing | Fake zeros mean `absent` lost an id |
| Look at the gap under the hero, and under the search field | 16px and 20px; the switcher shares the search field's edges | Both were 0 before this session |

**Still running:** a static server on `http://localhost:8000` (PID in
`lsof -i:8000`). Kill it when you are done.

---

**Project** ANTZ Command Centre — module home page + a four-level Site Command Centre
**Session ended** 1 September 2026 (fourth session)
**Working copy** `~/Desktop/Module Selection` — **uncommitted**, not deployed

---

## 0 · What the SIXTH session did

**The Site page has a menu icon, and it offers the real ANTZ module catalogue.**

`docs/Modules.md Files/` — the 39 dashboards and 299 widget definitions that
appeared in the repo at the end of the fifth session, and that the fifth session's
own handoff flagged as *"the single most important next move"* — is now the source
for a control rather than a document nobody had read. Three files:

    js/data/siteModules.js   the 34 topic modules, the twelve real roles,
                             and the bridge between those twelve and our five
    js/data/siteWidgets.js   section T — 34 module cards, scaled per Site
    js/components/PopMenu.js headings, checkbox rows, keepOpen, a height cap

**THE TWELVE ROLES ARE CLOSED, AND roles.js IS UNCHANGED.** Every module
document names the seats that treat it as a priority; across the 34 files exactly
twelve names appear. That closes the YELLOW risk `roles.js` has carried since it
was written — *its five roles are inferred* — **without replacing the five**,
because fifteen hand-balanced layouts hang off those ids and swapping in twelve
is a different job with a different risk. One map bridges them, every one of the
twelve is covered exactly once, and `antz.checkModules()` asserts it.

**EVERY MODULE CARD CARRIES A FACT NO OTHER CARD ON THE PAGE CARRIES.** This was
most of the work and it is the thing to preserve. Nine of the 34 collided with a
summary card on the first pass — Maintenance's document leads with 486 open work
orders and `site.maint.open` says twelve — so those nine took the module's SECOND
fact instead. Maintenance reports the hours the jobs cost, Assets the lapsed
service contracts, Housing the biosecurity pass rate, Animal Collection where the
animals not in their own enclosure are, Finance the cost per animal per day.

**FIGURES ARE AUTHORED ONCE AT BANNERGHATTA AND SCALED BY ONE RATIO.** The
documents are facility-wide and the two datasets do not divide cleanly — 57
animals per enclosure there against 6.6 here — so scaling each figure by its own
denominator gives some cards a plausible number and others a nonsense one. Every
card carries a `doc` field naming the line it came from. The reference Site's
ratio is 1, so what it shows is what was authored.

**THE MENU IS PopMenu, NOT A SECOND COMPONENT.** Four general additions —
`{ heading }`, `on`, `variant`, `keepOpen` — and the height is capped from the
space actually left below the button rather than by a number in CSS.

### Four defects this pass found in itself

| | |
|---|---|
| `1 critical breakdowns` | scaling hit one and the plural stayed. `label1` / `clause1`, declared not derived — Species, Papers and Staff all break a trailing-s rule |
| `1 Paper Expiring` over `All current` | six `none` clauses were reassurances about the CARD, contradicting the figure above them. `none` replaces the CLAUSE |
| a queue whose rows did not sum to its total | scaled separately; the total comes from the rows now |
| five 1×1 titles ellipsed at 900px | the title line gets 92px there, about twelve characters |

### The search field quotes its term, and Enter is answered

    before   Search Animals          <- reads as a caption
    after    Search "Animals"        <- reads as an example query

Curly quotes, matching the gallery's "Nothing matches ..." empty state. They sit
INSIDE the animated span so the whole quoted unit slides as one thing; outside,
the closing quote would jump horizontally on every swap as the word changed
width. It caught a latent bug: `step()` compared the next WORD against the
PAINTED TEXT, which stops being the same question once the text is decorated.

**PRESSING ENTER DID NOTHING, AND A FIELD THAT SWALLOWS A KEYSTROKE READS AS
BROKEN.** There is no index to answer with, so it acknowledges instead: with a
query the field settles, a ring leaves its edge and the magnifier darts (press ·
release · scan); with nothing the HINT bounces. Deliberately not a shake — a
shake means "you did that wrong" and an empty box is unfinished, not wrong.

**THE RING STARTS AT 2px, NOT 0.** From nothing its brightest frame is already
6px out and half faded, and the gesture read as a smudge. Starting with the ring
drawn puts the strongest frame where the eye is.

**AND MOTION IS NEVER THE ONLY CHANNEL.** `animate()` is a no-op under reduced
motion, so `onSubmit` announces either way. That half has its own browser in the
suite: nothing moves, the live region still speaks.

**THE FRAMES ARE SAMPLED, NOT REASONED ABOUT.** The first attempt to photograph
the ring read 13.5px at what it thought was 30ms, because `getAnimations()`
returns nothing once an animation has finished and 420ms was long over by the
time the harness arrived. The test fires Enter and pauses every animation it
started in the SAME turn of the event loop, then seeks.

### Every card looked the same, and the SEED was why

Forty-six of the seventy-four Site widgets were the `stat` composition. The fault
was the DISTRIBUTION, not any one card, which is why it survived three passes.

**THE DEFAULTS WERE ROWS OF FIVE AND A ROW OF FIVE CANNOT HOLD ANYTHING TWO ROWS
TALL.** A photograph, a donut and an attention card are all 2x2, so the seed was
silently excluding three quarters of the card system — authoring new widgets
would not have got one onto a default page. They are blocks of ten cells now, the
same thing `pair()` already did for Sections. `large + large + medium` looks like
ten cells and packs into three rows leaving five empty; the packer is asked
rather than trusted.

    widgets      74 -> 87
    stat         46 (62%) -> 40 (46%)
    compositions 9 -> 13

Thirteen new cards: **five photographs** (Site, collection, clinic, kitchen,
work — minimal content, an image and a name, except the collection which takes
its two figures off the record) and **eight quick-action cards** (three verbs
each, gated by the domain like everything else). Six module cards moved off
`stat` to `attention` / `ring` / `chart` / `status`, in every case because the
document already held a better shape than a single figure.

### Four defects, and the check that found a fifth

| | |
|---|---|
| two cards titled "Maintenance" in one default | the action cards were named after their domains, and four of those names were already on a summary card in the same domain |
| **every Section default has carried two cards titled "Enclosures" for three sessions** | found by the new duplicate-title assertion on its FIRST run. The list is `By Enclosure` now — the catalogue's own convention for a decomposition |
| the biologist's page showed the collection twice | the photograph's figures and a card repeating them |
| two pre-existing truncations | surfaced by widening the overflow sweep from the module cards to the whole Site catalogue |

### And the Hospital glyph

The redrawn export replaced the ward-block-and-cross one. **`iconSize` stays at
38** — it is the glyph's box on the artboard, not the file's canvas, and
following the file would have made Hospital the only module glyph that is not
the size Figma says. It shipped for one session as `hospital.svg`; the seventh
session renamed it back to `m-hospital.svg`, so the `m-` prefix holds across all
fifteen and the old drawing lives only in git history.

### The header gave its controls back

Five controls became one. The role chip, **Add**, **Customize** and **More** are
gone from the Site header; what is left is the **☰**, which is the only one of
the five that is about the product rather than the page.

    before   [☰] [Viewing as  Site Manager] [+ Add] [Customize] [...]
    after    [☰]

Everything else hangs off the avatar, which is the rule the home page has
followed since the profile menu was written — the Site header had been the
exception. `Viewing as` is a ticked radio group there; the quick actions are
under an `On this <level>` heading, gated by permission and level exactly as
before; `Open Report` came across because it was the one More item that was
nowhere else. The More menu's *Go Up* / *Open a Section* items are **not**
reproduced: the breadcrumb, the sibling caret, the counts strip and Escape are
already three routes to that move.

**THE ROW IS DEFINED ONCE FOR BOTH MENUS NOW.** `menuEntry()` is exported from
PopMenu.js, because the two components genuinely differ in their head, their
anchoring and their dismissal — and not in what a row is. It went out of step on
the first attempt: the role switcher arrived in the profile menu **without a
tick**, because ProfileMenu's renderer had never needed `checked`. `ProfileMenu`
takes `items` as a function of the state now; a label function cannot make a row
that is not there.

**AND A DUPLICATED REQUIREMENT FAILED THE WAY THEY DO.** The modules menu capped
its height against the space under its anchor and the profile menu did not, so
eighteen rows came out 1,097px tall in a 1,000px window with the last two
unreachable. `capToViewport()` is shared, and `.pmenu` scrolls.

**A SECOND CHECK THAT AGREED WITH ITSELF.** The truncation probe measured
`.pmenu__label` and `.pmenu__note` and not `.pmenu__heading-note`, so it passed
while "Site Manager · Command Ce…" sat ellipsed at the top of the menu. Two
sessions running, the blind spot has been the same shape as the bug: a check that
reads what the code intended rather than what the page renders.

### And one found in production, after the first deploy

**`btn.hidden = true` set the property, cleared the accessibility tree, and left
the button on the screen.** The modules button was supposed to be gone on the
Sites listing and at the two deeper levels; it shipped visible at all three,
because `[hidden]` is a bare attribute selector in the UA stylesheet at
specificity 0,1,0 and `.btn-icon { display: grid }` beats it.

**It got past a check that agreed with itself.** The test read `el.hidden` — the
property, which was correctly `true` — rather than the computed `display` or the
element's box. The listing rules at the foot of site.css were the same problem
solved one selector at a time; there is a general rule now
(`.btn-icon[hidden], .btn-solid[hidden], .btn-line[hidden]`) so the next control
to be hidden does not have to rediscover it. **Assert on the box, not on the
attribute.**

### And two found on the way past

**The gallery's rail listed eight domains that opened onto an empty pane.** The
comment on `visibleDomains()` claimed it filtered them and the code never checked.
Fixed — one call to the catalogue. **Escape did two things** with a header menu
open: closed the menu and climbed a level.

### How to accept it

| Try this | You should see |
|---|---|
| Site page → the **☰** left of *Viewing as* | Two headed lists: *For the Site Manager* (6) and *Also available to you* (28), with Medical, Animal Population and Alerts ticked |
| Tap **Maintenance** | It ticks, the page scrolls to a new *Downtime* card, and **the menu is still open** |
| Tap it again | The card goes, the tick goes |
| Remove a module card from the grid while the menu is open | Its row unticks |
| Switch the role chip through all five | 6+28 / 8+13 / 9+6 / 10+12 / 7+7, and a different first list each time |
| Drill to a Section or an Enclosure | **The ☰ is gone** — those levels have their own catalogues |
| Open **Mysuru**, role Facility Manager | IoT 11/23, Energy ₹1.8L *on generator*, and the same six cards read green at Zoo Core |
| Open **Hesaraghatta** | *Overtime* reads "Staff here are still on the parent Site's payroll" |
| `antz.checkModules()` | `[]` |

---

## 0 · What the FIFTH session did

**A widget opens the record it was summarised from.**

Tapping any Site, Section or enclosure widget that does not drill into the
hierarchy now opens that DOMAIN's full record over the page — a sheet with the
same manners as the widget gallery, headed by the domain at the domain's own
gradient. **52 records, 2,124 fields**, resolved against whichever Site,
Section or enclosure is loaded. Three files, and no component was forked:

    js/data/domainDetail.js        the records — 25 domains, tuple rows
    js/components/WidgetDetail.js  the sheet
    css/detail.css                 its stylesheet, scoped to `wdetail`/`d*`

**KEYED ON THE DOMAIN, NOT ON THE WIDGET.** 117 widgets would have meant 117
detail documents, most of them the same document with a different tile on top.
The workspace's own rule settles it — the destination is a property of the
domain — so every Maintenance widget opens the same record, and what stays
per-widget is what should: the sheet names the card it came from and opens
*scrolled to that card's group* rather than at the top.

**FIGURES THAT ARE ALSO ON A CARD ARE READ FROM THE CARD.** The sheet opens on
top of the widget and the two are on screen together. `maintOpen`, `assets`,
`vetCases`, `tasks`, `overdue`, `approvals` and `incidents` come out of the live
catalogue that `applySite()` has already rewritten; everything else is derived
from the subject record or authored once. The staff-count bug cannot recur here.

**IT GOES DOWN WITHOUT BEING COPIED DOWN.** §12's failure was reached on the
first pass and then fixed: Overview's Command Centre Summary and Executive
Action Dashboard are `only: ['site']`, and the Section and enclosure get *This
Section, Today* / *This Enclosure, Now* / *Needs Attention Here* / *Care Due
Here* instead. The sheet's title follows the depth — Site, Section or Enclosure
Overview — because Overview is the one domain whose subject is the page itself.

**NO CTA FLOOR CAME BACK ONTO A CARD.** The one action is in the SHEET's footer,
where a primary action is not a control inside a control. `View <module>` is
hidden entirely for Overview, which has nowhere to send anyone.

**NO COMPOSITE SCORES.** The source list asks for an overall facility health
score, a site-wise operational score and an animal health score by site — all
three are absent, replaced by the counts they would have been computed from.
Body condition, the Five Domains model and audit results stay: those are
measurements a profession publishes, not indices this product invented.

**`antz.checkDetail()` found two classes of defect the eye would not have.**
A table row of two cells against three columns, and **210 facts rows with a
tone string ('ok'/'warn'/'alert') sitting in the sub column** — which rendered
the word "warn" as a caption under a figure. Both fixed. The check resolves
every domain at every level and asserts tiles have values, groups have rows,
table rows match their columns, and every widget's landing group exists.

**A LANDING FOR MODULES AND WIDGETS**, adopted from a MasonryGallery reference
component (React + GSAP) — the design, not the machinery. `js/lib/landing.js`
plus one `land()` method on `createModuleGrid`, so the home grid and all three
workspace levels share it: no fork, and the cascade is computed from the grid's
own placement because the grid is the only thing that knows it.

Four substitutions, each with a reason:

  NO GSAP · `animate()` in motion.js is the one place reduced motion is
  honoured; a second engine is a second way to ignore it. 70KB for six
  keyframes, in a file with no build step.

  NO GEOMETRY · the reference animates x/y/width/height because it owns its
  masonry maths. Ours comes from CSS `grid-area` and is not animatable — hence
  the FLIP pass. The landing touches transform, opacity and filter only.

  BOUNDED · `innerHeight + 200` over 1.2s is right for a portfolio scrolled
  once and wrong for a view that re-lands on every level switch. 64px, 560ms.

  SEEDED RANDOM · `Math.random()` per item breaks under a grid that reconciles
  rather than rebuilds — the jiggleFor() rule. Hashed from the uid.

**THE BUG WORTH REMEMBERING: THE CAP ATE THE CASCADE.** Delay was
`min(score * stagger, maxDelay)`, and a bottom-up score is `(rows - row) * cols
+ col` — up to 40 on a five-column page, so every card in the top four rows
landed on the 340ms cap AT THE SAME INSTANT. The code read as though it worked;
only reading the animations' delays out of the DOM showed one value repeated.
Cells are ranked now and the ranks spread across a fixed span, which also means
a forty-card page compresses instead of taking a second and a half.

Blur is budgeted at 18 cells — past that the rise and fade stay and the blur
goes, because a `filter` costs a compositing pass per element per frame and the
stutter would land exactly in the 200ms the effect exists to decorate.

Which arrivals land: first paint, workspace switch, subject change, role change,
reset. Which do not: drag, repack, add, remove, edit mode. All nine are asserted.

**THE CHROME WAS REORDERED, AND THE PAGE TITLE DIED OF IT.** The switcher is now
FIRST — above the greeting and the search field — because *which workspace* is a
bigger question than anything under it, and it used to be discovered after the
page had been read. That settled the greeting argument the other way: with the
selected tab saying "Site Command Centre · Operate a Site" at the top and the
Site header naming the subject two rows down, the `Site Command Centre` page
title drawn from `body.is-site .home-header::before` was the third voice and the
one saying least. It is gone, `body.is-site .greeting { opacity: 0 }` with it,
and "Good Morning, Sourav Tambe" now shows in both views.

**AND THE SITE ROWS LOST THEIR 4px STATUS RAIL** — third statement of the same
word on a row that already carries a pill, an items list and a count, and it
pushed the Site name off the row's own left edge so nothing lined up with the
header above it.

**THE SEARCH FIELD NAMES WHAT IT WILL FIND, ONE WORD AT A TIME.** Animals ·
Enclosures · Users · Modules, per view AND per depth, on a 2.1s dwell.
`js/components/SearchHint.js`. It is NOT the placeholder — a placeholder is a
string and a string cannot animate — so the real one is emptied and the hint is
an `aria-hidden` span where it would have been, with the SCOPE moved to the
input's `aria-label`, which is the only place it was ever announced from.
Freezes on focus, hides while typing, stops on a hidden tab, and under reduced
motion does not cycle at all: one static line naming three categories.

**TWO BUGS IN IT, BOTH FOUND BY MEASURING RATHER THAN LOOKING.**

  `fill: 'forwards'` ON THE OUTGOING HALF. Two animations — out, then in on the
  promise — left the first still applied when the second ended, so every word
  finished arriving and then vanished. Sampled opacity said dim in 12 of 20
  frames while the markup and the text were perfectly correct. One keyframe set
  that leaves and returns holds nothing at the end.

  A SHARED STOP. `tick()` re-arms the dwell timer and was calling the full
  `stop()`, killing the text swap it had scheduled 260ms earlier — so the hint
  animated the same word for ever. It moved and never changed.

Both are asserted now: `verify_detail.py` samples the word's opacity and counts
distinct words across a cycle.

**THE MODULES MENU IS A CENTRED DIALOG NOW.** Reported from the deployed build:
it opened to the side and ran off the edge. It is thirty-four rows in two groups
and it decides what the whole workspace holds — that is a dialog, and it was
drawn as a hint. `createPopMenu` gained ONE flag, `centred`, and no component
was forked: the box is positioned in CSS rather than measured from the anchor,
capped at `min(76dvh, 720px)` with its own scroll, widened to 460 so no module
name ellipses, and the catcher doubles as a VEIL that blurs the page (same
values as the record sheet's scrim). Page scroll locks while it is open, and it
gained a sticky title and a × — a popover needs neither, because it belongs to
the button it came from; centred over a veil, nothing on screen says what it is
or how to leave it.

**AND EACH ROW SAYS ONLY HOW MANY WIDGETS.** It was "Site Overview · 6 widgets":
a domain name repeated on all thirty-four rows, under a heading that already
says what the group is, with the one useful number on the far side of a
separator.

The other four menus in the header are four rows each and stay popovers.

**THE SWITCH NOW OPENS THE SITES LISTING, AND IT TOOK THREE PASSES TO GET THE
INTENT RIGHT.** The first reading of the report was backwards — it was built to
land on a Site, then on a Site harder — and the user's reference screenshot
settled it: *Site Command Centre* is a DOOR TO THE SITES, and the listing is
what has to come. `setView()` resolves `level` to `sites` on the way into the
view, with reason `'sites'` so app.js treats it as a subject change (an open
record sheet closes, the previous level's grid is dropped).

Two things fell out of it that are worth keeping:

  A TAB THAT WAS A DEAD BUTTON. The listing lives inside the Site view, so
  working in a Site leaves the tab selected and `view === view` swallowed the
  tap — pressing the control did nothing at all. It now means "back out to the
  Sites", which is what an already-selected tab does everywhere else.

  THE DESTINATION NO LONGER DEPENDS ON PERSISTED STATE. `level` is saved, so
  the tab used to point wherever you happened to be last. `siteId` is still
  untouched by the switch, which is what lets the listing mark "Last opened".

`antz.site.allWidgets()` needed one line: the switch lands on a listing now, and
a listing has no grid to sweep, so the helper steps into the Site level itself.

Verification: **`python3 tools/verify_detail.py`** — three levels, six widths,
empty subjects, Escape behaviour: ALL PASS. `tools/verify.py` is still fully
green, so the home page is untouched.

---

## 0 · What the FOURTH session did

### The last pass: the Site Workspace went minimal

**Eighty-three widgets became forty, and a Manager's twenty-nine became twelve.**
The workspace was a dashboard; it is a Site home screen now. Every card is a
whole clickable module carrying a name, a figure and **one clause** that says
whether to go in.

**THE `View X ›` FLOOR CAME BACK OUT, one session after it went in.** It was a
reasonable reading of the brief's `[View Assets]` sketches and it was wrong: the
card has been a `<button>` since the first line of `ModuleCard.js`, so the floor
was a control inside a control, and eleven of them turned a workspace into a page
of links. The affordance is the surface — hover lifts, press settles, focus
rings — and nothing is drawn.

**Everything that named an individual record is gone.** Critical Equipment's five
asset names, the maintenance job list, the veterinary cases, the licence and
inspection rows, the activity and upcoming timelines. What survives of each is
the count that decides whether to open the module. Site page → summary; module →
detail; detail page → records.

**Emergency Readiness was a health score in disguise** — a 74% gauge — and it is
`3 / 5 systems ready` now. The `health` LAYOUT is down to exactly one card in the
whole product: the enclosure's Five Domains welfare assessment.

**Veterinary and Welfare became their own Site domains**, and **Projects exists
for the first time** (`d.projects`, the 26th domain, sharing Work & Activity's
fill). Animal Operations is two numbers.

**The narrow card moves every row.** Twelve cards packed 2-2-1 four times is a
grid with a column of smalls down the right; reordered to 2-2-1 / 1-2-2 / 2-1-2 /
1-2-2 it reads as a composition. First-fit means the ORDER IS THE LAYOUT.

**Not done, on purpose: §13's subtler gradients.** See §5.


**Housing is a module, and the flow it opens is the missing top of the
hierarchy.**

    Home page  →  Housing  →  Sites  →  Site  →  Sections  →  Enclosures

Nothing on the home page had said the Site Command Centre existed — it was
reachable only from the segmented switch — and nothing in the product had ever
shown all four Sites at once. Both are the same gap, and Housing closes it: **one
tile** at the foot of the home page, and a new **`sites`** level that is the
Housing listing.

**ONE TILE, AND THAT WAS A CORRECTION MADE ON REQUEST.** Housing was built with
four cards — a Sites status list, an attention list, the door and a count — on
the reasoning that every other module carries three to six. The user's answer
was *"Don't add anything new in the Module Selection page. I need one module
called Housing, enough."* They were right, and the reason is worth keeping: the
home page is a MODULE CHOOSER, and the three extra cards previewed a page that
is one tap away. The five extra variants are deleted from the catalogue, not
merely unseeded — a card that should not be on this page should not be addable
to it.

**The listing is a table, not four cards.** The question it serves is
comparative — which Site needs me this morning — and a comparison wants its
values in columns. Ranked by what is open, worst first; the Site you last had
open is *marked* rather than sorted up. It is the only level with no subject, so
it has no catalogue, no saved arrangement and no widgets.

**Site Health is gone. So are Section Health and Enclosure Health.** §2 of the
new brief forbids it by name, and the argument holds: an index over six
incommensurable things is not an observation, two Sites at 87% are not in
comparable condition, and it hid the difference between *failing* and
*unfinished* — Hesaraghatta scored 61% and is three weeks old. The `health`
LAYOUT stays for the enclosure's Five Domains welfare assessment, which is a
published framework rather than an index this product invented. `overview.status`
replaced all three in the fifteen defaults.

**Maintenance appeared three times on a Manager's page** — a door, an open-jobs
list, and a `Maintenance Split` carrying a different decomposition of the same
twelve jobs four rows down. The `attention` layout gained an optional `split`,
which is how §10 draws the card, and `site.maint.split` is **deleted from the
catalogue** rather than dropped from the defaults: a card that must not appear
twice must not be addable twice.

**Infrastructure went from `full` to `large`** — it was 960px wide with a third
of it empty. **Utilities became one card** rather than three. **Every large
widget grew a `View <module> ›` floor**, which is both §41's navigation promise
and the fix for the brief's "large unused spaces inside cards".

**91 pre-existing clipping defects were fixed** as a side effect. The previous
sweep only checked content against the *card* floor; these were rows cut by
their own `overflow: hidden` container, which is a different measurement.

---

## 0b · What the third session did

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
| Live (home only — **two sessions behind**) | <https://antz-module-selection-home.vercel.app> |
| Repository | <https://github.com/naveen-lset/Module_Selection-Home-page-> |
| Vercel project | `naveen-lsets-projects/antz-module-selection-home` |
| Working copy | `~/Desktop/Module Selection` |
| Figma source (home) | [Antz Modules → Home](https://www.figma.com/design/CqCR8vdtWyasWENyA02Khv/Antz-Modules?node-id=55476-32828) · node `55476:32828` |
| Figma (pushed screens) | [Desktop-Navigation](https://www.figma.com/design/CNhiaOGCLdnlNxj7x2Ohrd/Desktop-Navigation) · page *Claude Screens* — **home flow only; the Site Workspace is not in Figma yet** |

```
index.html      ~17,580 lines — the whole application, no build step
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

**Two workspaces, FIVE levels, one card engine.**

| | Module Selection | Sites | Site | Section | Enclosure |
|---|---|---|---|---|---|
| Question | which function? | which Site needs me? | how is my Site doing? | how is this area running? | how is this animal housed? |
| Groups | 18 modules | — | 18 domains | 15 domains | 11 domains |
| Cards | 94 · 215 combos | **none — it is a listing** | **40 · 79** | 40 · 95 | 37 · 88 |
| Store | `antz.home.layout` v5 | — | `antz.site.layout.<role>` | `antz.section.layout.<role>` | `antz.enclosure.layout.<role>` |
| Locked cards | Species, Medical | — | **none** | **none** | **none** |
| Defaults | one arrangement | — | five, one per role | five | five |

**117 widgets, 26 domains, 262 widget × size combinations, 15 role × level
defaults.** Four Sites, 31 sections, 139 enclosures.

**THE SITE LEVEL IS DELIBERATELY THE THINNEST CATALOGUE OF THE THREE NOW**, and
that inverts what was true before. A Site page is a summary and a set of doors;
a Section and an Enclosure are where the operational detail lives. If a new Site
widget wants to name a thing — an asset, a job, a case, an event — it belongs one
level down or inside the module, and the answer at the Site is the count.

**`sites` IS A LEVEL, NOT A THIRD TAB, AND IT IS THE ONLY ONE WITH NO SUBJECT.**
Housing → Sites → Site → Section → Enclosure is one hierarchy and the breadcrumb
is its spine. It has no catalogue, no store and no widgets: `syncWorkspace()`
sets `body.is-listing`, shows `#sitesList`, hides `#siteWorkspace`, and returns
before every branch that touches a workspace. Adding a widget grid to it later
would be the wrong instinct — the decision it serves is *which Site*, and that
is one list.

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
                             // level is now one of sites|site|section|enclosure
antz.site.state()            // the live workspace layout, at the live level
antz.site.go('site')         // switch workspace
location.hash = '#sites'     // the Housing listing (no console helper — it has
                             // no subject, so there is nothing to pass)
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

**The two from before still hold.** `priority: 'primary'` means exactly "on the
default home page", and `VERSION` in `layoutStore.js` is bumped only when the
module catalogue changes shape. It is at **5** now: Housing joined the
catalogue, and a saved v4 layout had no Housing on it and no way to acquire one
except by hand — which would have left a returning user on a home page with no
door into half the product.

**THERE IS NO HEALTH SCORE, AT ANY LEVEL, AND IT IS NOT COMING BACK.** The
`health` layout survives for exactly one card — the enclosure's Five Domains
welfare assessment, which is a published framework with defined criteria. A
second gauge over incommensurable domains re-opens the thing §2 of the brief
forbids by name. `site.health` and `sec.health` are still fields on the records
and are deliberately rendered NOWHERE; if you find yourself reaching for one,
the answer you want is `attention` and `openItems`.

**A COUNT THAT APPEARS TWICE MUST HAVE ONE SOURCE — and `openItems` is the
newest instance of that rule.** The per-Site attention rows are on the Site
record; `derive()` hands them to the Needs Attention widget and the Sites
listing reads them directly. Do not re-author them in a widget's `data`.

**`hidden` IS ONLY A UA RULE.** Any class on the same element that sets
`display` beats it on specificity, and the "hidden" panel then sits on screen
underneath the one that replaced it. `.sites` deliberately declares no
`display`; an hour went into learning that.

**A CARD WITH A `View X` FLOOR HAS ONE ROW LESS TO GIVE.** Four list layouts
render everything they are given and let the card clip the overflow. The
`.card[data-foot]` rules in cards.css drop the row that would be cut, at
breakpoints measured on the eight-width sweep. Change a footer's height and
those breakpoints move.

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

**THE WHOLE CARD IS THE CONTROL, AND NOTHING GOES INSIDE IT.** No `View X`, no
arrow, no footer link, no button. It was tried in this same session and removed
in it; do not put it back. The affordance is hover / press / focus on the
surface.

**ONE CLAUSE PER SUB, AND IT IS THE ACTIONABLE HALF.** Twenty-four characters is
what a 1×1 card holds. `5 need attention`, not `231 operational · 5 need
attention`. Where nothing is wrong the clause turns over — `All operational`,
`None overdue` — rather than disappearing.

**§13's SUBTLER GRADIENTS WERE NOT BUILT, and that is a judgement, not a miss.**
The fills are unchanged; the page calmed down because the cards got smaller and
fewer. Desaturation was tried on this product once and reverted — under a veil
the already-quiet fills turn grey rather than soft. If it is asked for again it
is one tonal scale in `cards.css`, and it belongs in the Figma file first.

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

**The Manager default follows the brief's priority order for the role, and the
"optional" widgets are deliberately not seeded.** A default carrying everything
has no hierarchy left to offer. Risk, Projects, Transport and Documents are one
tap away in the gallery.

**Housing shares Hospital's fill, and that is the first shared fill on the home
page.** All sixteen Figma gradients were spoken for, so a fifteenth module either
re-opened the palette or shared. Hospital's own seeded card is the ward
*photograph*, so the deep slate is not drawn anywhere else on the default page.
This is a one-off, not a precedent — a nineteenth module needs a conversation
about the palette rather than a second borrow.

**The Sites listing is a quiet sheet, not four gradient cards.** Every widget in
this product is a saturated fill you go *into*; a listing is something you read
*across*. Four gradient cards would have made the page look like a workspace one
level too early, and would have made a Site's colour mean something — it does
not, because a Site is not a domain.

**The listing ranks on open items and marks where you were; it does not sort you
to the top.** Moving the row a reader is used to seeing in third place breaks the
one thing a ranked list promises.

**A `View <module>` floor is on every large data widget, and on no small one.**
It is §41's navigation promise made visible, and the reason the list layouts stop
pooling their slack in a void at the bottom. Overview widgets are exempt: their
subject is the page you are already on.

---

## 6 · Open items

**⚠ UNCOMMITTED AND NOT DEPLOYED.** This session's work is in the working copy
only. `git add -A && git commit`, then `vercel deploy --prod --yes`.

**⚠ §37 of the brief — the 8–12 pinned-widget cap — is deliberately NOT built.**
The five seeded role defaults run 21–29 widgets, roughly half of them the 1×1
doors and KPIs the grid needs to pack its two-row blocks without a hole. Capping
at twelve would seed fewer *substantive* widgets than §31's own suggested first
viewport lists. The anti-clutter mechanism §37 names — a curated default with
everything else behind Add Widget — is already how the product works (a Manager
is seeded 29 of 83). If the user wants the cap enforced, it is a limit in
`ModulePickerBottomSheet.js` plus a re-cut of all fifteen defaults, and the
second half is the expensive part.

**⚠ None of the Site Command Centre is in Figma, and now there is one more
screen.** The home flow's seven frames are in *Desktop-Navigation*, page *Claude
Screens*. Missing: the **Sites listing** (one frame, plus its 960 stacked
reflow), and the three workspaces —
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

**⚠ Eighty-nine widget ideas are mocked up, module by module, and waiting on
a decision.** `mockups/widget-concepts.html` — one BLOCK OF TEN CELLS per module
for all eighteen home modules, 41 compositions, sizes mixed on purpose (36 at
1x1, 28 at 2x1, 22 at 2x2, 3 full width). Eighteen of the compositions are
SIGNATURES that serve one module and would not transplant: Medical's cases are a
severity ladder, Hospital's ward is its beds, Pharmacy's stock is shelves with
the expiry end drawn dark, Lab's samples are tubes, Species is an exact treemap,
Mortality is a tape read downwards, Fetal Death is forty outcome slots, Eggs is
eight day-counters, Housing is the estate worst-first, Diet is the store in
kilograms, Follow Up is a month, Parivesh is runway to a deadline, Administer is
a queue's depth drawn, Users is the day, Security is the fence, Reports is a page
it would print, Approvals is age not size, Communication is the conversations.
The other 23 are shared vocabulary. **If it has to shrink, cut signatures, not
vocabulary.** Every figure is from `docs/Modules.md Files/` — the file and
dataKey are printed in each block's legend; six modules have no spec of their own
(Lab, Hospital, Mortality, Fetal, Eggs, Follow Up) and read the nearest real
keys, and a few row-level distributions inside signatures are invented to fill
the shape while the totals are real. Photographs only where one exists — six
files in `assets/img/`, so six image cards; everywhere else the glyph is blown up
at 12%. Quick actions at three sizes (1x1 one verb, 2x1 three, 2x2 four).

**Rules the page keeps, and asserts:** no 1x1 carries a title (the glyph names
it, as a `door` does), no card repeats in words what its figure said — what a
card is FOR lives in the legend under the block — and no card says "View".
`mock.checkBlocks()`, `checkCollapsed()`, `checkOverflow()`, `checkImages()` and
`checkRules()` are green at nine widths. **Four defects the checks caught that
review had not:** a runway track at 0x0 (a bare `<span>` is inline and ignores
height); the watermark inflating every 1x1's scrollHeight by 14px (an absolutely
positioned descendant counts toward scroll overflow even under `overflow:
hidden` — it needs a clipper, and a transform does not help); the treemap's
blocks not matching their shares because `flex-grow` does not distribute free
space in exact proportion at those magnitudes (percentages do); and a treemap
block 16px tall clipping a 27px label, which passed until `checkOverflow` was
taught to ask about the VERTICAL axis as well as the horizontal.

**Old note, superseded.** **⚠ Twelve new widget compositions are mocked up and waiting on a decision.**
`mockups/widget-concepts.html` — a standalone page, this product's own tokens,
cards at artboard size, the reference Site's real figures. Drawn from the four
sheets in `References/Widgets_Reference/`; what is taken is the composition and
never the styling. Each one names the existing layout you would otherwise reach
for and why it falls short. **Two are decisions rather than proposals:**
`setpoint` would be the first card in the product that WRITES (optimistic
state, failure path, undo, a permission gate finer than the role chip), and
`agenda` overlaps `timeline` closely enough to be a variant rather than a
twenty-second entry in `LAYOUTS`. Nothing is wired to `derive()`, the picker or
the packer. Eight of the twelve are 2x2, so adding them means REPLACING cards
in the fifteen seeded defaults, not appending — the page notes this. Its own
checks are `mock.checkOverflow()` and `mock.checkCollapsed()`, green at nine
widths; the second one exists because the split bar shipped at zero height and
every overflow assertion passed on it.

**Worth doing next, and small.** The Sites listing has no filter or sort control
— the ranking is fixed at worst-first. Four Sites do not need one; forty would,
and the row template already carries every field a filter would key on.

**Still open from before.** `site.risk.top` overflows horizontally by ~60px at
`medium` on every width. It is pre-existing, it is not in any default (only a
user who resizes it down reaches it), and it is one of about forty `medium`-size
clipping defects the sweep reports across the three catalogues — all of them the
deliberate "show what fits" behaviour of the list layouts in a 132px content box,
and all of them worth a pass of their own.

---

## 6b · The defects the FOURTH session found in itself

### Three of them are spacing, and a person found all three

None of the sweeps could have caught any of these. Every sweep in this project
measures content against **its own container**; all three are the space
*between* two elements, and nothing measures that.

| | Was | Now |
|---|---|---|
| Hero → first card row | **0** | `var(--grid-gap)` — the artboard says 16 and it had never been drawn |
| Search field → switcher | **0** | 20 |
| Switcher → hero | 52 | 32, the artboard's page padding alone |
| Switcher width | **1024** against everything else's **960** | 960 |

The band steps **24 / 20 / 32 / 16** now. The last two are not choices — 32 is
the artboard's page padding and 16 is the grid gutter. **If you add a chrome row
between the search field and the hero, it needs `padding-inline: var(--pad-page)`
and a margin on the element ABOVE it, not below.** The switcher had neither, and
that is both of the first two rows in that table.

### And two in the code

The artboard's own arithmetic is in the CSS — `32 padding + 204 hero + 16 gap +
5 × 164 rows + 4 × 16 gaps = 1136` — and the sixteen after the hero had never
been drawn, so the frame measured 1120 for three sessions while the README
claimed 1136. That is the first row of the table above, and it is the reason to
trust the arithmetic already written down over the claim that it was met.

**A sprite glyph in a layout with no rule for it filled the viewport.**
`glyph()` names the wrapper after whatever layout asked for it and appends
`--sprite`, and only `card__icon--sprite` and `c-head__icon--sprite` had CSS. So
`housing.compact` rendered an `<svg>` with no width — 199px of content in a
124px card. It had been latent for two sessions because every group carrying a
sprite was a Site DOMAIN, and no domain offers a compact card. Housing is the
first MODULE with one.

**The listing rendered on top of the workspace.** `.sites { display: block }`
beat the UA's `[hidden] { display: none }` on specificity, so hiding the panel
did nothing. Found in the first screenshot after wiring it, which is the only
way it was ever going to be found.

**The `View X` floor cut the row above it in half.** Thirty-one pixels taken off
a list whose container clips its overflow does not remove an entry, it bisects
one — "Keeper training · Batch 4" lost its date. The first sweep missed it
entirely because it measured content against the *card* floor and the container
had already shrunk. Fixing the measurement found **91 pre-existing instances** of
the same class of defect.

---

## 7 · The eight bugs the third build found in itself

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
2. **Scroll to the bottom of the home page and tap Housing.** That is the flow
   this session built: Housing → Sites → Site → Sections → Enclosures. Any of
   the four Housing cards does it. Then open **Mysuru** from the listing — it is
   the Site that is actually in trouble — and come back up with the **Sites**
   crumb, and out with **Housing**.
3. Work the role chip through all five roles, the Site caret through all four
   Sites, and then go **down**: tap the Sections count in the header, then the
   Enclosures count. Hesaraghatta is the Site with the empty states; `CAR-02` is
   the enclosure the Site's Welfare Alerts card promises you.
4. Read the README's *Housing — the way in*, *No Site Health* and *The workspace
   the brief asked for* sections for this session, *The Site Command Centre* and
   *Down the hierarchy* for the two before it, and
   `docs/framing-site-command-centre.md` for what the thing is *for*. This file
   carries the state.
5. Adding a widget is a data edit in the right level's catalogue —
   `siteWidgets.js`, `sectionWidgets.js` or `enclosureWidgets.js`. Pick a layout,
   give it content, choose its sizes, and name the decision it serves. Ask first
   whether it belongs one level up: deeper catalogues earn their existence by
   being *more specific*.
6. Adding it to a default is a data edit in `roles.js`, composed with `pair()` and
   `wide()` — and then `antz.checkSiteDefaults()`, which will tell you if you have
   left a hole.
7. Before shipping: `python3 tools/verify.py`, the clipping sweep at eight widths
   across all twelve subjects **measured against each list container and not only
   against the card**, all three console assertions, the Sites listing at nine
   widths, and a console-error check.

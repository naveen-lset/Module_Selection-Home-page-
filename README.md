# ANTZ Command Centre — Home

The Home page and its customizable module dashboard, implemented from Figma.

**Source of truth:** [Antz Modules → Home (iPad Pro 12.9" - 6)](https://www.figma.com/design/CqCR8vdtWyasWENyA02Khv/Antz-Modules?node-id=55476-32828) · node `55476:32828`

### Open it

**Double-click `index.html`.** One file, no server, no install, no build step.
Everything but the images lives in it — the stylesheet is in `<style>`, the whole
application is in the single `<script>` at the foot. The only network request is
for three Google fonts, and it renders without them.

```
index.html      the whole thing
tools/          foliage.py + the supplied header artwork it processes
assets/img/     7 photographs exported from the Figma file, plus foliage.png
assets/icon/    27 SVGs — 25 exported from the Figma file, plus Approvals
                and Communication, drawn in the same idiom for the two
                modules the artboard never contained. Their *fills* are not
                new: see "The palette is closed" below.
```

---

## Fidelity

Measured against the artboard at 1024pt:

| | Figma | Built |
|---|---|---|
| Grid | 5 cols × 179.2px, 16px gap, 164px rows | **identical** |
| Content width / padding | 960px / 32px | **identical** |
| Hero banner | 960 × 204 | **identical** |
| Search field | 960 × 64, r16 | **identical** |
| Gap under the hero | 16px | **16px** — see below; it was 0 for three sessions |
| Card order | 5 rows, 15 cards | **the artboard's 5 rows and 15 footprints, then one Housing tile** |
| Main Frame (node `55476:32852`) | 1024 × 1136 | **1316px** = 1136 + 180, and 180 is exactly one more row (164 + 16) |
| Page height | — | 1691px, with the workspace switcher and the Housing tile |
| Mortality icon frame | +16, +16, 44 × 44 | **identical** |
| Mortality label box | y 108 in content box, h 24 | **identical** |
| Follow Up bullets | 646, 711, 771, 831, 891 | **647, 711, 771, 831, 891** |

Pixel difference over the whole Main Frame was **5.49 / 255** (2.2%) — photo
recompression and font antialiasing — when the default page was the artboard's
own fifteen cards. It no longer is: four of those cards have been swapped for
statistics, progress and attention cards so that the default home page covers
all four things a command centre has to answer before anyone types anything
(see *The default home page is a balance* below). **The grid, the footprints and
the five rows are unchanged** — the same fifteen slots in the same order — so
every measurement above still holds. What is inside four of them does not.

### The sixteen pixels under the hero that were never drawn

The banner sat **flush** against the first row of cards. The artboard does not:
the Main Frame's own arithmetic — written into `cards.css` two sessions before
anyone noticed it was not being obeyed — is

```
32 padding + 204 hero + 16 gap + 5 × 164 rows + 4 × 16 gaps = 1136
```

and the sixteen after the hero had never existed. The built frame measured
**1120**, the grid and every card row under it sat 16px too high, and the
"pixel-exact" claim in the row above was 16px out on the one measurement nobody
had taken. Found by a user looking at the page, not by any of the sweeps —
which is worth recording, because none of them measure *between* two elements.

It is set as `margin-bottom: var(--grid-gap)` on `.hero` rather than as a
literal 16, because that is what the space **is**: on the artboard the gap
between the banner and the cards is the same gap as between two card rows,
which is what makes it read as one grid with a banner in it rather than as a
banner with a grid underneath. The token already steps 16 → 14 → 12 with the
breakpoints; a hard-coded 16 would have been wrong at 768 and 640.

Type sizes are Figma's at the reference width — 24px greeting, 32px name, 36px
hero, 20px search and card labels, 44px figures, 16px body, 14px meta — reached
through `clamp()` so the page still holds together at other widths.

Icons and photographs are the assets exported from the file, not redrawn.

### Nothing was added to the resting page

An earlier pass put a right-aligned **Edit** control above the grid, because the
artboard has no way into edit mode. That row cost 28px and was the only reason
the build was not pixel-exact, so it is gone.

Everything the user can do to their own home page now hangs off **their own
avatar** — a popover with *Edit Modules*, *Add Widget* and *Reset Home Page*.
That costs no pixels at rest, and the avatar is where a person looks for the
things that are theirs rather than the organisation's. Their home page is one of
those.

The three gestures stay, because a long press on a card is what people bring
with them from every phone home screen they have used, and it should not stop
working because a menu appeared:

| | |
|---|---|
| press and hold a card | 500ms, finger or mouse, ≤8px of drift |
| right-click a card | the desktop equivalent of the same intent |
| press <kbd>E</kbd> | anywhere outside a text field |

The 500ms hold is deliberately longer than the 200ms the drag controller uses;
the two never overlap, since the drag hold only arms once editing is already on.
The section header collapses to zero height at rest and expands to 44px with a
title and **Done** once editing — at that point the user is in a mode and needs
to see it.

### Two things the artboard got wrong, and what was built instead

- The **Follow Up** card in the file at time of writing is a list of dated
  updates. An earlier version was a month calendar whose first week read
  "30 1 2 4 5 6 7" — the 3rd missing, eight values laid into seven cells — with
  the Sunday column labelled "SAN". The current list design is what is built.
- The list's five rows are the same string five times, which is placeholder
  copy. Reproduced as drawn; the strings are one array in the script.

### The file moved twice while this was being built

Two edits landed in the Figma mid-implementation, both caught by re-reading the
live node rather than trusting the first fetch:

- **Follow Up** changed from a month calendar to a list of dated updates.
- The layout's **sixth row** — Users, Parivesh and Security repeated at the
  small size — was removed, and a new **Reports** module was added to close
  row 4. Fifteen cards now, not seventeen.

Everything above row 4 is byte-identical between the render I first built from
and the live one, so those two were the only changes.

---

## The widget system

### Eighteen modules, ninety-four cards, and no two modules alike

The failure mode this is built to avoid is giving all eighteen modules the same
five generic cards: it produces a gallery where every module looks identical and
none of the cards is worth adding. So each module exposes only the card shapes
its actual work has —

| | |
|---|---|
| Security | a resting-state card (*All Systems Normal*), a session breakdown, an alert count, an access log — and no progress bar |
| Diet & Kitchen | a feeding plan, a preparation bar, a diet mix, a kitchen queue — and no trend line |
| Fetal Death | three cards, which is the honest total for a module with six records a month |
| Parivesh | six, because a submission workflow has states worth separating |

Every module has one plain **Default** door. That is the floor, and the only
thing all seventeen share.

### Nineteen compositions, and why seven were added

The catalogue began with twelve layouts and they could all answer one question:
*how much*. A stat is how much, a metrics row is how much three times, a queue
is how much of each. Put six of them on a module and you have six ways of
printing a number — which is the failure the layouts were introduced to fix,
arrived at from the other direction.

The seven added here answer the questions an operational home page actually
gets asked, and each one is a question the first twelve could only answer as
another figure:

| | | |
|---|---|---|
| **ring** | what a total is *made of* | a donut and a legend |
| **arc** | how *full* something is | a 240° gauge with the ratio inside it |
| **flow** | where a population has *got to* | stages, counted, with chevrons between |
| **attention** | what needs *someone* | one count, then the named things inside it |
| **meters** | how much is *left* | rows that each carry their own track |
| **entity** | *which one* | a batch, an animal, a result — named |
| **hierarchy** | what *contains* what | indent and elbows, not three counts in a row |

**The visualisations are drawn on the gradient, not on a plate laid over it.**
Every donut segment, gauge arc and meter track is white at an opacity, so the
module's colour shows through all of them. This is the line between a card that
belongs to this system and a dashboard tile dropped into it, and it is the one
rule that made the seven worth building rather than importing.

**Segments are one white at four opacities, not four hues.** Four colours would
read as four categories with meanings of their own, and would collide with
whichever module the card belongs to — a green wedge inside a green card.
Opacity ranks the parts, which is what a composition is actually saying.

**These seven have a type hierarchy that the older twelve do not.** Primary
text is white, a supporting label is 78%, metadata is 62%. That is deliberate
and it is a divergence: an accessibility pass took the opacity hierarchy out of
the original layouts and that decision still stands for them, so the two
treatments exist side by side and are never mixed inside one card. If the
hierarchy should come back everywhere, that is one edit — and it moves the
measured contrast the wrong way, which is why it has not been made unasked.

#### Three things the sweep caught that no screenshot would have

**The featured-entity watermark made every entity card look broken.** The
enlarged module glyph is meant to run off the bottom-right corner into the
card's own padding. Sitting inside the composition element, it made that
element 18px taller than its box at every size and width — indistinguishable,
to anything measuring `scrollHeight`, from real clipping. It is a card layer
now, beside the composition rather than inside it, and the card clips it.

**`overflow-wrap: anywhere` bought a passing sweep and cost the design.** It
lets a flex item shrink below its longest word, so a five-stage pipeline fitted
— as *Requeste / d* and *Processin / g*. It is `break-word` now, and a stage
list that will not fit is offered at a wider size instead of being broken to
suit the one it was asked for.

**A pipeline turns through a right angle when the card does.** Five stages need
width, not height, and `full` gives both: the row sat in the middle of 344px of
empty gradient looking like a fault. At two rows tall the stages stack, the
chevrons point down the way a pipeline reads, and the labels stop having to
survive a 43px column.

### No invented periods

The brief this was built to is blunt about it: no *Today*, no *This Week*, no
*This Month* unless the module's data genuinely has that shape. Three cards
were carrying one and have lost it — *Today's Progress* is **Preparation
Progress**, *Today's Kitchen* is **Diet Distribution**, and Eggs' *Collected
This Month* is now just **Eggs Collected**.

Three kept a time word because theirs is real: Follow Up's *Due Today* is a due
date, Administer's schedule is a list of appointments, and Eggs' incubation
card says *Day 18* — a genuine position in a real 28-day cycle. The one time
series left in the catalogue is Mortality's trend, and its axis is three months
the module actually recorded.

### Five purposes — which order the shelf, and are never drawn

| | |
|---|---|
| **Navigate** | a door. Icon, name, nothing else. |
| **Understand** | a figure, a set of figures, a breakdown or a trend. |
| **Attention** | work that is waiting, overdue, low or unreviewed. |
| **Act** | two or three things you can start from the home page. |
| **Monitor** | what is happening — activity, schedule, progress. |

These are **not shown**. An earlier pass grouped each module's widgets under a
labelled heading with a line of copy on each, and it put a taxonomy in front of
the thing the user came to look at. What the purposes still do is *order* the
shelf, which is the more valuable half: a module reads as a sentence from left
to right — the door first, then the figures, then what is waiting, then what you
can do, then what just happened. Medical is the only module that earns all five.

They stay searchable: typing "attention" or "monitor" finds the right widgets.

### Twelve layouts, two fills, one design language

The previous version of this file gave every card the same skeleton — a label
row, then a stack of content blocks — and varied only what went in the stack.
It read well as data and it failed as design: Medical's five cards came out as
five green rectangles with different words in them, and no preview in the
picker told you anything its caption did not.

A variation now declares a **layout**, and a layout is a whole composition with
its own markup, its own hierarchy and its own fill:

| | |
|---|---|
| `door` · `compact` | a glyph and the module name — the bold coloured tile, upright or on its side |
| `photo` | a photograph with the name in a scrim band |
| `stat` | one number, as large as the card allows |
| `metrics` | two to four figures side by side, separated by space alone |
| `chart` | a trend line that owns the card, summary beneath |
| `queue` | a total, then named rows with figures on a common right edge |
| `status` | dotted rows — a state, not a measurement |
| `progress` | a ratio, a full-width track, a caption |
| `timeline` | dated entries down a hairline rule |
| `recent` | the objects you were last working on |
| `actions` | two to four controls, and the controls are the content |

**Colour is the one thing that does not vary.** Every card is its module's own
gradient with white text; a photograph is the only other fill.

There was a third, briefly, and it was a mistake worth recording. Data cards
were given a `soft` fill — the same gradient under a white veil, dark text — on
the reading that a statistics card wants a calm surface. On a vivid module it
worked. On Follow Up's petrol and Approvals' slate, which are desaturated to
begin with, the veil did not soften the colour, it **removed** it: two grey
cards on a page whose whole premise is that a module is recognisable by its
fill. The variety was never supposed to come from the fill — a queue looks
nothing like a timeline whatever colour they are — and the fill's job is the
opposite one, holding a module's cards together.

What every card still shares: Inter, one type scale, 16px radius, the 4px
spacing scale, the exported Figma glyphs, one hover lift, one press, and the
whole card as the target. **Same design language, different information
composition.**

### No "View →" anywhere

The whole card is the link. Every informational card used to end in a
"View Requests →" that repeated what clicking anywhere already did, cost a line
of vertical space, and competed with the data above it. They are gone. Quick
Actions is the exception, and its controls are the content rather than an
afterthought at the foot.

### Add Module is at the top

It was a tile packed after the last card, on the theory that it lands in the
first free slot rather than in a bar you go looking for. On a fifteen-card page
that theory is wrong: the tile sits below the fold, and the one action a person
opens Edit Modules to perform is the one they have to scroll to find.

It is now a header action — `Edit Modules · ＋ Add Module · Done` — and on a
phone, where those three do not share a line, the row wraps and Add Module takes
the full width underneath, still above the grid. It is dressed as an action,
not as a module: an outlined control sized like Done beside it, because a filled
or card-shaped button there competes with the things it adds.

Two bugs came out of that move, both only visible once the header could wrap.
The header had a hard-coded `height: 44px` in edit mode, so the wrapped row
painted outside its own box; and `.edit-hint` carries `margin-top: -12px`, tuned
for a header that never wrapped, which put the actions 4px inside the hint's
first line. Measured at 1440 / 1024 / 768 / 500: header 44px (94 when wrapped),
zero overlap with the hint or the grid.

### The jiggle, and why it is this small

An earlier version of this file argued for **no jiggle at all**: the page has a
header that changes to read *Edit Modules*, a Done button and a remove control
on every card, so the state is already legible without vibrating at anybody.
That was true and it missed the point. Those all say *the page is in edit mode*.
The jiggle is the only one that says **this card is the thing you can move** —
it is the affordance, not the announcement, and a card that does not move is a
card you have to be told about.

The amplitude is the whole argument. Nothing exceeds **0.75° of rotation or
0.6px of travel** — measured across a live edit session, the worst values seen
were 0.69° and 0.30px. That is under what the eye resolves as motion on a
stationary object and over what it resolves as life. The naive version of this
effect uses 3° and 5px, and at that size a command centre does not look
editable, it looks broken.

**Three keyframe sets, and a phase per card hashed from its uid.** Fourteen
cards on one synchronised animation is not fourteen jiggling cards, it is one
jiggling grid. The phase comes from the uid rather than the index — the index
changes on every reorder, so the whole page would visibly re-synchronise on each
drop — and rather than from `Math.random()`, because the grid reconciles instead
of rebuilding, so a surviving card would keep an old value while a new
neighbour got a fresh one. Hashed from the uid it is a property *of the card*:
it survives reordering, resizing, re-rendering and a reload.

The hash is FNV-1a, not the usual `h * 31 + c`. Uids differ in one or two
characters and a weak hash leaves that difference in the low bits; the first
attempt took its duration from bits 5–7 and produced **two distinct durations
across fifteen cards**, so the grid still drifted into step. Durations matter
more than delays here: two cards sharing a duration drift back into phase no
matter how they were offset, two on different durations never do.

**The battery objection is answered rather than dismissed.** Only `transform` is
animated, so the whole thing lives on the compositor and never touches layout or
paint; it runs only inside edit mode; `prefers-reduced-motion` stops it through
the global block; and it is paused outright when the tab is hidden.

**Jiggle and drag never share a transform.** The animation runs on the `.card`,
the FLIP reflow runs on the `.slot`, and the dragged card is a clone in a fixed
layer — three different elements, so nothing has to arbitrate. The source slot's
animation is switched off for the duration of the gesture and comes back on the
drop.

### Attention is not a red card

The brief says it twice — Hospital's critical card must use "subtle attention
styling, not a full red background", and "do not make every Mortality card red"
— and both are the same mistake. A module repainted by its worst news stops
being recognisable, and a grid where four cards are red trains everyone to stop
seeing red.

So an attention card keeps its module's own fill and says so with a warning
glyph in its label row and the warm accent on its note. Mortality's fill is its
own coral throughout, and only its *review queue* — the one card actually
waiting on someone — takes the accent.

It carried a hairline ring as well, and that is gone. On a grid where only one
or two cards are ever in this state, a ring reads as a card that has been
*selected* rather than one that needs attention — and the glyph was already
doing the work.

### The default home page is a balance

Seventy-one cards exist and **fifteen** are on the default page. Not for
tidiness: a home page carrying every card has no hierarchy, which is the same as
having no home page. The fifteen cover all four things a command centre has to
answer before anyone has typed anything —

| | |
|---|---|
| Navigate | Medical · Hospital · Pharmacy · Diet & Kitchen · Lab · Mortality · Eggs · Administer · Users · Security · Reports · Parivesh |
| Understand | Species Statistics |
| Attention | Pending Approvals |
| Monitor | Follow Up Task Queue |

Hospital and Diet & Kitchen are their **photographs** rather than their figures
— the artboard's own two photographic module cards, back on the page they were
drawn for. Their statistics, Live Status and Today's Preparation, are one click
away in the gallery.

`priority: 'primary'` in the catalogue means **exactly** "one of these fifteen".
There is no third state and no exception list, so the rule can be checked rather
than remembered — `antz.checkDefaults()` asserts the two files agree in both
directions. It found two disagreements the first time it ran.

The arrangement is still the artboard's: five rows, no gaps, the same fifteen
footprints in the same order, and both photographic cards kept.

---

## How it works

### A card stores a *meaning*, never a measurement

A card is `{ uid, variantId, size }`. `size` is a word — `'large'` — not a
width. Column count belongs to the viewport, so one stored card resolves
correctly at every breakpoint through a single table:

```
          2 cols    4 cols    5 cols    8 cols   12 cols
small     1 × 1     1 × 1     1 × 1     1 × 1     2 × 1
medium    2 × 1     2 × 1     2 × 1     2 × 1     3 × 1
large     2 × 2     3 × 2     2 × 2     4 × 2     4 × 2
tall      1 × 2     2 × 2     2 × 2     2 × 2     2 × 2
full      2 × 2     4 × 2     5 × 2     8 × 2    12 × 2
```

Turning an iPad sideways costs nothing: the column count changes, spans
re-resolve, the packer re-runs, and the saved layout was never touched.

The **5-column row is measured, not chosen** — every small card in the artboard
is 179.2px, and (960 − 4×16) ÷ 5 = 179.2 exactly. An earlier requirements note
said six columns at this width; the Figma is the more specific instruction.

The **8 and 12 columns are currently unreachable** — the page is capped at 1024
(below), so `--grid-cols` never rises above five. They are kept because the
table is the size contract rather than a cache of it: delete the rows and
lifting the cap later resolves every span to 1×1 with nothing to say why.

### The page is the artboard, on every screen

`.page` is capped at **1024px** — 960 of content inside 32px margins, which is
exactly the Figma frame. Above that it centres, and nothing reaches past it:
not the grid, not the hero banner, not the header planting, not the status bar,
not the Add Widget panel. Measured at 1024 / 1280 / 1440 / 1920 / 2560, the page
is 1024px and the banner 960px at every one of them.

It was capped at 1440 before, which let a desktop stretch a design drawn for a
tablet.

**Two things had to be pinned with it, and missing either breaks the page.**

*The column count.* `--grid-cols` is set by media queries, which measure the
**viewport**, while the grid divides the **page**. While those grew together the
arrangement was sound; the moment the page stops growing they diverge, and a
1920px monitor asks for twelve columns inside 960px of content — 57px cards, on
a design whose smallest card is 179. The 8- and 12-column bands are therefore
gone and five is terminal: above 1024 the page is always the artboard, so the
artboard's five columns are always the answer.

*The type.* Every `--fs-` token is a `clamp()` on `vw`, tuned to land exactly on
Figma's value at 1024 and keep growing past it. Pinned page, unpinned type, and
a 1920px monitor renders artboard-width cards carrying desktop-width text. Above
1024 they are frozen at the values those clamps already produce there — and the
Figma-referenced ones land on round numbers (24, 32, 36, 20, 44, 16, 14, 12)
because they were derived to, which is as clear a confirmation as you get that
the two definitions agree. Nothing jumps at the breakpoint; the curve stops.

Below 1024 nothing changed: the page still fills the viewport, the columns still
step 2 → 4 → 5, and the type is still fluid.

### Three things the exported values got wrong

Each of these was found by measuring the render, not by reading the export.

**`lineHeight: 100` does not mean `line-height: 1`.** Every Antz text style
reports it, and it reads like a ratio of 1. In Figma a percentage line height of
100% means 100% of the font's own default — Auto. The node metadata settles it:
a 20px Module Name occupies a 24px text frame, which is Inter's normal 1.21.
Setting these to 1 was tried and measured worse, and is reverted.

**My own container query was overriding Figma.** A rule shrank icons to 36px and
labels to a 1.1em clamp on any card under 200px wide — which is every 1×1 card,
including all of the reference ones. Figma puts a 44px glyph and a 20px label on
every module card. Measured, `--fs-card` was computing to 17.6px instead of 20px.
Removed.

**The Follow Up photograph is cropped to its bottom, not its centre.** A plain
centred `cover` lands on the pale cloud band; Figma shows the deep teal below it.
`object-position: 50% 98%` was solved by fitting the rendered card's own pixels
and drops that card's mean channel error from 119 to 74. The same fit was run on
the other three photographs and all measured centred to within noise, so they
are untouched.

The update rows also needed `line-height: 1.2` rather than `normal`: Figma's
bullets sit 60px apart and mine were 61, and the 1px-per-row drift pushed the
fifth row out of the 264px window that is meant to cut it in half.

### The widget gallery, and the two versions of it that hid modules

There have been three versions of this screen. The first two both hid modules,
in opposite ways.

**v1 — one long scroll.** Every module's previews in a single column. With
fifteen modules that came to **5,308px of gallery inside a 902px window**:
Medical, Hospital and half of Pharmacy were visible and the other twelve were
below the fold with nothing to suggest they existed.

**v2 — a grid of module tiles you clicked into.** All fifteen were on screen at
once, which fixed the fold — but only until you opened one, at which point the
other fourteen vanished behind a **Back** button. Comparing Pharmacy's queue
card with Medical's meant two navigations and a memory test.

**v3 — a persistent vertical rail**, which is the shape Apple's widget gallery
settled on, and for the same reason. Every module is listed down the left,
grouped under its category, **always**. Choosing one swaps the pane beside it
rather than navigating, so moving between modules costs nothing and no module is
ever more than a scroll from being seen. Below **768px** — a phone — there is
no room for two columns, so the rail *is* the sheet and the widgets slide over
it, which is exactly what iOS does at that width. Same two panes, same code, one
`grid-template-areas` swap.

**Two independent things change across the breakpoints, and for a while this was
written as though they were one.** The *layout* splits into two panes at 768px;
the *presentation* changes at 1024px, where the bottom sheet lifts off the edge
and becomes a centred panel. Both lived in a single `min-width: 1024px` block,
which meant every iPad in portrait — 768, 810, 820 and 834pt — was handed the
phone's stacked arrangement despite having ample room for the rail. Only the
12.9" is 1024pt in portrait, so it was the one tablet the old breakpoint got
right. They are two decisions and they are now two blocks.

The script needs to know which arrangement is live, and it asks the cascade
rather than keeping its own copy of the number: the stylesheet sets
`--picker-split` and `isSplit()` reads it, the same arrangement as
`currentColumns()` and for the same reason — there used to be a hard-coded
`innerWidth >= 1024` in the component that would have gone on believing every
portrait iPad was stacked after the CSS moved.

A module's widgets are **one shelf of previews with a name under each** — no
group headings, no descriptions, no size counts, and no card count beside the
module in the rail. All of those were tried and all of them were prose in front
of a picture that already says what the widget is; with 3 to 6 widgets a module,
that prose was most of the pane. The purposes still order the shelf (above); the
sizes are still on the footer's selector, where they are a choice to make rather
than a fact to read.

Search matches module names, keywords, purposes, widget names **and every figure
and label the card shows** — "overdue", "population", "hatching", "low stock",
"all systems" each find the right card and narrow the rail to the modules that
have one.

### The selection is a basket, not a cursor

The gallery used to hold **one** chosen widget. Adding three cards therefore
meant open → pick → **Add to Home** → reopen → pick → **Add** → reopen → pick →
**Add**: the sheet threw away everything you had learned about it twice, and the
module you were comparing against was two navigations behind you each time.

It now holds a selection you build up. Clicking a preview adds it; clicking it
again takes it out, because the way out of a selection should be the gesture
that made it. The count and the action say what will happen — **3 Selected**,
**Add 3 Modules** — and the whole batch is added in a single store write, so the
packer places the group at once and the grid runs one FLIP pass rather than
three fighting each other.

**It is a `Map`, keyed by variant id.** Insertion order is the one thing a Map
guarantees, and the order a curator picks widgets in is the order they should
arrive on the page — appended in that order, which is what lands them in the
first free positions the packer can find instead of scattering them.

**The basket survives browsing.** Changing module and typing a search both used
to clear it, which would have made multi-select useless the moment a curator
wanted two Medical cards and a Pharmacy one. Only opening the sheet clears it.

**Sizes are per card, and the tray is what makes that reachable.** The footer's
size control has to have exactly one subject and the basket has many, so it
follows the most recently touched card and names it — *Size for Care Overview*.
That alone would be a trap: clicking a selected preview deselects it, so there
would be no way back to re-size something picked three tiles ago. Hence the
tray — a chip per selected card, showing its chosen size; the chip body hands
the size control to that card, the × drops it from the basket.

The tray scrolls sideways rather than wrapping, because a wrapping tray changes
the height of a fixed bar as cards are added and moves the Add button out from
under the thumb aiming at it. Two details came out of testing it: the active
chip is scrolled into view, **aligned to its leading edge rather than centred**
— centring cut the previous chip after its name, so the tray showed a pill
reading just "Medium" — and the edge fades are set from the scroll position, so
an edge is only soft when there is genuinely something past it.

**The bar is stacked below 1024px, not just on phones.** Side by side, the
actions take about 250px of it, and on a split layout the rail has already taken
240 off the left: an iPad in portrait gave the chips 128px to hold three chips
totalling 562, and the active one could not be scrolled into view because there
was no view to scroll it into.

### Three defects the gallery exposed

The first two were invisible on the home page and obvious the moment a picker
drew every card:

- **Three module fills were translucent.** Figma gives Species, Diet & Kitchen
  and Hospital an alpha fill because on the artboard those three only ever sit
  *on top of a photograph* — the alpha is the photograph showing through.
  Transcribed literally, a Species or Hospital card with no photograph under it
  painted 32%-alpha teal onto white, and the picker's module chips, which wear
  the same fill behind a white glyph, came out as pale ghosts beside the twelve
  opaque ones. They are now opaque ramps of the same three hues, built the same
  way as the rest of the palette. The photographic cards never read these tokens
  at all, so they are untouched.
- **`gradient-stat` cards had no fill.** The background rule named only
  `data-treatment='gradient'`, so every "figures" card was white text on
  nothing. No such card was in the default layout, so it had never shown.
- **Module glyphs drew nothing.** They became exported SVG files when the design
  was implemented, but the picker still asked the sprite for them —
  `<use href="#i-m-medical.svg">` resolves to nothing. Once fixed they were
  still invisible: the exported glyphs are white, for dark cards, and the chip
  behind them was pale. They now carry the module's own gradient.

A fourth was found by measurement rather than by eye: the preview renderer was
still building cards against a 146.7px reference column from when the grid was
six columns wide, so every preview was the wrong size and its container queries
dressed it for a card that no longer exists.

### The header planting

A band of foliage behind the greeting, dissolving before the search field. The
artwork was supplied as a flat PNG; `tools/foliage.py` turns it into the asset
the page uses and `assets/img/foliage.png` is its output.

**The artwork had to be un-composited before it could be used at all.** It
arrives opaque, on its own flat ground of `rgb(228,241,244)` — a blue that is
not this product's mint canvas. Dropped in as a background it paints a rectangle
of the wrong colour with a hard edge on all four sides, and no amount of masking
rescues that, because the ground is part of the picture. So the script measures
the ground from the four margins, turns every pixel's departure from it into
alpha, and solves `P = ink·a + bg·(1−a)` for the ink underneath. What comes out
is transparent and sits correctly on anything.

Two things fell out of measuring it. The ink is **one colour** — over every
pixel above 55% alpha the recovered hue spans five degrees, 177.7° to 183.1°,
at essentially constant saturation and value. It is a single teal wash at
varying density, so the per-pixel colour is discarded and `#5EBFC0` written into
all three channels; nothing visible is lost and the file drops by roughly two
thirds, because constant channels compress and recovered noise does not. And the
bare paper still reads about 2.5/255 away from the ground, which left in becomes
a grey haze over the whole header, so it is subtracted before anything is
normalised.

It is also **mirror-paired**, because the source is a one-off illustration whose
left and right edges do not meet. A mirrored pair always does, so `repeat-x` has
no seam at any width.

**The crop is the layout.** There is no nudging in the CSS: `background-size:
auto 100%` maps the crop onto the box, so the crop's proportions place the
artwork. Measured off the source row by row, the first leaf tips appear at
y=105, the mass peaks at y=380 and it is back to bare paper by y=560. The crop
takes **70 to 560** — nearly the whole illustration — which lands the tips at
31px, clear of the greeting at 32, and the peak of the mass at 278.

An earlier version cropped 85–400 into a 220px box that stopped above the search
field. The band is now 440px and runs the full depth of the header, past the
field and behind the hero banner, so there is room for all of the artwork; at
the old depth a full crop scaled the leaves to nine pixels.

**The fade is a mask, not a gradient.** The obvious way to soften the bottom of
an illustration is to lay a background-coloured gradient over it, and it is
wrong here twice over. The page wash is a translucent double gradient that
changes down the document, so an overlay would be chasing a moving target and
would show as a pale block the moment it missed. And an overlay fades the whole
band uniformly — leaves and gaps alike — which reads as fog rather than as
planting thinning out. `mask-image` removes the artwork's own alpha instead, so
the leaves dissolve individually and the gaps stay exactly as transparent as
they already were. There is no boundary to see because there is no second layer.

**The stops are in pixels, and they are the requirement.** Percentages would
float with the box height and hide what the numbers mean; these are absolute and
measured against the page. Solid from 0 to **239px** — the search field runs
135–199, so the planting is at full strength the whole way down the header,
behind the field and through the gap under it, with its tips clearing the top of
the field by a hundred pixels. Then **239 → 428px** of feather: 239 is forty
pixels below the foot of the field, and 189px of ramp is long enough to read as
atmosphere rather than as an edge. Eight stops, so the falloff eases.

**One thing to know about where that feather lands.** The hero banner starts 32px
below the search field, so a fade beginning at 40px starts 8px *inside* it and
runs its whole length behind an opaque photograph. What is actually visible is
the planting at full strength down to the hero's top edge, and the feather
showing only in the page gutters either side of the card. That is the
instruction carried out exactly — if the feather should be seen across the page,
it has to begin at the foot of the field instead, and there are 32 pixels to do
it in.

The band now reaches the hero, which meant lifting `.main-frame` out of its way:
positioned elements paint above unpositioned in-flow siblings whatever the
source order, so without `position: relative; z-index: 1` the foliage would lie
over the top of the leopard.

**And a second mask layer thins it behind the greeting**, because the planting
must not cost readability. Measured on the render with the glyphs made
transparent and the true painted ground sampled underneath:

| | no planting | planting | + thinning |
|---|---|---|---|
| "Good Morning," `#00ABAB` | 2.65:1 · 2.62 worst px | 2.65:1 · **2.24 worst px** | 2.65:1 · 2.48 worst px |
| "Sourav Tambe" `#1F415B` | 10.16:1 · 10.04 worst px | 10.06:1 · 8.56 worst px | 10.15:1 · 8.91 worst px |

That layer only *thins* — it does not clear — and its strength tracks the depth
of the band. While the planting stopped above the search field, holding its
centre at 0.30 was enough. Now that it runs at full strength the whole depth of
the header, the same ellipse left the greeting at 2.24:1 against a 2.62:1
baseline; at 0.06 it measures 2.48:1. That is about a tenth of a point of loss
against the 0.38 it was costing, and it keeps the illustration whole rather than
erasing it across the left of the header.

### The palette is closed

**Sixteen gradients, all from the Figma file, and no seventeenth.** An earlier
pass invented an indigo for Approvals and an amber for Communication; both were
reverted. The two modules the artboard never drew borrow from the file instead —
**Approvals wears Users' slate, Communication wears Follow Up's petrol.**

Duplication is native to this palette anyway: in the Figma file, Reports and
Parivesh already share one cyan and Pharmacy and Follow Up already share one
petrol. Two more pairs is consistent with it, and a colour that is not in the
file is not.

*Which* two was a legibility decision rather than a semantic one. The obvious
pairing was Administer's sage for Approvals — its blurb is literally "approvals,
authorisations and administrative queues" — and Administer's sage is the
**lightest fill in the set**, `rgb(179,198,188)` to `rgb(155,176,163)`. That is
fine behind a door carrying two words and poor behind Approvals' primary card,
which is on the default home page carrying a count, a note and a warm accent
line; rendered, it was close to unreadable. Slate and petrol are the two darkest
fills in the file that were not already carrying a data-heavy card.

If you would rather have the semantic pairing back, it is one line each in
`modules.js` — but the contrast is the reason it is not there now.

### Gradients are sampled, not transcribed

Figma reports each card fill as two alpha stops, e.g.
`rgba(0,109,53,.16) 48.848%, rgba(0,109,53,.8) 74.362%`. Pasting those into CSS
is wrong: a Figma gradient handle is positioned independently of the shape, and
on these cards it runs well past the corners, so the card shows only a slice of
the ramp — while CSS maps 0–100% onto the shape's own diagonal.

Transcribed directly, every card came out right at its dark end and far too pale
at its light end. Measured: the top-left of Medical was `#E7FAF9` against
Figma's `#86B99F`, while the bottom-right matched to within one unit.

So each fill is the **rendered** ramp, sampled at ten points along the card's
own gradient axis. A linear gradient is constant perpendicular to its axis, so
every stop is the median of a full perpendicular scan line — which also rejects
the white icon and label glyphs sitting on the axis.

### Other decisions worth knowing

**A computed packer, not CSS auto-placement.** `grid-auto-flow: row` leaves
holes as soon as spans are mixed; `dense` fills them but will not say where it
put anything, and drag-and-drop has to know. Placement is first-fit, computed,
so the coordinates stay in our hands. Only the order is persisted; coordinates
are derived from (order × column count) every render.

**Row breaks are explicit.** The artboard's last two rows are Parivesh +
Security, then Users + Parivesh + Security, with two cells left deliberately
empty. First-fit would pull the second group up into that gap — tidier, and not
what was drawn — so a `newRow` flag holds the grouping.

**Pointer Events, not HTML5 drag-and-drop**, which has never worked on touch.
One code path serves a finger and a mouse.

**A long press, not `touch-action: none`.** Disabling touch scrolling on the
cards would make dragging reliable and the page unscrollable. A finger still for
200ms is not scrolling, so at that moment the gesture is taken; before it, the
page scrolls normally.

**Previews are the cards.** The picker builds a real card at real size and
scales it with a transform, which does not change what a container query sees —
so a full-width preview lays itself out exactly as it will on the page.

**A keyed reconciler, not a re-render.** Rebuilding the grid on every state
change would destroy the element mid-drag along with its pointer capture,
restart every transition, and throw away focus. `grid-area` is not animatable,
so movement is played back with FLIP.

---

## Accessibility — measured, and honest

Re-run **31 August 2026** against the full catalogue, replacing an audit of the
old fifteen-card page that had been left in this file marked stale. The earlier
figure — *23 of 30 text runs below AA* — is withdrawn; it measured a page that
no longer exists.

It was measured twice, by two methods that do not share an assumption. Every
stop of all sixteen gradients was walked analytically and every ink the layouts
put on them composited against it; and then the whole catalogue was rendered and
the painted pixels sampled directly. The two agree.

**Nothing here is fixed.** A remedy was built and reverted — see *The remedy
was built, measured, and taken back out*. The gradients render exactly as Figma
drew them.

### Before — white text cleared AA on none of the sixteen fills

At its lightest stop, the best fill in the set reaches 3.78:1 and the worst
1.49:1, against the 4.5:1 that AA asks of body text.

| | fill | light end | of the card below AA | below 3:1 |
|---|---|---|---|---|
| worst | Parivesh · Reports | **1.49:1** | all of it | all of it |
| | Eggs | 1.62:1 | all of it | all of it |
| | Lab | 1.65:1 | all of it | all of it |
| | Administer · Approvals | 1.79:1 | all of it | all of it |
| | Medical | 2.09:1 | all of it | 42% |
| | Mortality | 2.10:1 | all of it | all of it |
| | Diet & Kitchen | 2.17:1 | all of it | 69% |
| | Fetal Death | 2.20:1 | all of it | all of it |
| | Security | 2.76:1 | first 67% | first 17% |
| | Pharmacy · Follow Up | 3.01:1 | first 56% | none |
| | Users · Communication | 3.22:1 | first 45% | none |
| | Species | 3.29:1 | first 38% | none |
| best | Hospital | 3.78:1 | first 21% | none |

**Ten of the sixteen clear AA at no point on the card.** That is the load-bearing
sentence: this is not a defect a layout can move text away from, because on
those ten there is nowhere to move it to.

### The three semantic tones are worse, everywhere

`--c-ok`, `--c-warn` and `--c-alert` are tinted, and on a dark ground white is
the best possible ink — so a tint can only measure worse. On the worst fill they
run 1.12:1 to 1.21:1, and they fail AA on **all sixteen**, at every point.

This matters more than it looks. On a ground where white *exactly* clears 4.5:1,
no tint clears it at all: the tone would need a relative luminance of 0.989,
where white's is 1.0. Any ground dark enough for the tones is meaningfully
darker than one merely dark enough for white.

### The dominant defect is opacity, not the palette

The data layouts express hierarchy by fading white, and that — not the gradients
— is what puts most runs furthest below the line:

| | |
|---|---|
| `.l-stat__label` | .78 |
| `.l-queue__text` | .74 |
| `.l-status__text` | .72 |
| `.l-chart__delta` · `.l-progress__caption` | .70 |
| `.metric__label` | .68 |
| `.l-stat__sub` · `.l-progress__of` · `.l-timeline__meta` · `.l-recent__kind` | .60–.62 |
| `.l-recent__when` | **.55** |

A 55%-opacity white is a far weaker ink than white, and it is used on the same
fills. Sizing any fix to full-opacity white — the obvious move — leaves every one
of these runs still failing.

### The remedy was built, measured, and taken back out

A full fix was implemented and then reverted on the project owner's
instruction. It is written up here because the measurements are the useful
part and because the next person will otherwise propose it again.

**What it was.** A flat black veil composited over each fill as a second
background layer, one alpha per module, each sized so that module's lightest
stop — its worst point — cleared 4.55:1 against every ink the cards use. Black
rather than a grey scrim: both reach 4.5:1, but multiplying toward black scales
chroma while mixing toward grey collapses it, so at equal contrast the grey
needs .60 and keeps 38% of the palette's saturation where black needs .44 and
keeps 59%. Per module rather than one shared value, because a single veil has to
satisfy Parivesh and would then spend that same darkening on Hospital, which
needs half of it. Sized to the semantic tones rather than to white, because the
tones are tinted and on a dark ground white is the lightest possible ink — a
tint can only measure worse, so sizing to white leaves every toned run failing.

**It worked.** 530 gradient-card text runs, worst pixel 4.79:1, none below AA,
cross-checked against 64,064 ink × point combinations across the palette.

**And it was the wrong trade.** The mean darkening was .42 and the brightest
fills took more than half: Lab went from gold to olive, Mortality from coral to
brick, Eggs from bright cyan to dark teal, Administer from sage to grey. Pairs
of modules closer than dE 10 went from 5 to 12 — Administer and Security were
20.2 apart and became 4.9. Holding every fill to the same contrast ceiling means
holding them to the same luminance, and what is left to tell modules apart is
hue alone. On a page whose entire premise is that a module is recognisable by
its colour, that is not a tuned design, it is a different and worse one.

This is exactly the trap *The palette is closed* warns about, and it was walked
into anyway. **The instruction on this project is to build the Figma artboard
exactly. Contrast conformance does not override it.** If the fills are ever to
change, that decision belongs in the Figma file, not in a CSS overlay applied
after the fact.

### What was kept, and what it bought

Two things survived the revert, both of which leave every gradient untouched:

- **The opacity hierarchy is gone.** Eleven rules faded white text to between
  55% and 78% to express hierarchy — `.l-recent__when` at .55 was the worst —
  which is a weaker ink on the same fills, and it was the larger half of the
  defect. All eleven now run at full opacity and lean on the size and weight
  difference already sitting beside them.
- **The Quick Actions chip is a dark plate**, not 18% white. The light plate was
  lightening the ground beneath its own white label: 2.38:1, worse than the bare
  card at 2.99:1. The same tint of black reads 4.26:1.

Measured over the whole catalogue, before and after, sampling the true painted
ground beneath every run:

| | runs below AA | below 3:1 | worst run |
|---|---|---|---|
| before | 483 of 530 | 305 | 1.43:1 |
| **now** | **472 of 530** | **291** | **1.49:1** |

**That is a marginal improvement and it is not presented as more.** The page
does not meet AA on its card fills and will not while the palette is the
artboard's. The finding stands as documented, not fixed — which is what it has
been for this project's whole life, now with numbers behind it.

### Still outstanding — the photographs

**The seven photographic cards were not fixed and still fail.** Ten of their
sixteen text runs are below AA, worst 2.67:1 on the Species figures. They are a
different problem with a different fix — the ground is an image, so it needs the
`--scrim-band` extended behind the text rather than a flat veil, and the right
alpha can only be found by sampling each photograph. The greeting, at Figma's
own `#00ABAB` on the mint canvas, is also still 2.53:1 against a 3.0:1
requirement.

The **Edit** control is the exception — it is not in the artboard, so its cyan
was darkened from `#00AFD6` (2.40:1) to `#007A95` (4.61:1). It is only visible
in edit mode.

---

## Verified

| | |
|---|---|
| Layout vs artboard | 5 rows, 15 cards, same footprints in the same order; page height unchanged |
| Catalogue | **17 modules, 74 variations, 150 variant × size combinations** · 3–6 per module, no two modules alike |
| Catalogue ↔ default page | `antz.checkDefaults()` · **0 disagreements**, both directions |
| Every variant at every size | **150 combinations, at 1920 / 1440 / 1280 / 1024 / 900 / 834 / 768 / 640 / 500px** · measured, not eyeballed: `scrollHeight` vs `clientHeight` on every composition root and `scrollWidth` vs `clientWidth` on every label · **0 overflowing, 0 clipped** |
| Responsive | 390 / 834 / 1024 / 1194 / 1440 / 1728px · **0 overlaps, 0 horizontal scroll** |
| Content cap | 1024 / 1280 / 1440 / 1920 / 2560px · page **1024px** and banner **960px** at every one · 5 columns, type frozen at the Figma values, **0 elements outside the page box** |
| Packer | 2 / 4 / 5 columns · **0 cell overlaps, 0 spans exceeding the grid** |
| Drag | mouse, touch long-press and keyboard · live reflow, correct commit, clean teardown. Driven over **CDP `Input.dispatch*`**, not synthetic events — a synthesised `PointerEvent` cannot hold pointer capture, so it lifts a card and then never reorders it, which is why an earlier pass recorded drag as unverifiable |
| Gallery | 17 modules in the rail, always · module → widget → size → add, end to end |
| Rail anchored | **768 / 834 / 1024 / 1440px** · both panes live, back button hidden, rail still visible after choosing a module · add flow end-to-end at 768 and 834 |
| Palette | **16 gradients, all from the Figma file** · 0 invented |
| Palette untouched | **0 `rgb()` stops changed** in the whole history of the contrast work — the veil was an overlay, never an edit to a gradient. After the revert, every card fill renders **pixel-identical** to the pre-contrast build; the only pixels that differ across the whole page are the secondary text runs that are no longer faded |
| Header planting | 1440 / 834 / 500px · masked fade, no hard edge, no gradient block · **0 horizontal scroll** |
| Planting vs readability | greeting measured before/after · mean **2.65:1 → 2.65:1** and 10.16 → 10.15; worst pixel 2.62 → 2.48 and 10.04 → 8.91 |
| Planting stacking | hero banner paints **over** the 440px band at 1440 / 834 / 500 · hit-tested, not eyeballed |
| Search | names, keywords, purposes **and card content** — "low stock", "overdue", "population", "hatching", "all systems", "communication" |
| Persistence | `localStorage` **v4** with versioning and repair · survives reload, verified by round-tripping the arrangement through `Page.reload` |
| Edit entry | profile menu, plus 8 gesture cases: long-press (mouse + touch), right-click, <kbd>E</kbd>, and the four that must NOT trigger — short click, press-and-scroll, typing in search, resting state |
| Banner link | `<a href target="_blank" rel="noopener">` to the Command Centre · clicked: this tab stays put, so the new tab is doing the work · name reads "Antz Command Centre (opens in a new tab)" · no underline, no link colour, box unchanged at 1920 / 1024 / 500 |
| Card links | Species Management is an `<a target="_blank" rel="noopener">`, every other card still a `<button>`, every picker preview still an inert `<div>` (0 hrefs, 0 focusable) · click at rest does not navigate this tab; click in edit mode is prevented; keyboard reorder of the linked card still commits |
| Multi-select | select one / several / deselect by tile / deselect by chip · count and action label track the basket · basket survives changing module **and** searching · per-card sizes committed as picked · batch added in one write, all cards land, picker closes, edit mode persists |
| Selection tray | active chip scrolled into view and fully visible at **390 / 768 / 1024 / 1280 / 1600px** · 0 horizontal overflow at any of them |
| Jiggle | all cards animating, **15/15 transforms changing** over a live sample · not in lockstep · measured amplitude **0.69° rotation, 0.30px translation** · stops on the dragged card, resumes on drop · stops on Done · absent at rest |
| Jiggle phase | stable across removal, keyboard reorder and re-render — hashed from uid, so a card keeps its phase |
| Errors | **none** — no console errors, page errors or failed requests |

Two high-severity defects found by an adversarial review of the previous pass
are fixed and regression-tested: a drag returned to its own slot left the grid
pinned to a stale card list, and a prototype key such as `toString` in a saved
layout took the whole page down at module-evaluation time.

---

## The Site Command Centre

A second workspace, reached from a segmented switch under the search field:

```
[ Module Selection  |  Site Command Centre ]
```

Module Selection is the home page above, unchanged. The Site Command Centre is
a configurable operating surface for one Site — `Housing → Sites → Site` — and
it answers a different question. The home page answers *"which function do I
want?"*. This answers *"how is my Site doing?"*, which no module card could,
because module cards aggregate across the whole organisation.

The framing that produced it is in [docs/framing-site-command-centre.md](docs/framing-site-command-centre.md):
the problem, the stakeholder map, eleven recurring decisions in
Decision → Question → Insight → Action form, the scope boundary, and a YELLOW
readiness verdict with its named risk.

### The IA is function-first; accountability is place-first

Eighteen modules cut the organisation **vertically** by function. A Site is
where those verticals collide **horizontally**: one place, one budget, one
generator, one team, one licence, one set of animals. Anyone whose
accountability is a *place* rather than a *function* had no home in the
product — to answer "how is my Site doing?" they had to visit many modules and
assemble the answer in their head.

So the Site Workspace groups by **domain** — People, Finance, Assets,
Utilities, Safety, eighteen of them — and each domain names the module its
cards navigate into. That is the whole of the relationship. The workspace is
**context, summary and navigation**; the module is where the work is done.

### It is the same engine, and that was the point

| | |
|---|---|
| Widgets | **83 across 18 domains**, 204 widget × size combinations |
| New compositions | **2** — `health` and `insight` |
| Reused compositions | **17** — every layout the module catalogue had except `compact` and `photo` |
| New components | 3 — the switcher, the Site header, a small anchored menu |
| Forked components | **0** |

Of the eleven widget types the brief asks for, nine already existed:

| Brief widget type | Composition |
|---|---|
| KPI | `stat` |
| Status | `status` |
| Progress | `progress` · `arc` · `meters` |
| List | `queue` |
| Trend | `chart` |
| Distribution | `ring` · `metrics` |
| Action | `attention` |
| Timeline | `timeline` |
| Map / hierarchy | `hierarchy` |
| **Health** | **new** — a gauge and the domains the index is made of |
| **Insight** | **new** — measured change, in sentences |

The grid, the packer, the semantic sizes, the drag controller, the edit mode,
the size popover and the widget gallery are the *same instances of the same
components*, configured differently. There are exactly three seams:

```js
createModuleGrid({ isCore })            // the home page locks two cards; the workspace locks none
createModulePicker({ source })          // a rail of modules, or a rail of domains
createEditMode({ labels })              // "Add Module", or "Add Widget"
```

Everything else is resolved before it reaches a component: site widgets
register into the same id lookup as module cards, so `renderCard` does not know
there are two catalogues and does not need to.

**A second gallery was the obvious shortcut and would have been a slow
mistake.** That file is seven hundred lines of behaviour that took three
attempts to get right — the basket that survives browsing, the tray that lets
you re-size a card you picked four tiles ago, the split that becomes a stack on
a phone, the search that indexes what a card *shows* rather than what it is
called. A copy would have started drifting on the first bug fixed in one of
them.

### Every widget traces to a decision

`decision` on each widget names the recurring decision from the framing
document that it exists to serve — D1 *escalate or absorb*, D3 *which failing
thing do I fix first*, D5 *can I still spend*. It is never rendered. The rule
is that a widget tracing to no decision is cut, however easy its data is.

Three were cut under it: a **Total Enclosures** KPI (the header already says 48,
and knowing the number changes nothing anybody does), a **Staff Birthdays** list
(a nice thing, not an operational one), and a **per-species population
breakdown**, which belongs in Species Management and would have been the
workspace pretending to be a module.

### Five roles, one workspace

The wrong implementation is five dashboards: identical on day one, five
products by the end of the quarter. A role contributes exactly two things —
a **permission set** and an **ordered list of widget ids**. Both are plain data.

| Role | Opens on | Widgets | Domains | Cannot see |
|---|---|---|---|---|
| Site Manager | Site Status | 29 | 11 | — |
| Veterinarian | Veterinary Cases | 21 | 10 | Finance · Assets · Maintenance · Utilities · Vendors · Risk · Insights |
| Biologist | Species at Site | 21 | 8 | as above, plus Safety and Emergency |
| Facility Manager | Critical Equipment | 22 | 9 | Finance · Animal Operations |
| Administrator | People | 21 | 10 | Assets · Maintenance · Utilities · Inventory · Animal Operations |

The Manager default is the brief's own §20 order: Health and Attention, then
People and Budget, then Infrastructure full width, then Maintenance and Assets,
Utilities and Animal Operations, Upcoming and Activity. §20's "optional" row —
Compliance, Risk, Inventory — is deliberately **not** seeded; it is one tap away
in the gallery, and a default carrying everything has no hierarchy left to
offer.

**Permission is subtractive, and the layout self-heals.** The saved document is
an ordered list and positions are derived from it, so a role that loses four
domains loses four entries and everything after them moves up. First-fit closes
any gap a wide card would have left. The page gets *shorter*, never sparser —
which is what §16 asks for.

Permission reaches the header too: the quick-actions menu is filtered by the
same set, so a veterinarian who cannot see Finance widgets is not offered
"Create Request" either. One source, checked in both places.

**One saved layout per role**, keyed `antz.site.layout.<role>`. A manager who
arranges their workspace, looks at the veterinarian view, and comes back gets
their arrangement back — sharing one key would have meant destroying your own
work by looking at something. Not per *Site*, though: an arrangement is a
statement about how you work, not about one Site.

### Emptiness is a property of the Site, not of the widget

§15 asks for real empty states and forbids fake zero values. The temptation is
an `isEmpty` flag on a widget, which *is* the fake — the widget is not empty,
the **Site** has no data for it.

So there are four Sites, and **Hesaraghatta Field Station was commissioned three
weeks ago**. It has people and space and no asset register, no budget line, no
compliance history. Seven of a Manager's twenty-two widgets have nothing to draw
there and say so, in the product's own voice, with the action that would start
fixing it. The same Asset Health card is full at Bannerghatta.

An empty card gets a **neutral outlined surface**, not the domain gradient under
a veil. The veiled-gradient treatment was tried on this product once before, for
data cards, and reverted: on a desaturated fill it does not soften the colour,
it removes it. This sidesteps that entirely — an empty card is not a quiet
version of a full one, it is a different thing, and on a workspace where a third
of the cards have nothing to say the ones that *do* must still be the ones that
carry.

### Figures that are already in the Site record are derived, not re-typed

The Site header read "19 Staff" from the Site record while the People widget
read "86 Staff" from the catalogue, **on the same screen**. That is the worst
class of bug this page can have — not a crash, a page that looks completely fine
and is wrong.

So anything the Site record knows is computed from it once, in `derive()`, and
anything it does not know is authored per Site in `figures`. The split is not
stylistic: a count that appears twice must have one source, and a judgement —
*which two domains are dragging a Site down* — cannot be computed.

> **Superseded.** The paragraph below argued for a comparative health score.
> There is no health score any more — see *No Site Health*. What survives of the
> argument is that four Sites are what make any comparison possible at all; the
> Sites listing ranks them on open items instead.

The four Sites are also the reason a health score means anything. 87% is a
number; **87% next to 94% and 61% and 72%** is a decision about where to go this
week.

| Site | Health | Reads as |
|---|---|---|
| Bannerghatta Safari | 87% | working, with Safety and Maintenance behind |
| Bannerghatta Zoo Core | 94% | well run; only Maintenance behind |
| Hesaraghatta Field Station | 61% | **not failing — unfinished.** Four domains "Not Set Up" |
| Mysuru Rescue Centre | 72% | actually in trouble: 19 items open on half the staff |

Hesaraghatta's rows say *Not Set Up* rather than showing a bad score, because a
reader who cannot tell "failing" from "not started" will go and fix the wrong
thing.

### Colour is the domain, and the palette is still closed

On the home page, colour identifies a **module** and does not vary between that
module's cards. Here the same rule holds one level up: colour identifies the
**domain**, so a person scanning the workspace finds the finance card by its
green without reading it.

Eighteen domains onto **the same sixteen gradients**, all from the Figma file.
Four pairs deliberately share a fill, and each pair is two halves of one subject
rather than two unrelated domains that ran out of colours:

```
Safety & Compliance / Emergency Readiness   coral
Work & Activity     / Upcoming              petrol
Assets              / Vendors & Contractors neutral
Space & Capacity    / Site Insights         teal
```

The brief's own colour instructions are honoured where it gives them: People
blue, Finance green, Infrastructure neutral, Utilities cool, Safety warm, Animal
Operations a natural tone.

Domain glyphs are **sprite symbols**, not exported files — the artboard has no
Site Workspace to export from, so eighteen were drawn in the same idiom as the
two module icons the file was already missing. A sprite glyph inherits
`currentColor`, which is what lets the same mark sit white on a gradient card
and petrol in a gallery rail row.

### Why the switch sits under the search field

Three places were on the table and two of them break something.

- **A left rail** scales to a third and fourth workspace, and costs 72–88px of a
  960px content width permanently. That width is not a preference: 179.2px
  columns are (960 − 4×16) ÷ 5 *exactly*, and the whole artboard falls out of
  that arithmetic. A rail would have made every card the wrong size on the one
  page whose fidelity is measured in units.
- **Tabs on the greeting line** are free vertically, and that row already
  carries a two-line greeting plus three 44px controls. At 834px portrait it
  wraps, and what wraps is the switcher.
- **A segment between search and content** costs about 60px once, sits where the
  eye already travels on its way to the first card, and reads as what it is —
  two ways of looking at the same work.

Both panels stay in the DOM and are toggled with `hidden`, so the switch is
instant and each keeps its scroll position. `#site/<siteId>` is written to the
hash with `replaceState` so a workspace can be linked to without four presses of
Back to leave the page; a deliberate Site change *does* push, because that one
is a navigation.

The greeting steps aside in the Site view. "Good Morning, Sourav" and
"Bannerghatta Safari Site" are both answers to *where am I*, and a page that
gives two has given none.

### Bugs this build found in itself

Four, all caught by driving the page rather than reading it:

**Switching Site showed the previous Site's figures.** The grid reconciles by
uid and rebuilds a card only when its variantId or span changed — right for
every other update, exactly wrong for this one, because a Site switch changes
neither. It showed Bannerghatta's numbers under Hesaraghatta's name, which is
the worst failure this page could have because it is the one that looks like it
worked. Fixed with a teardown: a Site switch *is* a navigation, so there is no
continuity to preserve.

**Two galleries wrote the same element id.** `aria-labelledby="picker-title"`
resolves to the first match in the document, so the site widget sheet announced
itself as "Add Module" to anyone using a screen reader. Ids are now per
instance — the gallery's title and all four size selectors.

**A health card's rows went two-column on an iPad in portrait.** The threshold
was written as a `max-width`, and `large` is two columns on the reference grid
but *three* at the 768px band — so a card that had gone single-column at 1024
came back as two 164px columns, and "Maintenance / Attention" does not fit in
164. The threshold is now derived from the space the rows actually get.

**`chev-right` and `chev-left` were being called and had never been defined.**
The gallery's rail rows and its phone-width back button both rendered an empty
box. Pre-existing; found while wiring the switcher, which needs the same three.

### Verified

| | |
|---|---|
| Widget catalogue | **83 widgets, 18 domains, 204 widget × size combinations** · 1–9 per domain |
| Role defaults | `antz.checkSiteDefaults()` · all five roles: **0 unknown widgets, 0 unsupported sizes, 0 permission violations, 0 duplicates, 0 empty grid cells** |
| Every widget at every size | **207 combinations × 4 Sites × 9 widths = 7,452 renders** at 1920 / 1366 / 1194 / 1024 / 900 / 834 / 768 / 640 / 500px · `scrollHeight` vs `clientHeight` on every composition root, `scrollWidth` vs `clientWidth` on every label · **0 overflowing, 0 clipped, 0 horizontal scroll** |
| Roles | five defaults packed at 5 columns · **0 empty cells** in any of them · each opens on a different card |
| Permissions | eight role × denied-domain pairs on the grid · **0 leaks** · gallery rail filtered (a vet sees 11 domains, not 18) · quick-actions menu filtered per role |
| Empty states | Hesaraghatta: **7 of 22** widgets have no data and say so · **0 fake zeros** on any card · full data restored on switching back |
| Header ↔ widgets | staff, animals, enclosures, sections, health and attention cross-checked between the Site header and the widgets, **on all four Sites** · 0 disagreements · three consecutive Site switches do not compound |
| Drag | mouse drag reorders the workspace store, tears down clean, and persists to `localStorage` |
| Gallery | 18 domains in five groups · previews are real cards · search indexes what a widget *shows* ("generator" finds Utilities) · multi-select, per-card sizes, one-write batch add |
| Document | **0 duplicate element ids** with both galleries mounted |
| Regression | the module home page: **0 changes** to its 213 combinations at six widths, `antz.checkDefaults()` still clean, mouse and touch drag still pass |
| Errors | **none** — no console errors, page errors or failed requests |

```js
antz.site.view()          // { view, siteId, roleId }
antz.site.state()         // the live workspace layout
antz.site.go('site')      // switch workspace
antz.site.site('hg-field')// switch Site
antz.site.role('vet')     // switch role
antz.site.allWidgets()    // every widget at every size, on the workspace grid
antz.checkSiteDefaults()  // assert all five role defaults, and that they pack without gaps
```

### Not built, and deliberately

*(Section and Enclosure workspaces were deferred here and have since been built —
see the next section.)*

Out of scope: a cross-site comparison view (the Sites list carries health; the
analytics screen does not exist), real module destinations (widgets navigate;
destinations are announced, exactly as the home page's cards are), and any
backend — role and permission are a front-end simulation with a switcher, which
is why the role chip is drawn with a dashed outline.

---

## Down the hierarchy — Section and Enclosure

`Housing → Sites → Site → Section → Enclosure`. All three workspaces run on the
same components. The switcher stays two-way; depth lives inside the Site Command
Centre, with the breadcrumb as its spine.

### Why depth is not a third tab

A five-way switcher would have flattened a hierarchy into five peers and thrown
away the one thing the reader needs most — that *this* Section is inside *that*
Site. So `level` sits under the switch, the breadcrumb carries the ancestry, and
going deeper is what it looks like: going into something.

```
Housing / Sites / Bannerghatta Safari / Carnivore Safari / CAR-02
```

`#site/bg-safari`, `#section/car`, `#enclosure/car.2` — a workspace switch uses
`replaceState` because it is not a navigation; a move through the hierarchy uses
`pushState` because it is. <kbd>Esc</kbd> goes up a level.

### The rule the brief is firmest about

Section 12: keep the philosophy through the hierarchy, but *"do NOT copy the same
widgets everywhere — the widgets should become increasingly specific as the user
moves deeper."*

The failure mode is very easy to reach: ship the Site's 83 widgets again with a
`sectionId` filter, and every level looks identical while carrying smaller
numbers. Nobody can then tell which level they are on except by reading the
breadcrumb, and the hierarchy has bought nothing.

So the catalogues get **smaller and sharper** with depth, and the difference is
subject rather than scale:

| | a Site asks | a Section asks | an Enclosure asks |
|---|---|---|---|
| people | how many staff does this place have? | who is on the rota for this area right now? | who is the assigned keeper? |
| structure | what is the asset register worth? | which of my enclosures is not sound? | is this barrier sound? |
| conditions | what is the electricity bill? | is it too hot in the reptile house? | what is it under the shade net? |
| animals | 42 species, 318 animals | 5 species, 38 animals, 1 welfare alert | Anand and Bhima, and how they are |

| | Site | Section | Enclosure |
|---|---|---|---|
| Widgets | **84** | **41** | **38** |
| Widget × size | 207 | 97 | 90 |
| Domains | 18 | 15 | 11 |
| Manager default | 22 widgets | 20 | 16 |
| Gone from the level above | — | Finance, Vendors, Risk, Insights | + Safety, Inventory, Assets, Maintenance, Area Ops |
| New at this level | — | Area Operations, Environment & Conditions | Occupancy, Condition, Husbandry, Veterinary, Assessments |

**160 widgets over 25 domains**, and four whole domains are absent from the
Section level *by design*: a section does not have a budget, a contract, a risk
register or a quarterly insight. Five are new at the enclosure level and exist
nowhere else.

### Where the "no individual animals" rule inverts

The Site catalogue has a standing rule against naming an animal: a Site widget
that does is no longer a workspace card, it is a small copy of Species
Management. That rule is about **altitude**, not about animals — and at the
enclosure it inverts. §12 lists the enclosure's subjects as *"animal/occupancy,
enclosure condition, husbandry, veterinary, assessments"*: every one is about the
specific creatures in this specific space. A card here reporting "42 species at
this Site" would be the failure.

So `enc.occ.list` names individuals, and `enc.assess.welfare` is the **Five
Domains** model — Nutrition, Environment, Health, Behaviour, Mental State. That
is not five words picked to fill a card; it is the framework zoo welfare
assessment actually uses, and the one place in this build where the widget
followed the profession rather than the layout. It reuses the `health`
composition, because the shape is identical: one index, and the parts it is made
of.

### The summary and the detail agree

Three enclosures are authored explicitly, and they are the ones a Site-level card
already promised: **Welfare Alerts** names `CAR-02` and `HRB-03`, **Restricted
Areas** names `REP-04`. Drill into any of them and you find the condition the
summary told you about — `CAR-02` is the Bengal Tiger with the stereotypic
pacing, `REP-04` is closed for barrier repair. `antz.checkHierarchy()` asserts
the codes exist.

The other 136 are **generated** from their section's seeds, with every varying
number hashed from the enclosure's own code so it is stable across reloads and
identical on every machine. Authoring 139 records by hand would have produced 139
rows of plausible noise that drifts out of step with its section the first time a
count changes.

And the counts reconcile. Section records **sum exactly** to their Site's
`counts` — enclosures, staff, species, animals — on all four Sites, asserted in
both directions by `antz.checkHierarchy()`. It would be tidier to derive the Site
totals and delete the Site's own numbers; it would also be wrong, because a Site
has staff who belong to no section. Two numbers with a stated relationship and a
test is the honest shape.

### Still no forked components

| | |
|---|---|
| Grids | **1** |
| Edit modes | **1** |
| Drag controllers | **1** |
| Size popovers | **1** |
| Headers | **1** |
| Widget galleries | **1** |
| Catalogues | 3 |
| Stores | 3 (nine keys — three levels × role) |

What swaps when the level changes is three pieces of data — the catalogue, the
store, and the subject. Nothing else.

Three components were generalised rather than copied:

**The store became a factory.** `createWorkspaceStore({ level, keyPrefix,
version, getWidget })`, instantiated three times. The Site version was a
singleton; copying it twice would have produced three files that are 95%
identical and diverge on the first bug — and there *was* a bug in the original's
`repair()`, which would then have needed fixing three times.

**The Site header became a workspace header.** One `subject()` function is the
only level-aware code in the file; it returns the crumbs, the siblings and the
counts, and everything below it is written once. A Section header would otherwise
have been the third copy of a breadcrumb, a status pill, a sibling menu, a role
chip and a counts strip — and the fourth place to fix the next bug in any of
them.

**The gallery's search index became rebuildable.** One `revision` value, changed
when the level does. The alternative was four picker instances: four sheets in
the document, four sets of duplicate ids to keep unique, and four copies of a
basket that took three attempts to get right.

### Fifteen defaults, composed from blocks

Five roles × three levels. On the five-column grid there are exactly two
arrangements that fill two rows with nothing left over:

```js
pair(a, b, c, d)   // two 2×2 cards and two 1×1 cards → 4+4+1+1 = 10 cells
wide(a)            // one full-width card             → 5×2   = 10 cells
```

The Site defaults stay a flat list because they transcribe §20 literally and that
is worth being able to read. The ten deeper ones are composed from those two
helpers, because hand-counting cells ten times is how a hole gets into a shipped
default. `antz.checkSiteDefaults()` asserts the result either way.

Every level therefore needs at least one 1×1 widget per domain a role can see — a
pair leaves one column, and something has to go in it. That is why the deeper
catalogues carry a KPI per domain, not decoration.

Each role opens on a different card at every level:

| Role | Site | Section | Enclosure |
|---|---|---|---|
| Site Manager | Site Status | Section Status | Enclosure Status |
| Veterinarian | Veterinary Cases | Welfare Alerts | **Welfare · Five Domains** |
| Biologist | Species at Site | Species in Section | Welfare · Five Domains |
| Facility Manager | Critical Equipment | Enclosure Condition | Open Defects |
| Administrator | People | Shift Roster | Enclosure Health |

The Facility Manager's enclosure workspace is the **thinnest of the fifteen** —
13 widgets over 5 domains, with no Occupancy, Husbandry, Veterinary or
Assessment. At an enclosure a facility manager cares whether the box is sound,
not what is in it. §16 asks for a workspace that still looks intentional when
most of it is unavailable, and the page gets *shorter* rather than sparser: three
blocks and the structural checks at full width, zero empty cells.

### Emptiness travels down, because the reason for it does

Hesaraghatta Field Station was commissioned three weeks ago. Its Site workspace
has 7 empty widgets of 22; **Grassland Plot A** has 2 of 20; **HGA-01** has 3 of
16. A Site with no asset register has no enclosure-level maintenance history
either, and saying so at each depth is more honest than showing a zero once and
then inventing detail underneath it.

### Bugs this pass found in itself

**Two animals in one enclosure with the same name.** The generator indexed the
name table with a hash slice per position, and slices collide — HRB-03 came out
holding two animals called Shakti. It walks forward from a collision now, so the
result is still deterministic. Nobody would have crashed over it and every reader
who looked twice would have stopped believing the page.

**The clinical history named an animal that was not an occupant.** `enc.vet.history`
was authored copy (Bhima, Kaveri) while the occupant list is derived, so on most
enclosures the history named animals the Individuals card two rows away did not
contain. Both come from the same function now.

**REP-04's note contradicted its own occupant count** — "occupants moved to
REP-05" on a card reporting six occupants.

**Two status rows clipped at the 900px band**, which is the narrowest the
reference grid ever gets: five columns inside 836px, so a one-row status card's
two columns are 138px each. `"6 days"` became `"6 d"` and `"Pacing logged"`
became `"Pacing"`.

### Verified

| | |
|---|---|
| Catalogues | **160 widgets · 25 domains · 387 widget × size combinations** |
| Hierarchy | `antz.checkHierarchy()` · 4 sites, **31 sections, 139 enclosures** · section counts sum exactly to every Site record in both directions · all three enclosure codes a Site card names exist |
| Defaults | `antz.checkSiteDefaults()` · **15 role × level arrangements**: 0 unknown widgets, 0 unsupported sizes, 0 permission violations, 0 duplicates, **0 empty grid cells** |
| Every widget at every size | **394 combinations × 11 subjects × 9 widths ≈ 8,900 renders** at 1920 / 1366 / 1194 / 1024 / 900 / 834 / 768 / 640 / 500px · **0 overflowing, 0 clipped, 0 horizontal scroll** |
| Levels differ | 18 → 15 → 11 domains in the gallery; 22 → 20 → 16 widgets in the Manager default; each role opens on a different card at each level |
| Permissions at depth | a facility manager sees no Occupancy, Husbandry or Veterinary widget at an enclosure but does see Condition; a biologist sees no Veterinary widget; a vet sees both Veterinary and Assessments |
| Coherence | across six enclosures: the clinical history names **no animal that is not an occupant**; CAR-02 is the Bengal Tiger, HRB-03 the Gaur, REP-04 the closed tortoise vivarium — exactly as the Site cards said |
| Deep links | `#enclosure/hrb.3` opens with its whole ancestry and survives a reload; `#section/zaq` crosses to another Site; `#enclosure/nope.9` falls back to the Site level |
| Per-level persistence | removing a Section widget writes `antz.section.layout.manager` and leaves `antz.site.layout.manager` untouched; drag at the enclosure level writes `antz.enclosure.layout.manager` |
| Drag at depth | mouse drag reorders the enclosure workspace, persists, and tears down clean |
| Regression | the module home page and the Site level: **0 changes** · `tools/verify.py` fully green |
| Errors | **none** at any level, on any subject |

```js
antz.site.section('car')      // into a Section
antz.site.enclosure('car.2')  // into an Enclosure
antz.site.children()          // what is under the current subject
antz.site.up() / .down()      // move through the hierarchy
antz.checkHierarchy()         // the counts reconcile and the promises hold
antz.checkSiteDefaults()      // all fifteen role × level arrangements
```

---

## Housing — the way in, and the Sites listing

The Site Command Centre used to be reachable only from the segmented switch.
Nothing on the home page said the hierarchy existed, and nothing in the product
let you look at all four Sites at once — the Site switcher was a popover hanging
off the header's own title.

Both are fixed by the same thing: **Housing is a module now.**

```
Home page → Housing → Sites → Site → Sections → Enclosures
```

### One card, and the four that were built and taken out again

Housing is **one tile**. It appends as a sixth row under the artboard's five, so
node 55476:32828's twenty-five cells are still the first twenty-five cells of
the page.

It was four. A Sites status list, an attention list ranked by open items, the
door and a count — on the reasoning that every other module carries three to six
cards and a lone tile would be the thinnest thing on the page, and on the
arithmetic that `1 + 4 + 4 + 1 = 10` is the only shape that fills two rows of
five without a hole.

**That was the right argument on the wrong page.** The home page is a *module
chooser*. Everything those three extra cards said — which Sites exist, which one
is in trouble, how big the estate is — is said better one tap later by the Sites
listing, which is the entire point of the door. Three cards previewing a page
that is one tap away is not depth, it is the same page twice.

They are gone from the **catalogue**, not just from the seed: a card that should
not be on this page should not be addable to it either. `repair()` drops the
retired ids out of anyone's saved layout without a version bump, which is what
it is for.

**Its fill is shared with Hospital, deliberately.** The palette is sixteen closed
Figma gradients and all of them were spoken for. Hospital's own seeded card is
the ward *photograph*, so the deep slate is not actually drawn anywhere else on
the default page — and of the sixteen it is the one that reads as ground and
building rather than as a department. This is the first shared fill on the home
page; it is not a licence for a seventeenth gradient.

**And its glyph is a sprite, which found a two-session-old bug.** Housing is the
first *module* with a `sprite` instead of an exported `icon`, and `glyph()`
names the wrapper after whatever layout asked for it — so `l-compact__icon--sprite`
had no CSS, the `<svg>` resolved to the viewport rather than to 34px, and a
124px card came out 199px tall. Every previous sprite belonged to a Site domain,
and no domain offers a compact card. The compact door has since been dropped
with the rest, but the CSS gap it exposed is fixed for whatever carries a sprite
next.

### Three spacing defects in the chrome, all of them found by looking

None of the sweeps could have caught these: every one of them measures content
against its own container, and all three of these are the space *between* two
elements.

| | Was | Now |
|---|---|---|
| Hero → first card row | **0px** — the banner sat flush on the cards | `var(--grid-gap)`, the artboard's own 16 |
| Search field → switcher | **0px** — two controls touching | 20px |
| Switcher → hero | 52px, the largest gap on the page under its least important control | 32px, the artboard's page padding alone |
| Switcher width | **1024** where the search, hero and grid are all **960** | 960, sharing every edge |

The chrome band now steps **24 / 20 / 32 / 16** down into the page: the greeting
is a different kind of thing from the search; the switcher is the same kind of
thing, so it sits closer; 32 is the artboard's page padding before the hero; 16
is the grid gutter. The last two are not choices.

### The listing is a table, because the question is comparative

`level: 'sites'` is a fourth level, not a third tab — Housing → Sites → Site →
Section → Enclosure is one hierarchy and the breadcrumb is its spine. It is the
only level with **no subject**, so it has no catalogue, no saved arrangement and
no widgets; `syncWorkspace()` shows the listing and skips every branch that
touches a workspace.

Four Sites as four cards is four things read one at a time. The question here —
*which of these needs me this morning* — is comparative, and a comparison wants
its values in columns, so that 41 staff under 147 animals reads against 104
staff under 604 without the reader holding either in their head. That is a
table, and section 3 of the brief says so: use one when the information needs
multiple columns or comparisons.

It is not a `<table>`. Each row is a single tap target that has to reflow into a
stack on a narrow tablet, and a table cannot do either. It is a list of buttons
on a grid — same columns, tablet behaviour.

**Ranked by what is open, worst first.** Mysuru is at the top because nineteen
things are open on it against Bannerghatta's twelve, on half the staff. The Site
you last had open is *marked*, not sorted up: moving the row a reader is used to
seeing in third place breaks the one thing a ranked list promises.

**The surface is the opposite of a card.** Every widget in this product is a
saturated gradient you go *into*; the listing is a quiet sheet you read *across*.
Four gradient cards here would have made the page look like a workspace one level
too early, and made a Site's colour mean something — it does not, because a Site
is not a domain. The only colour on a row is four pixels of state at the leading
edge.

### What moved so the listing and the widget could agree

The per-Site attention rows used to live in the widget catalogue for one Site
and in `figures` for the other three. The listing needs the same rows, and that
is exactly the shape the staff-count bug had — one fact authored twice, correct
until somebody edits one copy.

So `openItems` is on the **Site record**, `derive()` hands it to the Needs
Attention widget, and the listing reads it directly. `attention` stays its own
field rather than being summed, because Hesaraghatta's three are three
commissioning *blockers* and two of them carry no number to add up.

---

## No Site Health

There was a Site Health card: a gauge reading 87% with the six domains it was
composed of listed beside it, at full width, first on the Manager's page. There
was a Section Health and an Enclosure Health under it. All three are gone, and
the reason is worth keeping because the card was genuinely well made.

**An index is not an observation.** 87% is not measured anywhere — it is a
weighting somebody chose over six things that are not commensurable, and the
weighting is invisible to everyone who reads the number. Two Sites at 87% are
not in comparable condition. One Site moving 87 → 84 tells nobody which of the
six moved, or whether it matters.

**It absorbed the page's attention for nothing.** It was the largest element on
the workspace and the only one that could not be acted on. Its six rows were
real — and they are, one for one, cards the workspace already carries: Critical
Equipment, Maintenance, Infrastructure, Utilities, Compliance, People. Those say
the same thing with the name of the failing pump in it.

**And it hid the difference between failing and unfinished.** Hesaraghatta scored
61%, which reads as a Site being run badly; it is three weeks old. What replaced
that number is seven widgets rendering a real empty state and an open list headed
*Commissioning* naming an asset register that has not been opened. That cannot be
misread.

The `health` **layout** stays. One card still earns a gauge: the enclosure's
**Five Domains** welfare assessment, which is a published framework with defined
criteria rather than an index this product invented for itself.

What replaced the three cards in the fifteen defaults is `overview.status` at
each level — Operations, Perimeter, Water Supply, Power; states somebody set
rather than a number nobody computed. Same size, same position, every word
checkable. The sibling menus stopped quoting a score too: a chooser should rank
on the thing the choice is about, which is what is open.

---

## The workspace the brief asked for

Three more corrections, all of them things the brief names by hand.

### One Maintenance card, and the split is inside it

Maintenance appeared **three times** on a Manager's page: a door tile, an open-jobs
list, and a `Maintenance Split` metrics card four rows further down carrying a
different decomposition of the same twelve jobs. Two cards headed *Maintenance*
with different numbers on them is a reconciliation the reader should never have
been handed.

The `attention` layout gained an optional **`split`** — three figures between the
hero and the named rows — which is exactly how section 10 draws the card:

```
MAINTENANCE
12  Open Jobs
2 Critical   4 Due Soon   6 Scheduled
· Water Pump #04                Critical
· Generator #02                Tomorrow
· Fence Line C                   3 days
· Chiller #01                    4 days
View Maintenance ›
```

`site.maint.split` is **deleted from the catalogue**, not merely dropped from the
defaults: a card that must not appear twice must not be available to add a second
time. Procurement took the same treatment — 14 requests partitioned six, four and
four, rather than the bare count section 17 calls out.

### Infrastructure is a quarter of the size

It was `full`: 960px wide, two rows tall, six one-line rows, and about a third of
it empty underneath them. It is `large` now — 2×2, six rows down one column,
sitting beside Utilities in the pair the brief draws. `full` is still *offered*,
because the default is the opinion and not the constraint.

A card's size is a claim about how much there is to read, and this one was
claiming three times what it had.

### Utilities is one card, not three

Electricity, Water and Power & Generation are three good cards, and a workspace
carrying all three has spent six grid cells saying *the utilities are fine*.
`site.util.overview` is the roll-up — grid, water, both generators, solar,
diesel reserve — and it is where Mysuru running on a DG at 31% diesel reads as
one fact instead of three. The individual cards stay in the gallery for the roles
that live in them.

### Every widget says where it goes

The brief draws `[View Maintenance]`, `[View Assets]`, `[View Inventory]` and
six more at the foot of the widgets it specifies. Two things come out of it:

**It answers "where does this take me" before the tap.** A card that is context,
summary and navigation has to say which of the eighteen modules it is a doorway
into, and the domain and the module are not always the same word — Inventory
opens Pharmacy, People opens Users.

**And it gives the list layouts a floor.** Five attention rows in a 2×2 card left
ninety pixels of nothing under them, which is the brief's complaint about large
unused spaces inside cards. A footer is not filler: it is the one element that
belongs at the bottom edge, and with it there the space above it reads as
structure rather than as a card that ran out of content.

Only where there is both a destination and room: home-page modules carry no
`module` field so nothing on the home page grows one; doors are already the door;
and at 2×1 there are 132px for everything. The **Overview** domain is exempt too —
its subject is the page you are already on, and "View Housing" at the foot of a
Site Status card is an invitation to go *up* from a card whose whole job is to
describe where you are.

**A floor costs one row, and the row is given up rather than cut.** Four list
layouts render everything they are given and let the card clip the overflow —
fine when the cut lands in dead space, awful when it lands halfway through
"Keeper training · Batch 4". Thirty-one pixels of footer is one entry, so one
entry goes, at breakpoints measured on the eight-width sweep rather than guessed.

The same pass found and fixed **91 pre-existing clipping defects** across the
three levels that the previous sweep had not been looking for: it only checked
content against the *card* floor, and these were rows cut by their own
`overflow: hidden` container.

### Verified

| | |
|---|---|
| Home page | `tools/verify.py` **fully green** — 215 combinations × 6 widths, drag through the browser's own input pipeline, no console errors |
| Catalogues | **18 home modules · 94 cards · 215 combinations**; **160 site widgets across 25 domains** (83 · 40 · 37) |
| Chrome alignment | search, switcher, hero and grid share both edges at 1440 / 1024 / 768 / 640 / 500 |
| Console assertions | `antz.checkDefaults()` · `antz.checkSiteDefaults()` · `antz.checkHierarchy()` — all three clean, including the **0 empty grid cells** check across all fifteen role × level defaults |
| Clipping sweep | every widget at every size × 4 Sites × 8 widths, and × 8 deeper subjects — **0 regressions**, 91 pre-existing defects fixed |
| The flow | Home → Housing card → `#sites` → a Site → a Section → an Enclosure, and back up through all four with the browser's own Back button |
| The listing | 1366 / 1180 / 1024 / 900 / 834 / 768 / 640 / 500 / 390px — no truncation, no horizontal scroll, reflows to a stack at 960 |
| Deep link | `#sites` opens the listing with the workspace unmounted; Escape from it lands on the home page, where the Housing crumb does |
| Menus at the new level | the listing is not offered Customize or Reset — both would silently edit the Site workspace underneath it |

### One thing in the brief that was not built

Section 37 recommends a practical cap of **8–12 pinned widgets**. It is not
implemented as a hard limit, and that is a decision rather than an oversight:
the five seeded role defaults run 21–29 widgets, of which roughly half are the
1×1 doors and KPIs the grid needs to pack its two-row blocks without a hole.
Capping at twelve would mean seeding fewer *substantive* widgets than section 31's
own suggested first viewport lists. The anti-clutter mechanism section 37 names —
a curated default, with everything else behind Add Widget — is already how the
product works: a Manager is seeded 29 of the 83 site widgets.

---

## The Site Workspace, made minimal

The workspace was a dashboard. It is a **Site home screen** now: twelve cards,
each one a whole clickable module, each one carrying a name, a number and one
line that says whether to go in.

| | Before | After |
|---|---|---|
| Site catalogue | 83 widgets, 204 combinations | **40 widgets, 79 combinations** |
| Manager's default | 29 widgets | **12** |
| Facility Manager | 28 | **12** |
| Veterinarian / Biologist | 21 / 21 | **10 / 10** |
| Card heights on a default | 132 / 296 / 296 px, mixed | **164 throughout** — one row of content, one row of card |
| CTA links on the page | 11 | **0** |
| Individual records on the page | asset names, job names, case names, event lines | **none** |

### The card is the control

`View Assets ›`, `View Maintenance ›` — eleven of them, one at the foot of every
large widget. They came out.

The card has been a `<button>` since the first line of `ModuleCard.js`. A link
at the bottom of a button is **a control inside a control**: it has its own hit
area competing with the surface around it, its own focus stop, and — read as a
set of eleven — it turns a workspace into a page of links. It also lies about
the size of the target, which on a tablet is the thing that matters most.

So the affordance is the surface, and it is three states and nothing drawn:

```
hover   translateY(-3px)
press   scale(.978)
focus   2px ring, 3px offset
```

The press is a little heavier here than on the home page, because on a
workspace where every card is a destination it is the only thing that says the
tap landed — there is no label to grey out and no ripple.

### One line, and it is the line worth acting on

Every metric card is `name → figure → label → one clause`:

```
ASSETS              MAINTENANCE          UTILITIES
248                 12                   Normal
Assets              Open Jobs            All Services
5 need attention    2 overdue            Electricity · Water · Generator
```

**The clause is one clause, and that is measured rather than stylistic.** A 1×1
card has 147px of content box — about twenty-four characters at the micro size —
so `231 operational · 5 need attention` wrapped onto two lines and then ran out
of card. It is also the wrong half of the sentence: nobody opens Assets because
231 of them are fine. Where there is genuinely nothing wrong the clause turns
over to the reassuring one — Zoo Core's Assets card reads `All operational`, and
its Maintenance card reads `None overdue`.

### What came off the page, and where it went

| Removed | Why | Where it lives now |
|---|---|---|
| **Needs Attention** (5 rows) | §8 — one card aggregating five domains is the dashboard pattern the brief is trying to get away from | as a clause on each of the five cards |
| **Critical Equipment** (5 named assets) | §7 — individual records | the Assets module; the count survives as `5 need attention` |
| **Emergency Readiness 74%** gauge | §9 — a health score wearing a different name | `3 / 5 systems ready`, which is the same fact and you can go and fix the fifth |
| Site Activity, Upcoming (timelines) | §7 — event records | counts: `18 events today`, `9 scheduled` |
| Licences, Inspections, Renewals, Deliveries, Quarantine, Top Risks, Contacts | records, all of them | their modules |
| Electricity, Water, Waste, Availability, Generator | §14 — five cards to say the utilities are fine | one Utilities card |
| Site Insights ("Since Last Period") | §25 — the most analytics-shaped thing on the page | — |
| Every `.door` tile | the metric card **is** the door now, and carries a number as well | — |

### Two things arrived

**Veterinary is a Site-level domain.** It used to be a card inside Animal
Operations, which made a veterinarian's first-class subject somebody else's
subheading. Welfare moved out to Assessments for the same reason. Animal
Operations is two numbers now — `42 Species / 318 animals` — which is what §17
asks for and all it should ever have been.

**Projects exists.** Two briefs have asked for it and both times it fell off the
end. `d.projects` is the 26th domain, sharing Work & Activity's fill because
they are a real sibling pair: a task is a thing being done today, a project is a
thing being done over a quarter.

### The narrow card moves every row

Twelve cards packed `2-2-1` four times is a grid with a column of small cards
down the right-hand side — the "boring equal grid" §11 asks not to build. The
same twelve reordered so the small one lands in a different column each row read
as a composed page:

```
2 2 1      Assets          Maintenance     Tasks
1 2 2      Safety          Infrastructure  Utilities
2 1 2      People          Sections        Projects
1 2 2      Enclosures      Inventory       Vehicles
```

First-fit does the rest — the packer takes the list in order, so **the order is
the layout**, and the composition costs nothing but the order of an array.

### Sections and Enclosures go down, not out

§16 makes them first-class, and they are the only two cards on the page that
navigate **into** the hierarchy rather than off to a module. Enclosures goes two
levels, because enclosures live under a Section and stopping at the Section on
the way past is not what "show me the enclosures" means.

### One thing that was asked for and not done

**§13's subtler gradients.** The fills are unchanged. The calming came from the
cards getting smaller and fewer — the coloured area on a Manager's page is about
a third of what it was — rather than from desaturating anything.

Desaturation was tried on this product once, on the home page, and reverted:
under a white veil the already-quiet fills (Follow Up's petrol, Approvals'
slate) do not soften, they **turn grey**, and colour identifying its subject is
a rule this product has defended twice. Re-running that experiment on a surface
whose whole premise is that colour identifies the domain seemed the wrong call
to make unasked. It is a small change if it is wanted — one tonal scale in
`cards.css` — and it belongs in the Figma file rather than in a CSS override.

### The brief's own checklist, run against the build

Every line below is asserted by a script, not by eye.

| | |
|---|---|
| No Site Health, no health score | ✓ — the `health` layout survives for exactly one card, the enclosure's Five Domains welfare assessment |
| No giant Needs Attention card | ✓ |
| No duplicate Maintenance | ✓ — `Maintenance` appears once in the page's whole text |
| No "View →" anywhere | ✓ — the string `View` does not appear in `#siteGrid` |
| Entire card clickable, nothing nested | ✓ — every card is a `<button>`; no `<button>` or `<a>` inside one |
| No individual records | ✓ — no asset, job or case name in the page text |
| No huge empty cards | ✓ — every default card is 164px, one row of content in one row of card |
| Sections and Enclosures first-class | ✓ — and they are the two that drill down |
| Role defaults | 12 / 12 / 10 / 10 / 12, all packing with **0 empty cells** |
| Permissions | a Facility Manager is offered 15 domains, a Biologist 8 — built from what the role can open, not thinned from the Manager's |
| Customize | edit mode, the gallery, resize and reset all still work on the new catalogue |
| Clipping | every widget × every size × 4 Sites × 8 widths: **0 clipped, 0 overflowing** |
| Deeper levels | Section and Enclosure: **0 regressions** against the pre-session baseline |
| Home page | `tools/verify.py` fully green |

---

## Opening a widget — the record underneath

A widget on the Site page is a name, a number and one line. **Tapping it opens
the record it was summarised from** — the whole of what the operation keeps for
that dimension of this Site, Section or enclosure, in the groups the discipline
keeps it in.

Twelve cards on a Manager's page, and behind them **2,124 fields across 52
records** — every domain the workspace can show, resolved at three depths.

### Keyed on the domain, not on the widget

117 widgets across three levels would have meant 117 detail documents, most of
them the same document with a different tile on top, and the second one written
would already have drifted from the first.

The rule the workspace already uses settles it: **the destination is a property
of the domain, not of the card.** Every Maintenance widget opens Maintenance, so
every Maintenance widget opens the same record. What is per-widget is the part
that should be: the card names itself in the header — *From Open Jobs · 39
fields in 6 groups* — and the sheet **opens scrolled to that card's own group**
rather than at the top of a six-hundred-row document.

An eighty-fifth widget tomorrow is wired by existing.

### Three compositions, and no more

| | For | Example |
|---|---|---|
| **facts** | a label and a figure — most of the record | `Staff-to-animal ratio · 1 : 3.7` |
| **table** | rows that share a shape | work orders, contracts, occupants |
| **items** | what is open, dotted | `Overdue maintenance · 4` |

A record of six hundred fields invents a fourth treatment every time somebody
adds a group unless the file says no.

### Figures that are also on a card are read from the card

The sheet opens **on top of** the widget, and the two are on screen together for
the length of the transition. A sheet computing its own *12 open jobs* over a
card reading *9* is the bug this build has already found once — the same fact
authored twice, correct until one of them is edited.

So `maintOpen`, `assets`, `vetCases`, `tasks`, `overdue`, `approvals` and
`incidents` are read out of the live catalogue, which `applySite()` has already
rewritten for the current subject. Everything else is derived from the subject
record or authored once — and neither can disagree with a card, because no card
holds it.

### It goes down without being copied down

§12 of the brief: copying the same content down the hierarchy is the failure, and
Overview is where it is easiest to reach. A Command Centre Summary is a **Site's**
morning brief; the same sixteen rows under an enclosure would read *Total
species: 1 · Enclosures occupied: 1 of 1*, which is a template running rather
than a record being kept.

So groups declare the depths they belong to, and the deeper levels get their own:

| Level | Overview record is |
|---|---|
| Site | Command Centre Summary · Critical Alerts · Executive Action Dashboard · Daily Operations |
| Section | This Section, Today · Open in This Section · Daily Operations |
| Enclosure | This Enclosure, Now · Needs Attention Here · Care Due Here |

The title follows too — *Site Overview*, *Section Overview*, *Enclosure
Overview* — because Overview is the one domain whose subject is the page itself.
Every other domain is called the same thing at every depth, because it **is** the
same thing.

### And no composite scores

The source list asks for an *overall facility health score*, a *site-wise
operational score* and an *animal health score by site or enclosure*. **None of
the three is here**, for the reason Site Health was deleted from this product:
an index over incommensurable things is not an observation, and it hides the
difference between failing and unfinished. Each is replaced by the counts it
would have been computed from.

What is kept is a score a profession publishes and audits against — body
condition, the **Five Domains** welfare model, an enclosure audit result, a
hygiene audit. Those are measurements, not indices this product invented.

### A sheet, not a fifth level

Going down the hierarchy means going somewhere **smaller**. Opening Maintenance
at the Site does not move you to a smaller place; it stays on the same subject
and shows more of it. So the two gestures stay distinct and both stay available:

| Gesture | Widgets | What happens |
|---|---|---|
| drill in | Sections, Enclosures, Section Contents | the level changes — breadcrumb, catalogue, workspace |
| open | every other widget | the record, over the page you are on |

The card itself is untouched: **no `View X ›` floor came back**. The one action
in the sheet's footer is the domain's module, and a footer button in a modal is
the sheet's primary action rather than a control inside a control.

### Verified

| | |
|---|---|
| Every domain at every level | **52 records, 2,124 fields**, all resolving — `antz.checkDetail()` |
| Ragged data | a table row of 2 cells against 3 columns, and 210 rows with a tone string sitting in the sub column — both **found by the check, both fixed** |
| Every widget on the page | all 12 open a record with groups in it |
| Clipping | 6 widths × the sheet: **0 overflowing**, tables scroll inside their own wrapper |
| Empty subjects | Hesaraghatta's Assets record shows the domain's own empty state, **not eighty rows of em dashes** |
| Escape | closes the sheet **only** — it does not also go up a level |
| Leaving the subject | switching Site, level, view or role closes the record with it |
| Home page | `tools/verify.py` fully green — 215 cards × 6 widths, drag, console |

---

## The thirty-four ANTZ modules, and the menu that offers them

`docs/Modules.md Files/` is the real thing: **39 dashboards, 299 widget
definitions**, generated from the live ANTZ v5 config with real routes, real
`dataKey`s, and — the part that mattered most — a **Roles** section on every
page naming the seats that treat it as a priority. Nothing built before this
pass had been checked against it.

So there is a menu icon in the Site header now, and it answers one question:
**more modules, based on the role.**

### Two lists, because a priority is a suggestion and a permission is the rule

```
FOR THE VETERINARIAN            8 modules
  Alerts & Key Indicators       Site Overview · 6 widgets
  Species SOPs & Guidelines     Documents · 4 widgets
  Pharmacy                      Inventory & Stock · 8 widgets
  Medical & Veterinary Care     Veterinary · 12 widgets        ✓
  Animal Welfare & Behaviour    Assessments · 7 widgets        ✓
  …
ALSO AVAILABLE TO YOU          13 modules
  …
```

**`mine`** is the modules whose *"Priority module for"* line names one of the
seats this workspace role covers. **`rest`** is everything else the role is
permitted to open. A module the role cannot see is in **neither** — the
difference between *not for you* and *not yours*, and the same subtractive rule
the widget gallery's rail already follows.

The counts move with the role and are worth reading as a design output rather
than a statistic: the Site Manager sees 6 + 28, the Veterinarian 8 + 13, the
Biologist 9 + 6, the Facility Manager 10 + 12, the Administrator 7 + 7. A
Biologist is offered fifteen modules and a Site Manager thirty-four, because
that is what their permissions come to.

### The row is a switch, not a link

Tapping puts the module's card on the workspace. Tapping a ticked row takes it
off. **The menu stays open** — `keepOpen` in PopMenu — because putting three
modules on a page should be three taps and not three round trips, and it
re-renders in place so the ticks are live while you work.

That matters more than it sounds. A menu of thirty-four one-way adds is a menu
you stop trusting after the first mistake, and **the way back has to be the
gesture that got you there.** A tick removed from the grid instead of from the
row unticks the row too, because the grid tells the header to refresh.

### One component, not a second one

Everything above is `createPopMenu` — the same 130 lines that already draw the
sibling chooser, the role switcher, the quick actions and More. Four things were
added to it and every one of them is general:

| | |
|---|---|
| `{ heading, note }` | a section label — no glyph column, no hover, no cursor |
| `on` | checkbox semantics, against `checked`'s radio semantics |
| `variant` | one extra class, for a menu that needs its own measurements |
| `keepOpen` | re-render in place and return focus to the row that was tapped |

A second menu component was the obvious shortcut and would have been the
expensive one: the four things a menu has to get right — the transparent
catcher, the viewport clamp, the roving focus, the return of focus — are four
decisions, and a copy would have made them eight.

The one measurement it does not take from CSS is its height. Thirty-four rows is
taller than a phone, and a fixed `max-height` is either short on a desktop or
off the bottom edge on a tablet, so `place()` caps it at **the space actually
left below the button** and the list scrolls inside that.

### Spacing and type, stated once

A long list is exactly where a component starts inventing its own scale — a
13px heading here, an 11px badge there — and thirty-four rows is enough
repetition for a half-step to read as a mistake rather than an accident. So the
contract is written out at the top of the stylesheet and **every value is a
token**:

| | |
|---|---|
| row height | 44px minimum — the brief's touch floor, and why the rows are `--s2` block padding on a 34px glyph rather than something tighter that would have fitted more in |
| row rhythm | `--s3` glyph → text, `--s2` text → tick |
| inset | `--s3` inline, inherited from the compact menu |
| heading | `--fs-micro`, 650, tracked +.05em, `--petrol-600`; its count in `--ink-3`; `--s4` above and `--s1` below, because **a heading belongs to what follows it** and equal space either side is the commonest way that stops being legible |
| label | `--fs-label` at 600 — the same as every other menu row in the product, because it is the same kind of thing |
| note | `--fs-micro` in `--ink-3`, one line, ellipsed |

Two measured exceptions, both documented in place. **44px** is the touch floor.
**356px** is the width, against the compact menu's 304: measured on the longest
label in the catalogue — *Safety, Security & Emergency* — with the tick present,
which is the widest a row ever gets. At 304 that name and *Medical & Veterinary
Care* both ellipsed, and **a module row that will not say which module it is has
lost the only thing it was for.**

### The widget count was a badge, and the badge was wrong

It sat right-aligned, and it cost the thing beside it. Two elements competing for
the same edge meant `margin-left: auto` fought itself, so the ticked rows
measured 24px narrower than the rest — and *Medical & Veterinary Care*,
*Animal Population Planning* and *Safety, Security & Emergency* all ellipsed,
**only when ticked.** A patch was written for it before the right answer showed
up: the count is a hint about what is behind a row, the name is the reason to
tap it, so the count moved onto the note line and the name got the width.
`badge` came back out of PopMenu with it.

## The module cards

Thirty-four modules, thirty-four Site widgets — `mod.alerts` through
`mod.executive`, section T of `js/data/siteWidgets.js`. They are in the gallery
like everything else; the menu is a shortcut to them, not a second catalogue.

### Every one carries a fact no other card on the page carries

This was most of the work. The obvious build is *put each module's headline KPI
on a card*, and it produces a workspace that contradicts itself:

| Module's headline | Already on the workspace |
|---|---|
| Maintenance — **486** open work orders | `site.maint.open` — **12** open jobs |
| Assets — **5,720** assets | `site.assets.total` — **248** assets |
| Housing — **1,840** enclosures | `site.space.count` — **48** enclosures |
| Animal Collection — **1,04,382** animals | `site.animal.summary` — **318** animals |

**Nine of the thirty-four collided that way**, and a reader who sees both learns
not to trust either. So where a module's headline is already on the workspace,
the card takes that module's **second** fact — the one that dashboard knows and
the Site summary does not:

- **Maintenance** stops counting jobs and reports the **hours** they cost — the
  figure that argues for the budget.
- **Assets** stops counting assets and reports the ones whose **service contract
  has lapsed** — the figure that turns into a breakdown.
- **Housing** stops counting enclosures and reports how many pass
  **biosecurity**.
- **Animal Collection** stops counting animals and reports where the ones **not
  in their own enclosure** actually are — quarantine, isolation, hospital.
- **Finance** leaves the budget to `site.finance.budget` and reports **cost per
  animal per day**, the one finance figure that compares one Site to another.
- **Compliance** leaves the obligation count alone and reports whether the people
  here have **acknowledged the SOPs** those obligations rest on.
- **Risk** counts what is **being done** about the register rather than what is
  in it, and the gap between the two is the only part anybody can act on.

Each is a genuine reason to open that module, which is the test §11 sets for a
workspace card.

### Authored once, at the reference Site, then scaled

The documents are facility-wide — 1,04,382 animals, 5,720 assets, 3,012 staff
across eight sites — and the two datasets do not divide cleanly. The documents'
facility runs **57 animals per enclosure** where Bannerghatta runs **6.6**, so
scaling every figure by its own denominator gives some cards a plausible number
and others a nonsense one.

So each card is authored **once, for Bannerghatta** — the Site this whole
catalogue was authored against — proportioned from the document's own figure,
with a `doc` field recording the line it came from so any value can be traced
back. Every other Site scales from it by **one ratio**: this Site's count against
Bannerghatta's, on the base the card names.

```js
{ key: 'medical', layout: 'stat', base: 'animals',
  title: 'Medical', n: 4, label: 'Under Treatment',
  sub: 3, clause: 'under observation', tone: 'warn',
  none: 'None in observation',
  doc: 'medical.md — 1,186 under treatment, 913 under observation' }
```

Bannerghatta's own ratio is 1, so **the authored value is what it shows** —
the only arrangement where the authoring and the arithmetic cannot quietly
disagree. `fixed: true` marks the figures that are rates, unit costs or
durations and do not scale at all: ₹96 per animal per day, 11 days of feed
cover, 23 days to close an incident, a 20-medicine emergency formulary.

**One function produces the data and it is called twice** — once at load with a
ratio of 1, which is how the catalogue entry gets its figures, and again from
`derive()` with the live Site's ratio. Two functions, one to author and one to
scale, is how the reference Site ends up showing something the authoring did not
say.

### One override, and it is the rule the file opens with

Animal Population's holding figure is the Site's **own animal count** — the
header shows it, `site.animal.summary` shows it, and a third card scaling the
document's 1,500 to something *near* it would be the staff-count bug again. So
the count comes off the record and **the document's ratio decides the capacity**:
1,500 held against 3,854 approved is 38.9%, so a Site holding 318 animals at the
same density is approved for **817**.

### Absence is inferred, not listed

Hesaraghatta has no asset register, so it has no lapsed service contracts
either. Writing thirty-four more ids onto the Site record would have meant two
lists that have to agree and will not, so the summary cards are the source: **if
every one of a domain's own cards is absent at this Site, the module card that
shares the domain has nothing to draw either.**

`absent` still wins where it names a module card outright, because the inference
cannot see everything — Utilities keeps its *Conditions* card at a Site whose
meters are not connected, so the domain is not empty even though Energy and
Water have nothing to report. Four ids, and the comment says why each is there.

Nineteen per-widget empty states were written so no two cards in a domain say the
same sentence. *"No electricity meter is connected, so there is no consumption to
cost."* *"Staff here are still on the parent Site's payroll."* *"No incidents
have been logged here, so there is no closure time to average."*

### Four defects this pass found in itself

**A count that scales to one has to take the singular.** Scaling turned *6
critical breakdowns* into *"1 critical breakdowns"* and *9 Open Alerts* into
*"1 Open Alerts"* at the two smallest Sites. `label1` and `clause1` are
**declared rather than derived** by stripping an "s", because the catalogue is
full of words that do not work that way — Species, Papers, Staff — and a plural
rule that is right nine times in ten is a rule that ships a typo.

**And the reassuring clause has to be about the same thing the count was.** Six
were written as a reassurance about the *card* instead, which put

```
1                     4
Paper Expiring        Vacant Positions
All current           Fully staffed
```

on the page — a headline figure flatly contradicted by the line under it. `none`
replaces the **clause**, not the card, so the Transport card's clause counts
certificates that have already lapsed and its `none` is *"None expired"*, and the
papers still expiring stay expiring.

**A queue's total has to be the sum of its rows.** Scaling the total separately
from the rows let the header round to three while the four rows rounded to two —
a card whose parts do not add up to its own total, which is the exact failure the
note on `site.people.mix` describes. The total is computed from the rows now.

**And the queue's absolute figures were too small to survive rounding.** 78
purchase orders across 1,840 enclosures scales to two at Bannerghatta, and a
four-row queue reading 1 / 1 / 0 / 0 is a card with nothing to say. The **shape**
is the document's — 28% waiting on a signature, 28% approved, 15% out, 24% in —
at a volume a Site of 248 assets actually runs. An order is not a request, which
is what keeps this card and `site.finance.procurement` two facts rather than one
restated.

### Thirty-four titles, and five of them were too long

At the 900px band a 1×1 card's title line gets **92px**, about twelve characters.
*Species Master* measured 101 and ellipsed, and so did four others. They are
*Taxonomy*, *Assessments*, *Unit Cost*, *Closures* and *Mitigation* now, and the
sweep is clean at all six widths.

## The twelve roles

`js/data/roles.js` has carried a standing note since it was written: **its five
roles are inferred**, because the real ANTZ taxonomy lived in a system this
prototype could not read. It can read it now. Every module document names the
roles that treat it as a priority, and across the thirty-four files exactly
twelve names appear:

> Management · Veterinarian · Paravet · Biologist · Nutritionist · Pharmacist ·
> Keeper / Animal Care · Maintenance / Engineering · Security · HR / People ·
> Admin / Finance · Procurement

**The five workspace roles are not replaced by them, and that is deliberate
rather than lazy.** A workspace role is a set of permissions and a default
arrangement — fifteen hand-balanced layouts hang off those five ids, and swapping
in twelve is a different piece of work with a different risk. What the twelve
give us is the thing this file needs and `roles.js` cannot supply: **which
modules a person in that seat actually opens.**

So the two are bridged by one map, and **the bridge is the only new thing that
can be wrong**:

```
manager    → Management
vet        → Veterinarian · Paravet
biologist  → Biologist · Nutritionist · Keeper / Animal Care
facility   → Maintenance / Engineering · Security
admin      → Admin / Finance · HR / People · Procurement · Pharmacist
```

Every one of the twelve is covered **exactly once**, so no module can fall out of
every role's list and none can appear in two. `antz.checkModules()` asserts it.

## Site Widgets opens on the important ones

Each role's default gained **one row of five cells** — the module cards that
role is actually asked about:

| Role | The module row |
|---|---|
| Site Manager | **Medical** · **Animal Population** · Alerts |
| Veterinarian | Medical · Assessments · Welfare Risk |
| Biologist | **Animal Population** · Breeding · Taxonomy |
| Facility Manager | IoT Devices · Energy Cost · Transport |
| Administrator | Leave · Overtime · Manpower |

The cell arithmetic is exact, which is the point: on the five-column reference
grid a `medium` is 2 cells and a `small` is 1, so **2 + 2 + 1 fills one row with
nothing left over.** `antz.checkSiteDefaults()` packs all fifteen role × level
seeds and counts the cells no card claimed — it is zero, which is the check that
stops a default from shipping a hole.

Two of the Site Manager's three are not Management-priority modules in the
documents, and that is not an inconsistency. **The default is the Site's
business; the menu is the module catalogue's opinion.** What a Site Manager is
*asked about* on a Monday morning is what is being treated and whether the
collection is inside its approved capacity, and both are one tap away for
everybody else.

## The header gave its controls back

The Site header carried five controls — a role chip, **Add**, **Customize**,
**More**, and the modules menu — and four of them were a second route to
something the avatar menu already offered.

```
before   [☰] [Viewing as  Site Manager ▾] [＋ Add] [⚙ Customize] [⋯]
after    [☰]
```

What is left is the one control that is about the **product** rather than the
page: the modules this role can put on it. Everything a person can do to their
own workspace hangs off their own avatar — which is not a new rule, it is the
rule the home page has followed since the profile menu was written, and the Site
header had quietly been the exception.

### What moved, and why each one belongs there

| | |
|---|---|
| **Viewing as** | Which seat you are looking through is a statement about **you**, not about the Site. In the header it was a dashed chip that had to explain it was scaffolding; in the account menu it needs no explaining, because that is where a person expects to find who they are signed in as. It is the only radio group in the menu — one role at a time, ticked. |
| **Customize / Reset** | Already there. The Customize button and the More menu were both second doors to items the avatar had carried for two sessions. |
| **On this Site** | The quick actions. These are the one genuine argument *against* the move — "Add Task" is a thing you do to the Site, not to your account — and they moved anyway, under a heading that names the subject, because the alternative was deleting eight permission-gated actions to save a button. Gated exactly as before: the role's permissions and the level. |
| **Open Report** | The only item the More menu had that was nowhere else. |

The rest of the More menu — *Open a Section*, *All Sites*, *Go Up* — is not
reproduced anywhere, and that is deliberate. Every one of them was a third route
to a move the breadcrumb, the sibling caret, the counts strip and <kbd>Esc</kbd>
already make: a menu item that says *"Go one level deeper"* next to a
breadcrumb is a menu item nobody reads twice.

The menu is ordinary on the home page — three items, as it always was — and long
on the Site. **That asymmetry is the point rather than a cost:** the home page
has one thing to arrange, and a Site has a role, a workspace and a subject.

### The row is defined once now, for both menus

There are two menu components and there is a good reason for both: `ProfileMenu`
renders a fixed head with the user's avatar and name because it is the account
menu, and `PopMenu` has no opinion about content because it hangs off several
controls. What they must **not** have two of is the **row** — the glyph plate,
the label and note, the tick, checkbox-against-radio semantics, the heading, the
rule.

That went out of step immediately. The role switcher moved into the profile menu
and **arrived without a tick**, because `ProfileMenu` had never needed one and
its renderer knew nothing about `checked`. So `menuEntry(item, state)` is
exported from `PopMenu.js` and both callers attach their own listener. What stays
in each component is what genuinely differs: the head, the anchoring, the
dismissal, and whether choosing something closes it.

`ProfileMenu`'s `items` is a **function of the state** now, too. It was a fixed
array of three whose *labels* were functions — enough while the only thing that
varied was wording, and not enough once the number of rows depends on the level
and the role's permissions. **A label function cannot make a row that is not
there.**

### And a duplicated requirement failed the way duplicated requirements do

The modules menu capped its own height against the space under its anchor. The
profile menu did not, because it had never needed to. Move eighteen rows into it
and it came out **1,097px tall in a 1,000px window**, with its last two rows
below the bottom edge and no way to reach them.

`capToViewport(menu, top, margin)` is shared for the same reason the row is: it
is not a difference between the two menus, it is the same requirement. A fixed
`max-height` in CSS cannot do the job — too short on a desktop, past the edge on
a tablet — and `.pmenu` carries `overflow-y: auto` so that what does not fit
scrolls instead of vanishing.

### A second check that agreed with itself

The truncation probe measured `.pmenu__label` and `.pmenu__note` and **not
`.pmenu__heading-note`** — so it reported zero while *"Site Manager · Command
Ce…"* sat ellipsed at the top of the menu. The note is gone (the ticked row
directly below it answers the same question, which is what makes a heading note
redundant rather than short), and the probe measures headings now.

Two sessions running, the defect and the blind spot have been the same shape:
**a check that reads what the code intended rather than what the page renders.**

## The bug that shipped, and the check that agreed with itself

The first deploy went out with the modules button **visible on the Sites listing
and at both deeper levels**, where it is meant to be gone.

`render()` sets `modBtn.hidden = sub.level !== 'site'`, which is correct and did
nothing. `[hidden]` is a bare attribute selector in the UA stylesheet at
specificity **0,1,0**, and `.btn-icon { display: grid }` is **0,1,0 on a class**
— which wins. So the property was set, the element left the accessibility tree,
and the button stayed on the screen.

The `.site-head--listing [data-add]` / `[data-customize]` rules at the foot of
site.css are the same problem, solved one selector at a time by whoever hit it
first. There is a general form now:

```css
.btn-icon[hidden], .btn-solid[hidden], .btn-line[hidden] { display: none; }
```

**The check that missed it is the more useful lesson.** The test read `el.hidden`
— the property, which was correctly `true` at all three levels — and reported
PASS. A property is what you asked for; a box is what the user gets. The check
reads `getComputedStyle().display` and `getBoundingClientRect()` now, and it
catches the original bug when the CSS rule is removed.

## Two bugs found on the way past

**The gallery's rail listed eight domains that opened onto an empty pane.** The
comment on `visibleDomains()` has said since the gallery was written that a
domain is in the rail *only if it has widgets at this level* — and the code never
checked. At the Site level `domains` is every domain in the catalogue, including
the ones whose widgets only exist a level down, so Responsibility, Area
Operations, Occupancy, Enclosure Condition and four others were rail rows that
opened onto nothing. Asking the catalogue is one call and it is the only honest
source. The manager's rail is **21 rows, none of them empty**, and Husbandry and
Site Insights are in it for the first time because the module cards populate
them.

**Escape did two things.** With a header menu open it both closed the menu *and*
climbed a level — one keystroke, two actions, and the second was the one nobody
asked for. The header exposes `menuOpen` now, because it is the only place that
holds all five menus.

## Verified — the sixth pass

```
antz.checkDefaults()      []   the catalogue and the default home page agree
antz.checkSiteDefaults()  []   15 role × level workspaces, no gaps
antz.checkModules()       []   34 modules, 12 roles, a card for every one
antz.checkDetail()        []   52 records, 2,124 fields, three levels
antz.checkHierarchy()     []   the counts add up

tools/verify.py           ALL PASS   215 cards × 6 widths, drag, console
tools/verify_detail.py    ALL PASS   records, navigation, empty states
```

`antz.checkModules()` is new and asserts the five ways the module catalogue and
the widget catalogue can drift apart quietly: a module naming a widget that does
not exist, a card sitting in a different domain from the one the module claims, a
card that does not point back at its module, a role name that is not one of the
twelve, and — **the one that matters most** — a module in the menu that no seat
can open, which is a row the product will never show anybody and is invisible
until somebody counts.

Beyond the suites: the 34 module cards were swept at every size they declare
across six widths for overflow and truncation (**0 problems**), the menu was
opened at 1024 / 900 / 768 / 640 / 420 / 375 and checked for a row under the
44px floor, a truncated label and a box outside the viewport (**none at any
width**), and every module card's resolved data was read at all four Sites to
confirm the figures move, the plurals agree and the empty states land.

## Interaction reference

| | |
|---|---|
| Enter edit mode | **avatar → Edit Modules**, or long-press / right-click a card, or <kbd>E</kbd> |
| Reorder, mouse | press and move 4px |
| Reorder, touch | hold 200ms, then drag |
| Reorder, keyboard | focus a card · <kbd>Space</kbd> · arrows · <kbd>Space</kbd> — <kbd>Esc</kbd> cancels |
| Remove | the **−** at a card's top-left · core cards show a lock |
| Resize | the **⤢** at a card's bottom-right |
| Add | **avatar → Add Module**, or **＋ Add Module** in the edit-mode header |
| Add a whole module | **☰ in the Site header** — the modules your role answers for, ticked where they are already on the workspace. Tap to add, tap a ticked row to remove; the dialog stays open |
| Change role | **avatar → Viewing as** — five seats, one ticked. It was a chip in the Site header |
| Site actions | **avatar → On this Site** — Add Task, Report Incident and the rest, gated by role and level |
| Open a widget's record | **tap the widget** — Sections, Enclosures and Section Contents drill down instead |
| Move around a record | the chips under its title, or scroll |
| Close a record | **Close**, the **×**, the scrim, <kbd>Esc</kbd>, or drag the header down |
| Reset | **avatar → Reset Home Page** |
| Save | **Done** |

Species Management and Medical are non-removable. Everything else is the
user's call.

### The modules menu is a dialog, and now looks like one

Thirty-four rows in two groups, deciding what the whole workspace contains —
hung off its button in the header it ran the full height of the screen and past
the left edge of it. One flag on the shared `createPopMenu`, `centred: true`,
and nothing was forked:

| | Popover | Centred |
|---|---|---|
| Position | measured from the anchor in JS | stated in CSS, `translate: -50% -50%` |
| Width | 356px, measured against the longest label | **460px** — no name ellipses |
| Height | capped by the space under the button | `min(76dvh, 720px)`, scrolls inside |
| Behind it | the page, sharp | **the page, blurred** — one veil that is also the catcher |
| Page scroll | follows the anchor | locked |
| Chrome | none — it belongs to its button | a **sticky title and a ×**, because centred over a veil nothing says what this is or how to leave |

**Each row carries the widget count and nothing else.** It used to read *Site
Overview · 6 widgets* — a domain name repeated on every row of a group whose
heading already says what these modules are, with the one useful number pushed
to the far side of a separator.

The other four menus in the header — siblings, roles, add, more — are four rows
each and stay popovers, because a popover belongs to the control it came from
and the page behind it is still the page you are working on.

### Where the switch lands

The **Site Command Centre** tab opens the **Sites listing** — every Site, ranked
by what is open, with the one you last had open marked. That is the question a
reader arrives with (*which Site needs me this morning*), and it is the top of
the hierarchy the whole workspace is built on: Housing → Sites → Site → Section
→ Enclosure. Landing straight in a single Site answers a question nobody has
asked yet and hides the other three.

`setView()` resolves the level on the way in, so the destination does not depend
on whichever level happened to be persisted. Two consequences worth stating:

- **Tapping the tab while it is already selected does the same thing.** The
  listing lives *inside* the Site view, so working in a Site leaves the tab lit;
  pressing it there means "back out to the Sites", the way an already-selected
  tab returns to the root of its section everywhere else. It used to be a **dead
  button** — `view === view` swallowed the tap entirely.
- **The reason is `'sites'`, not `'view'`**, whenever the level moves, so app.js
  treats it as a subject change: an open record sheet closes and the previous
  level's grid is dropped on the way out.

`siteId` is never touched by the switch, which is what lets the listing mark
*Last opened* and makes going back one tap.

In the **Site Command Centre** the same gestures apply, with the workspace's own
nouns — and nothing is locked, because which widget is indispensable is exactly
what differs between a veterinarian and a facility manager:

| | |
|---|---|
| Switch workspace | the segment under the search field, or <kbd>←</kbd>/<kbd>→</kbd> on it |
| Switch Site | the caret beside the Site name, or **Sites** in the breadcrumb |
| Switch role | **Viewing as** in the header — a prototype affordance, hence the dashed outline |
| Customize | **Customize** in the header, or **⋯ → Customize Workspace**, or long-press / right-click a widget, or <kbd>E</kbd> |
| Add | **＋ Add Widget** in the customize header, or **avatar → Add Widget** |
| Quick actions | **＋ Add** in the header — filtered by the same permissions as the widget library |
| Reset | **⋯ → Reset Workspace**, or **avatar → Reset Workspace** — per role |
| Drill down | any count in the header strip, and any widget |

<kbd>E</kbd> toggles the edit mode **of the workspace you are looking at**: it is
bound once at the document and resolved at press time, because binding two
listeners and letting each decide whether to act is how a key ends up doing two
things.

```js
antz.state()           // the live layout
antz.columns()         // the current column count
antz.reset()           // back to the default home page
antz.allVariants()     // every card at every size it declares, on the grid
antz.checkDefaults()   // assert the catalogue and the default page agree
```

> **⚠ Testing trap — under `--virtual-time-budget` the grid appears to leak
> card nodes.** Replace the whole set of cards at once in headless Chrome and
> the DOM keeps the previous set as well:
>
> ```
> load                 DOM  15    store  15
> antz.reset()         DOM  30    store  15   ← 15 stale nodes
> antz.allVariants()   DOM 180    store 150
> ```
>
> **This is not a product bug.** `dismiss()` in ModuleGrid.js removes a slot
> when the Web Animations `finished` promise settles, and under virtual time
> that promise never settles — so the removal never runs. Add
> `--force-prefers-reduced-motion` and the count is correct at every step,
> because `animate()` then returns an already-resolved promise. It does not
> reproduce in a real browser.
>
> It matters because it silently corrupts measurement: a sweep over
> `antz.allVariants()` walks 165 nodes of which 15 are stale copies sitting at
> their *old* coordinates, so anything read from a node's position — a contrast
> sample, a screenshot comparison — reads the wrong ground for those fifteen.
> Either pass `--force-prefers-reduced-motion`, or filter on `dataset.uid`
> starting `x`.
>
> The catalogue is **74 variations over 150 variant × size combinations**; the
> "165 cards" in an earlier note was the inflated DOM count, not the real one.

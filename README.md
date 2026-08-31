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
| Card order | 5 rows, 15 cards | **5 rows, 15 cards, same footprints** |
| Page height | 1695px | **1695px** |
| Main Frame (node `55476:32852`) | 1024 × 1136 | **1024 × 1136** |
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

### Seventeen modules, seventy-one cards, and no two modules alike

The failure mode this is built to avoid is giving all seventeen modules the same
five generic cards: it produces a gallery where every module looks identical and
none of the cards is worth adding. So each module exposes only the card shapes
its actual work has —

| | |
|---|---|
| Security | a resting-state card (*All Systems Normal*), an alert count, an access log — and no progress bar |
| Diet & Kitchen | a progress bar, a pending count, a daily total — and no alert card |
| Fetal Death | three cards, which is the honest total for a module with six records a month |
| Parivesh | six, because a submission workflow has states worth separating |

Every module has one plain **Default** door. That is the floor, and the only
thing all seventeen share.

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

**Fill is part of the composition, not decoration.** `solid` is the module's
gradient with white text — cards you go *through*. `soft` is the same gradient
under an 84% white veil with dark text — cards you *read*. One module therefore
has bold tiles and quiet data surfaces in the same hue, which is where most of
the visible variety comes from. The veil is a white layer composited over the
gradient rather than a second palette, so all seventeen modules get a correct
pale surface in their own hue from one rule and a new module needs no new
colour.

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

Every text run **on the previous, fifteen-card page** was screenshotted with the
glyphs made transparent, the true painted ground sampled underneath, and the
ratio computed.

> **23 of 30 text runs fell below WCAG AA on the Figma palette.**

**That audit has not been re-run against the new catalogue and the number should
not be quoted as if it had.** What can be said without re-measuring:

- The finding is *structural*, not incidental — it is white text on the light end
  of a gradient — so it applies to every new card on those same fills, and the
  seventy-one-card catalogue has many more text runs than thirty.
- Three fills got **better**: Species, Diet & Kitchen and Hospital were
  translucent and are now opaque (see *Three defects the gallery exposed*), which
  raises white-on-fill contrast on every card that uses them.
- **No new fills were introduced.** Approvals wears Administer's gradient and
  Communication wears Users', so both inherit whatever those two measured.
- The new secondary type — metric labels, notes, link rows — is *smaller* than
  the labels that were measured, so it sits below the same threshold on the same
  grounds.
- The header planting **was** measured, before and after. It does not move the
  greeting on average — 2.65:1 → 2.65:1 — and costs 0.14 on the worst pixel
  (2.62 → 2.48). See *The header planting* above for the method and for what it
  cost before the thinning layer was added.

A fresh audit is a screenshot-and-sample pass over `antz.allVariants()` and is
worth running before this ships to anyone.

From that audit: white labels on the light end of the module gradients measured
1.79:1 (Lab), 1.82:1 (Eggs), 2.27:1 (Mortality), 2.49:1 (Fetal Death), 2.83:1
(Medical) — all on fills that are unchanged.
Text over the pale top of the Follow Up photograph runs 1.01:1 to 4.43:1. The
Species figure captions are 3.05:1. The greeting, at Figma's own `#00ABAB` on
the mint canvas, is 2.53:1 against a 3.0:1 requirement for text that size.

**None of this was changed.** The instruction was to build the Figma exactly,
and silently re-colouring a designer's palette is not implementing it. The
numbers are here so the decision is yours.

The fix, when you want it, is small and does not alter the design's character:
darken the light end of each gradient until white clears 4.5:1, and extend the
Follow Up card's scrim upward behind its list. That was done in an earlier pass
and took every run to AA while remaining visually near-identical.

The **Edit** control is the exception — it is not in the artboard, so its cyan
was darkened from `#00AFD6` (2.40:1) to `#007A95` (4.61:1). It is only visible
in edit mode.

---

## Verified

| | |
|---|---|
| Layout vs artboard | 5 rows, 15 cards, same footprints in the same order; page height unchanged |
| Catalogue | **17 modules, 71 cards** · 3–6 per module, no two modules alike |
| Catalogue ↔ default page | `antz.checkDefaults()` · **0 disagreements**, both directions |
| Every variant at every size | **71 cards, every declared size, at 1920 / 1440 / 1024 / 900 / 834 / 768 / 640 / 500px** · measured, not eyeballed: `scrollHeight` vs `clientHeight` on every block stack and `scrollWidth` vs `clientWidth` on every label · **0 overflowing, 0 clipped** |
| Responsive | 390 / 834 / 1024 / 1194 / 1440 / 1728px · **0 overlaps, 0 horizontal scroll** |
| Content cap | 1024 / 1280 / 1440 / 1920 / 2560px · page **1024px** and banner **960px** at every one · 5 columns, type frozen at the Figma values, **0 elements outside the page box** |
| Packer | 2 / 4 / 5 columns · **0 cell overlaps, 0 spans exceeding the grid** |
| Drag | mouse, touch long-press and keyboard · live reflow, correct commit, clean teardown |
| Gallery | 17 modules in the rail, always · module → widget → size → add, end to end |
| Rail anchored | **768 / 834 / 1024 / 1440px** · both panes live, back button hidden, rail still visible after choosing a module · add flow end-to-end at 768 and 834 |
| Palette | **16 gradients, all from the Figma file** · 0 invented |
| Header planting | 1440 / 834 / 500px · masked fade, no hard edge, no gradient block · **0 horizontal scroll** |
| Planting vs readability | greeting measured before/after · mean **2.65:1 → 2.65:1** and 10.16 → 10.15; worst pixel 2.62 → 2.48 and 10.04 → 8.91 |
| Planting stacking | hero banner paints **over** the 440px band at 1440 / 834 / 500 · hit-tested, not eyeballed |
| Search | names, keywords, purposes **and card content** — "low stock", "overdue", "population", "hatching", "all systems", "communication" |
| Persistence | `localStorage` **v2** with versioning and repair · survives reload |
| Edit entry | profile menu, plus 8 gesture cases: long-press (mouse + touch), right-click, <kbd>E</kbd>, and the four that must NOT trigger — short click, press-and-scroll, typing in search, resting state |
| Banner link | `<a href target="_blank" rel="noopener">` to the Command Centre · clicked: this tab stays put, so the new tab is doing the work · name reads "Antz Command Centre (opens in a new tab)" · no underline, no link colour, box unchanged at 1920 / 1024 / 500 |
| Card links | Species Management is an `<a target="_blank" rel="noopener">`, every other card still a `<button>`, every picker preview still an inert `<div>` (0 hrefs, 0 focusable) · click at rest does not navigate this tab; click in edit mode is prevented; keyboard reorder of the linked card still commits |
| Errors | **none** — no console errors, page errors or failed requests |

Two high-severity defects found by an adversarial review of the previous pass
are fixed and regression-tested: a drag returned to its own slot left the grid
pinned to a stale card list, and a prototype key such as `toString` in a saved
layout took the whole page down at module-evaluation time.

---

## Interaction reference

| | |
|---|---|
| Enter edit mode | **avatar → Edit Modules**, or long-press / right-click a card, or <kbd>E</kbd> |
| Reorder, mouse | press and move 4px |
| Reorder, touch | hold 200ms, then drag |
| Reorder, keyboard | focus a card · <kbd>Space</kbd> · arrows · <kbd>Space</kbd> — <kbd>Esc</kbd> cancels |
| Remove | the **−** at a card's top-left · core cards show a lock |
| Resize | the **⤢** at a card's bottom-right |
| Add | **avatar → Add Widget**, or the **Add Widget** tile at the end of the grid |
| Reset | **avatar → Reset Home Page** |
| Save | **Done** |

Species Management and Medical are non-removable. Everything else is the
user's call.

```js
antz.state()           // the live layout
antz.columns()         // the current column count
antz.reset()           // back to the default home page
antz.allVariants()     // every card at every size it declares, on the grid
antz.checkDefaults()   // assert the catalogue and the default page agree
```

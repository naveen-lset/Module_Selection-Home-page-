# Riverside Rescue Centre

| | |
|---|---|
| Key | `site@SITE-0001` |
| Route | `/housing/site/SITE-0001` |
| Kind | Housing level — site |
| Icon | `Building2` |
| Accent | `#2563EB` |
| Widgets | 10 in catalog, 6 shown by default |
| Widget types | kpi ×2, gauge ×2, alertFeed ×1, chart ×3, list ×1, table ×1 |

> This dashboard is generated per site by a factory in `src/config/housingPages.ts`, so one exists for every site in the facility. The figures below are for **Riverside Rescue Centre** (`SITE-0001`); every `dataKey` is scoped with an `@` suffix and resolved by `resolveEntityData`.

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Animals at this site | kpi | sm | `site@SITE-0001.animals` |
| 2 | Staff on roll | kpi | sm | `site@SITE-0001.staff` |
| 3 | Site occupancy | gauge | md | `site@SITE-0001.occupancy` |
| 4 | Operational score | gauge | md | `site@SITE-0001.score` |
| 5 | Site alerts | alertFeed | lg | `site@SITE-0001.alerts` |
| 6 | Sections at this site | table | lg | `site@SITE-0001.sections` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Animals at this site | kpi | sm | `site@SITE-0001.animals` | yes |
| Staff on roll | kpi | sm | `site@SITE-0001.staff` | yes |
| Site occupancy | gauge | md | `site@SITE-0001.occupancy` | yes |
| Operational score | gauge | md | `site@SITE-0001.score` | yes |
| Site alerts | alertFeed | lg | `site@SITE-0001.alerts` | yes |
| Enclosure status | chart | md | `site@SITE-0001.enclosureStatus` | — |
| Welfare by section | chart | md | `site@SITE-0001.welfareBySection` | — |
| Animal health mix | chart | md | `site@SITE-0001.healthMix` | — |
| Open maintenance | list | md | `site@SITE-0001.maintenance` | — |
| Sections at this site | table | lg | `site@SITE-0001.sections` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Animals at this site

`site@SITE-0001.animals` · type `kpi` · size `sm` · id `animals`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 197 | Animals at this site | 6 sections | flat | neutral |

### Staff on roll

`site@SITE-0001.staff` · type `kpi` · size `sm` · id `staff`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 238 | Staff on roll | 311 ha | flat | neutral |

### Site occupancy

`site@SITE-0001.occupancy` · type `gauge` · size `md` · id `occupancy`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 197 | 486 | 41% | Site occupancy | — | bad |

### Operational score

`site@SITE-0001.score` · type `gauge` · size `md` · id `score`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 85 | 100 | 85% | Operational score | % | good |

### Site alerts

`site@SITE-0001.alerts` · type `alertFeed` · size `lg` · id `alerts`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| medium | IoT | Temperature sensor 27 offline | 4 h |

### Enclosure status

`site@SITE-0001.enclosureStatus` · type `chart` · size `md` · id `enclosureStatus`

**donut chart** · 4 series · total 25

| Series | Value | Share |
|---|---|---|
| Occupied | 17 | 68% |
| Quarantine | 4 | 16% |
| Under maintenance | 2 | 8% |
| Vacant | 2 | 8% |

### Welfare by section

`site@SITE-0001.welfareBySection` · type `chart` · size `md` · id `welfareBySection`

**bar chart** · unit: % · 6 series · total 486

| Series | Value | Share |
|---|---|---|
| Large | 75 | 15% |
| Small | 76 | 16% |
| Primates | 76 | 16% |
| Herbivores | 98 | 20% |
| Elephant | 70 | 14% |
| Aviary | 91 | 19% |

### Animal health mix

`site@SITE-0001.healthMix` · type `chart` · size `md` · id `healthMix`

**donut chart** · 4 series · total 106

| Series | Value | Share |
|---|---|---|
| Healthy | 69 | 65% |
| Quarantine | 20 | 19% |
| Under treatment | 10 | 9% |
| Under observation | 7 | 7% |

### Open maintenance

`site@SITE-0001.maintenance` · type `list` · size `md` · id `maintenance`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Mesh damage | Plumbing · due 22 Jun 2026 · Kavya Chauhan | Low | bad |
| Water pump failure | HVAC · due 11 Jul 2026 · Rohit Iyer | High | bad |
| Gate latch repair | Civil · due 21 Jun 2026 · Vikas Singh | Low | bad |
| HVAC not cooling | HVAC · due 07 Oct 2026 · Aarav Pillai | Low | warn |
| Gate latch repair | Mechanical · due 21 Aug 2026 · Rohit Chauhan | High | bad |
| HVAC not cooling | HVAC · due 04 Aug 2026 · Meghna Menon | Low | bad |
| Pathway resurfacing | Filtration · due 13 Aug 2026 · Priya Gupta | Medium | bad |
| Drain blockage | Electrical · due 28 Jun 2026 · Sneha Iyer | High | bad |

### Sections at this site

`site@SITE-0001.sections` · type `table` · size `lg` · id `sections`

_shown by default._

| Section | Theme | Enclosures | Animals | Capacity | Welfare |
|---|---|---|---|---|---|
| Large Carnivores Section | Large Carnivores | 5 | 36 | 86 | 75% |
| Small Carnivores Section | Small Carnivores | 4 | 15 | 52 | 76% |
| Primates Section | Primates | 4 | 32 | 89 | 76% |
| Herbivores Section | Herbivores | 3 | 31 | 63 | 98% |
| Elephant Care Section | Elephant Care | 5 | 59 | 149 | 70% |
| Aviary Complex Section | Aviary Complex | 4 | 24 | 47 | 91% |

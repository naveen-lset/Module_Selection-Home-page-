# Projects & Infrastructure

| | |
|---|---|
| Key | `projects` |
| Route | `/topic/projects` |
| Kind | Topic dashboard |
| Icon | `HardHat` |
| Accent | `#B45309` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | chart ×3, alertFeed ×1, list ×1, timeline ×1 |

## Roles

**Priority module for:** Maintenance / Engineering.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Project progress | chart | lg | `projects.progress` |
| 2 | Budget vs spend | chart | lg | `projects.budgetVsSpend` |
| 3 | Delays & dependencies | alertFeed | lg | `projects.delays` |
| 4 | Upcoming milestones | timeline | lg | `projects.milestones` |
| 5 | Open snags | list | md | `projects.snags` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Project progress | chart | lg | `projects.progress` | yes |
| Budget vs spend | chart | lg | `projects.budgetVsSpend` | yes |
| Stage mix | chart | md | `projects.stageMix` | — |
| Delays & dependencies | alertFeed | lg | `projects.delays` | yes |
| Open snags | list | md | `projects.snags` | yes |
| Upcoming milestones | timeline | lg | `projects.milestones` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Project progress

`projects.progress` · type `chart` · size `lg` · id `progress`

_shown by default._

**bar chart** · unit: % · 8 series · total 419

| Series | Value | Share |
|---|---|---|
| New carnivore | 24 | 6% |
| Hospital wing | 66 | 16% |
| Quarantine unit | 50 | 12% |
| Aviary netting | 15 | 4% |
| Solar rooftop | 39 | 9% |
| Water treatment | 95 | 23% |
| Feed kitchen | 38 | 9% |
| Visitor pathway | 92 | 22% |

### Budget vs spend

`projects.budgetVsSpend` · type `chart` · size `lg` · id `budgetVsSpend`

_shown by default._

**bar chart** · unit: ₹ lakh · 12 series · total 22,668

| Series | Value | Share |
|---|---|---|
| New plan | 2,860 | 13% |
| New actual | 1,802 | 8% |
| Hospital plan | 478 | 2% |
| Hospital actual | 100 | 0% |
| Quarantine plan | 1,886 | 8% |
| Quarantine actual | 1,565 | 7% |
| Aviary plan | 3,205 | 14% |
| Aviary actual | 2,308 | 10% |
| Solar plan | 303 | 1% |
| Solar actual | 297 | 1% |
| Water plan | 3,799 | 17% |
| Water actual | 4,065 | 18% |

### Stage mix

`projects.stageMix` · type `chart` · size `md` · id `stageMix`

**donut chart** · 5 series · total 18

| Series | Value | Share |
|---|---|---|
| Finishing | 6 | 33% |
| Design | 4 | 22% |
| Construction | 3 | 17% |
| Handover | 3 | 17% |
| Commissioning | 2 | 11% |

### Delays & dependencies

`projects.delays` · type `alertFeed` · size `lg` · id `delays`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Projects | New carnivore enclosure block (Phase 1) — 16% behind plan (PowerGrid Services) | 3 d |
| high | Projects | Hospital wing expansion (Phase 1) — 12% behind plan (FeedLine Traders) | 3 d |
| high | Projects | Quarantine unit upgrade (Phase 1) — 19% behind plan (FeedLine Traders) | 3 d |
| high | Projects | Aviary netting replacement (Phase 1) — 15% behind plan (AquaTech Systems) | 3 d |
| high | Projects | Solar rooftop phase II (Phase 1) — 11% behind plan (MedEquip India) | 3 d |
| high | Projects | Feed kitchen modernisation (Phase 1) — 13% behind plan (PowerGrid Services) | 3 d |

### Open snags

`projects.snags` · type `list` · size `md` · id `snags`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Feed kitchen modernisation (Phase 1) — 26 open snags | Finishing · target 11 Sept 2026 | — | bad |
| New carnivore enclosure block (Phase 1) — 25 open snags | Finishing · target 17 Nov 2026 | — | bad |
| New carnivore enclosure block (Phase 2) — 23 open snags | Handover · target 19 May 2027 | — | bad |
| Hospital wing expansion (Phase 2) — 23 open snags | Design · target 14 Sept 2027 | — | bad |
| Water treatment plant (Phase 2) — 20 open snags | Commissioning · target 26 Jan 2027 | — | bad |
| Hospital wing expansion (Phase 1) — 19 open snags | Design · target 07 Dec 2026 | — | bad |
| Solar rooftop phase II (Phase 1) — 17 open snags | Construction · target 06 Sept 2026 | — | bad |

### Upcoming milestones

`projects.milestones` · type `timeline` · size `lg` · id `milestones`

_shown by default._

| Date | Event | Detail |
|---|---|---|
| 04 Sept 2026 | Quarantine unit upgrade (Phase 2) | Finishing · 8% complete · PowerGrid Services |
| 06 Sept 2026 | Solar rooftop phase II (Phase 1) | Construction · 39% complete · MedEquip India |
| 06 Sept 2026 | Aviary netting replacement (Phase 2) | Finishing · 86% complete · GreenBuild Infra |
| 11 Sept 2026 | Feed kitchen modernisation (Phase 1) | Finishing · 38% complete · PowerGrid Services |
| 13 Sept 2026 | Aviary netting replacement (Phase 1) | Commissioning · 15% complete · AquaTech Systems |
| 25 Oct 2026 | Visitor pathway redevelopment (Phase 1) | Design · 92% complete · SafeGuard Solutions |

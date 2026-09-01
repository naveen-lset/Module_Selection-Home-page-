# Large Carnivores Section

| | |
|---|---|
| Key | `section@SEC-0001` |
| Route | `/housing/site/SITE-0001/section/SEC-0001` |
| Kind | Housing level — section |
| Icon | `Building2` |
| Accent | `#0891B2` |
| Widgets | 9 in catalog, 5 shown by default |
| Widget types | kpi ×2, gauge ×2, chart ×2, list ×1, table ×2 |

> This dashboard is generated per section by a factory in `src/config/housingPages.ts`, so one exists for every section in the facility. The figures below are for **Large Carnivores Section** (`SEC-0001`); every `dataKey` is scoped with an `@` suffix and resolved by `resolveEntityData`.

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Animals in section | kpi | sm | `section@SEC-0001.animals` |
| 2 | Keepers assigned | kpi | sm | `section@SEC-0001.keepers` |
| 3 | Section occupancy | gauge | md | `section@SEC-0001.occupancy` |
| 4 | Section welfare score | gauge | md | `section@SEC-0001.welfare` |
| 5 | Enclosures in section | table | lg | `section@SEC-0001.enclosures` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Animals in section | kpi | sm | `section@SEC-0001.animals` | yes |
| Keepers assigned | kpi | sm | `section@SEC-0001.keepers` | yes |
| Section occupancy | gauge | md | `section@SEC-0001.occupancy` | yes |
| Section welfare score | gauge | md | `section@SEC-0001.welfare` | yes |
| Enclosure status | chart | md | `section@SEC-0001.statusMix` | — |
| Species held | chart | md | `section@SEC-0001.speciesMix` | — |
| Open maintenance | list | md | `section@SEC-0001.maintenance` | — |
| Enclosures in section | table | lg | `section@SEC-0001.enclosures` | yes |
| Environment & biosecurity | table | lg | `section@SEC-0001.environment` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Animals in section

`section@SEC-0001.animals` · type `kpi` · size `sm` · id `animals`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 36 | Animals in section | 5 enclosures | flat | neutral |

### Keepers assigned

`section@SEC-0001.keepers` · type `kpi` · size `sm` · id `keepers`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 33 | Keepers assigned | — | — | neutral |

### Section occupancy

`section@SEC-0001.occupancy` · type `gauge` · size `md` · id `occupancy`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 36 | 86 | 42% | Section occupancy | — | bad |

### Section welfare score

`section@SEC-0001.welfare` · type `gauge` · size `md` · id `welfare`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 75 | 100 | 75% | Section welfare score | % | warn |

### Enclosure status

`section@SEC-0001.statusMix` · type `chart` · size `md` · id `statusMix`

**donut chart** · 2 series · total 5

| Series | Value | Share |
|---|---|---|
| Occupied | 3 | 60% |
| Quarantine | 2 | 40% |

### Species held

`section@SEC-0001.speciesMix` · type `chart` · size `md` · id `speciesMix`

**bar chart** · 8 series · total 22

| Series | Value | Share |
|---|---|---|
| Fishing Cat | 4 | 18% |
| Dhole | 3 | 14% |
| Clouded Leopard | 3 | 14% |
| Striped Hyena | 3 | 14% |
| Asiatic Lion | 3 | 14% |
| Lion-tailed Macaque | 2 | 9% |
| Indian Leopard | 2 | 9% |
| Indian Rhinoceros | 2 | 9% |

### Open maintenance

`section@SEC-0001.maintenance` · type `list` · size `md` · id `maintenance`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Mesh damage | Plumbing · due 22 Jun 2026 | Low | bad |
| Gate latch repair | HVAC · due 27 Aug 2026 | Medium | bad |
| Pathway resurfacing | Civil · due 06 Sept 2026 | Low | warn |

### Enclosures in section

`section@SEC-0001.enclosures` · type `table` · size `lg` · id `enclosures`

_shown by default._

| Enclosure | Type | Status | Occupancy | Hygiene | Next inspection |
|---|---|---|---|---|---|
| LAR-001 | Aviary | Occupied | 12/39 | 67% | 17 Sept 2026 |
| LAR-002 | Aquatic | Occupied | 3/17 | 78% | 05 Nov 2026 |
| LAR-003 | Outdoor | Occupied | 3/8 | 77% | 18 Sept 2026 |
| LAR-004 | Outdoor | Quarantine | 2/6 | 91% | 19 Aug 2026 |
| LAR-005 | Aviary | Quarantine | 16/16 | 93% | 10 Sept 2026 |

### Environment & biosecurity

`section@SEC-0001.environment` · type `table` · size `lg` · id `environment`

| Enclosure | Temp °C | Humidity % | Water quality | Biosecurity |
|---|---|---|---|---|
| LAR-001 | 28.7 | 76 | N/A | Non-compliant |
| LAR-002 | 19.6 | 54 | Good | Compliant |
| LAR-003 | 31 | 58 | N/A | Compliant |
| LAR-004 | 16.2 | 49 | N/A | Compliant |
| LAR-005 | 32.4 | 92 | N/A | Compliant |

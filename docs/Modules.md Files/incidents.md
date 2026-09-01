# Incident Management

| | |
|---|---|
| Key | `incidents` |
| Route | `/topic/incidents` |
| Kind | Topic dashboard |
| Icon | `AlertTriangle` |
| Accent | `#B45309` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | kpi ×1, list ×1, chart ×3, table ×1 |

## Roles

**Priority module for:** Security.

**Role-specific default layouts:** Security. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Average closure time | kpi | sm | `incidents.closureTime` |
| 2 | Open incidents | list | md | `incidents.openList` |
| 3 | Incidents by kind | chart | md | `incidents.byKind` |
| 4 | Repeat incident trend | chart | md | `incidents.repeatTrend` |
| 5 | Incident register | table | lg | `incidents.table` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Average closure time | kpi | sm | `incidents.closureTime` | yes |
| Open incidents | list | md | `incidents.openList` | yes |
| Incidents by kind | chart | md | `incidents.byKind` | yes |
| Root cause mix | chart | md | `incidents.rootCauseMix` | — |
| Repeat incident trend | chart | md | `incidents.repeatTrend` | yes |
| Incident register | table | lg | `incidents.table` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Average closure time

`incidents.closureTime` · type `kpi` · size `sm` · id `closureTime`

_shown by default · default for Security._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 23 days | Average closure time | — | down | good |

### Open incidents

`incidents.openList` · type `list` · size `md` · id `openList`

_shown by default · default for Security._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Medication error — Island | 24 Jun 2026 · SOP retraining scheduled | Open | bad |
| Medication error — Coastal | 01 Jul 2026 · Equipment replaced | Open | bad |
| Zoonotic exposure — Wetland | 11 Aug 2026 · Vendor notice issued | Open | bad |
| Equipment failure — Highland | 11 Jun 2026 · Equipment replaced | Open | bad |
| Medication error — Highland | 28 Jun 2026 · Inspection frequency increased | Open | bad |
| Bite / scratch — Central | 03 Jul 2026 · Equipment replaced | Open | warn |
| Biosecurity breach — Wetland | 23 Jun 2026 · Vendor notice issued | Open | warn |
| Feeding error — Highland | 03 May 2026 · Equipment replaced | Open | warn |

### Incidents by kind

`incidents.byKind` · type `chart` · size `md` · id `byKind`

_shown by default · default for Security._

**bar chart** · 10 series · total 52

| Series | Value | Share |
|---|---|---|
| Equipment failure | 7 | 13% |
| Animal escape | 7 | 13% |
| Zoonotic exposure | 6 | 12% |
| Animal injury | 6 | 12% |
| Near miss | 6 | 12% |
| Medication error | 5 | 10% |
| Biosecurity breach | 5 | 10% |
| Feeding error | 5 | 10% |
| Bite / scratch | 3 | 6% |
| Staff injury | 2 | 4% |

### Root cause mix

`incidents.rootCauseMix` · type `chart` · size `md` · id `rootCauseMix`

**donut chart** · 7 series · total 52

| Series | Value | Share |
|---|---|---|
| Design inadequacy | 11 | 21% |
| Under investigation | 9 | 17% |
| Procedure not followed | 8 | 15% |
| Third-party lapse | 7 | 13% |
| Equipment failure | 7 | 13% |
| Human error | 6 | 12% |
| Weather event | 4 | 8% |

### Repeat incident trend

`incidents.repeatTrend` · type `chart` · size `md` · id `repeatTrend`

_shown by default._

**line chart** · unit: repeat incidents · 6 series · total 59

| Series | Value | Share |
|---|---|---|
| Mar | 8 | 14% |
| Apr | 11 | 19% |
| May | 9 | 15% |
| Jun | 12 | 20% |
| Jul | 10 | 17% |
| Aug | 9 | 15% |

### Incident register

`incidents.table` · type `table` · size `lg` · id `table`

_shown by default · default for Security._

| ID | Kind | Site | Severity | Status |
|---|---|---|---|---|
| INC-0001 | Medication error | Island | critical | Open |
| INC-0002 | Medication error | Coastal | critical | Open |
| INC-0003 | Zoonotic exposure | Wetland | critical | Open |
| INC-0004 | Equipment failure | Highland | critical | Open |
| INC-0005 | Medication error | Highland | critical | Open |
| INC-0006 | Bite / scratch | Central | high | Open |
| INC-0007 | Biosecurity breach | Wetland | medium | Open |
| INC-0008 | Feeding error | Highland | high | Open |

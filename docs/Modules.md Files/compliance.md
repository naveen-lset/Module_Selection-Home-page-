# Compliance & Audits

| | |
|---|---|
| Key | `compliance` |
| Route | `/topic/compliance` |
| Kind | Topic dashboard |
| Icon | `FileCheck` |
| Accent | `#2563EB` |
| Widgets | 6 in catalog, 4 shown by default |
| Widget types | alertFeed ×1, gauge ×1, list ×1, chart ×2, table ×1 |

## Roles

**Priority module for:** Management, Admin / Finance, HR / People.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Licence & deadline alerts | alertFeed | lg | `compliance.expiryAlerts` |
| 2 | SOP acknowledgment | gauge | md | `compliance.sopAck` |
| 3 | Open audit findings | list | md | `compliance.openFindings` |
| 4 | Pending compliance items | table | lg | `compliance.pendingItems` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Licence & deadline alerts | alertFeed | lg | `compliance.expiryAlerts` | yes |
| SOP acknowledgment | gauge | md | `compliance.sopAck` | yes |
| Open audit findings | list | md | `compliance.openFindings` | yes |
| Compliance item kinds | chart | md | `compliance.kindMix` | — |
| By authority | chart | md | `compliance.authorityMix` | — |
| Pending compliance items | table | lg | `compliance.pendingItems` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Licence & deadline alerts

`compliance.expiryAlerts` · type `alertFeed` · size `lg` · id `expiryAlerts`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Compliance | Licence — Wildlife protection — overdue 25 d (State Forest Dept) | 1 d |
| critical | Compliance | Licence — Wildlife protection — overdue 13 d (Pollution Control Board) | 1 d |
| critical | Compliance | Licence — CITES documentation — overdue 13 d (Pollution Control Board) | 1 d |
| critical | Compliance | Licence — Biomedical waste — overdue 5 d (Pollution Control Board) | 1 d |
| critical | Compliance | Licence — Animal welfare board — overdue 6 d (State Forest Dept) | 1 d |
| critical | Compliance | Licence — Fire safety — overdue 21 d (Pollution Control Board) | 1 d |

### SOP acknowledgment

`compliance.sopAck` · type `gauge` · size `md` · id `sopAck`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 71 | 100 | 71% | SOP acknowledgment | % | warn |

### Open audit findings

`compliance.openFindings` · type `list` · size `md` · id `openFindings`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Audit finding — Wildlife protection | Animal Welfare Board · owner Sneha Patil | Action required | warn |
| Audit finding — Biomedical waste | Animal Welfare Board · owner Kavya Bose | Submitted | warn |
| Audit finding — Wildlife protection | State Forest Dept · owner Divya Das | Submitted | warn |
| Audit finding — Wildlife protection | Fire Dept · owner Ritu Patil | Submitted | warn |
| Audit finding — Biomedical waste | Central Zoo Authority · owner Ritu Patil | Compliant | warn |
| Audit finding — CITES documentation | Central Zoo Authority · owner Divya Das | Compliant | warn |

### Compliance item kinds

`compliance.kindMix` · type `chart` · size `md` · id `kindMix`

**donut chart** · 6 series · total 48

| Series | Value | Share |
|---|---|---|
| Permit | 13 | 27% |
| Statutory report | 9 | 19% |
| Licence | 8 | 17% |
| SOP acknowledgment | 7 | 15% |
| Audit finding | 6 | 13% |
| Certification | 5 | 10% |

### By authority

`compliance.authorityMix` · type `chart` · size `md` · id `authorityMix`

**bar chart** · 6 series · total 48

| Series | Value | Share |
|---|---|---|
| Animal Welfare Board | 13 | 27% |
| Central Zoo Authority | 9 | 19% |
| Pollution Control Board | 8 | 17% |
| State Forest Dept | 7 | 15% |
| Fire Dept | 7 | 15% |
| Internal Audit | 4 | 8% |

### Pending compliance items

`compliance.pendingItems` · type `table` · size `lg` · id `pendingItems`

_shown by default._

| Item | Kind | Authority | Deadline | Status |
|---|---|---|---|---|
| Licence — Wildlife protection | Licence | State Forest Dept | Overdue 25 d | Overdue |
| Licence — Fire safety | Licence | Pollution Control Board | Overdue 21 d | Overdue |
| Licence — Wildlife protection | Licence | Pollution Control Board | Overdue 13 d | Overdue |
| Licence — CITES documentation | Licence | Pollution Control Board | Overdue 13 d | Overdue |
| Licence — Animal welfare board | Licence | State Forest Dept | Overdue 6 d | Overdue |
| Licence — Biomedical waste | Licence | Pollution Control Board | Overdue 5 d | Overdue |
| Statutory report — Biomedical waste | Statutory report | State Forest Dept | 4 d | Action required |
| Permit — Environmental clearance | Permit | State Forest Dept | 8 d | Action required |

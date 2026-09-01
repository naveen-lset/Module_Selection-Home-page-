# Payroll, Bonus & Rewards

| | |
|---|---|
| Key | `payroll` |
| Route | `/topic/payroll` |
| Kind | Topic dashboard |
| Icon | `IndianRupee` |
| Accent | `#15803D` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | kpi ×2, list ×1, chart ×2, table ×1 |

## Roles

**Priority module for:** Admin / Finance, HR / People.

**Role-specific default layouts:** HR / People. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Payroll status | kpi | md | `payroll.status` |
| 2 | Overtime cost | kpi | sm | `payroll.overtime` |
| 3 | Pending approvals | list | md | `payroll.pendingApprovals` |
| 4 | Department-wise cost | chart | md | `payroll.deptCost` |
| 5 | Payroll summary | table | lg | `payroll.table` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Payroll status | kpi | md | `payroll.status` | yes |
| Overtime cost | kpi | sm | `payroll.overtime` | yes |
| Pending approvals | list | md | `payroll.pendingApprovals` | yes |
| Department-wise cost | chart | md | `payroll.deptCost` | yes |
| Bonus eligibility | chart | md | `payroll.bonus` | — |
| Payroll summary | table | lg | `payroll.table` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Payroll status

`payroll.status` · type `kpi` · size `md` · id `status`

_shown by default · default for HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 6/12 departments processed | Payroll status (this month) | — | — | warn |

### Overtime cost

`payroll.overtime` · type `kpi` · size `sm` · id `overtime`

_shown by default · default for HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| ₹84.3 lakh | Overtime cost (month) | — | up | warn |

### Pending approvals

`payroll.pendingApprovals` · type `list` · size `md` · id `pendingApprovals`

_shown by default · default for HR / People._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Administration — 10 approvals pending | In progress · ₹180.54 lakh | — | warn |
| Veterinary Services — 9 approvals pending | Processed · ₹8.09 lakh | — | warn |
| Conservation & Research — 7 approvals pending | Processed · ₹148.59 lakh | — | warn |
| Animal Care — 10 approvals pending | In progress · ₹47.49 lakh | — | warn |
| Nutrition & Diet — 6 approvals pending | Processed · ₹54.23 lakh | — | warn |
| Pharmacy — 5 approvals pending | Processed · ₹61.63 lakh | — | warn |
| Engineering — 10 approvals pending | Pending approval · ₹149.95 lakh | — | warn |
| Safety & Security — 6 approvals pending | In progress · ₹205.19 lakh | — | warn |

### Department-wise cost

`payroll.deptCost` · type `chart` · size `md` · id `deptCost`

_shown by default · default for HR / People._

**bar chart** · unit: ₹ lakh · 12 series · total 1,375

| Series | Value | Share |
|---|---|---|
| Administration | 181 | 13% |
| Veterinary | 8 | 1% |
| Conservation | 149 | 11% |
| Animal | 47 | 3% |
| Nutrition | 54 | 4% |
| Pharmacy | 62 | 5% |
| Engineering | 150 | 11% |
| Safety | 205 | 15% |
| Finance | 115 | 8% |
| Human | 144 | 10% |
| Procurement | 75 | 5% |
| Housekeeping | 185 | 13% |

### Bonus eligibility

`payroll.bonus` · type `chart` · size `md` · id `bonus`

**bar chart** · unit: staff · 12 series · total 4,517

| Series | Value | Share |
|---|---|---|
| Administration | 219 | 5% |
| Veterinary | 504 | 11% |
| Conservation | 505 | 11% |
| Animal | 176 | 4% |
| Nutrition | 101 | 2% |
| Pharmacy | 573 | 13% |
| Engineering | 512 | 11% |
| Safety | 305 | 7% |
| Finance | 522 | 12% |
| Human | 143 | 3% |
| Procurement | 597 | 13% |
| Housekeeping | 360 | 8% |

### Payroll summary

`payroll.table` · type `table` · size `lg` · id `table`

_shown by default._

| Department | Headcount | Cost ₹ lakh | Overtime | Status |
|---|---|---|---|---|
| Administration | 972 | 180.54 | 3.63 | In progress |
| Veterinary Services | 1026 | 8.09 | 1.88 | Processed |
| Conservation & Research | 518 | 148.59 | 14.9 | Processed |
| Animal Care | 950 | 47.49 | 10.8 | In progress |
| Nutrition & Diet | 454 | 54.23 | 17.91 | Processed |
| Pharmacy | 784 | 61.63 | 14.21 | Processed |
| Engineering | 109 | 149.95 | 0.51 | Pending approval |
| Safety & Security | 814 | 205.19 | 1 | In progress |
| Finance | 71 | 114.77 | 0.84 | Processed |
| Human Resources | 182 | 144.15 | 11.2 | In progress |
| Procurement & Stores | 411 | 74.82 | 3.99 | In progress |
| Housekeeping | 421 | 184.69 | 3.43 | Processed |

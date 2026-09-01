# Finance & Budget

| | |
|---|---|
| Key | `finance` |
| Route | `/topic/finance` |
| Kind | Topic dashboard |
| Icon | `PiggyBank` |
| Accent | `#15803D` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | gauge ×1, kpi ×1, chart ×2, alertFeed ×1, list ×1, table ×1 |

## Roles

**Priority module for:** Management, Admin / Finance.

**Role-specific default layouts:** Management, Admin / Finance. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Annual budget utilised | gauge | md | `finance.utilisation` |
| 2 | Cost per animal per day | kpi | sm | `finance.costPerAnimal` |
| 3 | Budget vs actual | chart | lg | `finance.budgetVsActual` |
| 4 | Budget alerts | alertFeed | lg | `finance.budgetAlerts` |
| 5 | Cost centre summary | table | lg | `finance.spendTable` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Annual budget utilised | gauge | md | `finance.utilisation` | yes |
| Cost per animal per day | kpi | sm | `finance.costPerAnimal` | yes |
| Budget vs actual | chart | lg | `finance.budgetVsActual` | yes |
| Capex vs opex | chart | md | `finance.capexOpex` | — |
| Budget alerts | alertFeed | lg | `finance.budgetAlerts` | yes |
| Outstanding payments | list | md | `finance.outstanding` | — |
| Cost centre summary | table | lg | `finance.spendTable` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Annual budget utilised

`finance.utilisation` · type `gauge` · size `md` · id `utilisation`

_shown by default · default for Management, Admin / Finance._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 268 | 412 | 65% | Annual budget utilised | ₹ cr | good |

### Cost per animal per day

`finance.costPerAnimal` · type `kpi` · size `sm` · id `costPerAnimal`

_shown by default · default for Management._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| ₹96 | Cost per animal per day | +3% vs plan | up | neutral |

### Budget vs actual

`finance.budgetVsActual` · type `chart` · size `lg` · id `budgetVsActual`

_shown by default · default for Management, Admin / Finance._

**bar chart** · unit: % of budget · 14 series · total 1,085

| Series | Value | Share |
|---|---|---|
| Administration | 55 | 5% |
| Veterinary | 86 | 8% |
| Conservation | 101 | 9% |
| Animal | 49 | 5% |
| Nutrition | 107 | 10% |
| Pharmacy | 109 | 10% |
| Engineering | 82 | 8% |
| Safety | 67 | 6% |
| Finance | 43 | 4% |
| Human | 107 | 10% |
| Procurement | 58 | 5% |
| Housekeeping | 98 | 9% |

_2 further series not shown._

### Capex vs opex

`finance.capexOpex` · type `chart` · size `md` · id `capexOpex`

_default for Admin / Finance._

**donut chart** · unit: ₹ cr · 2 series · total 443

| Series | Value | Share |
|---|---|---|
| Capex | 117 | 26% |
| Opex | 326 | 74% |

### Budget alerts

`finance.budgetAlerts` · type `alertFeed` · size `lg` · id `budgetAlerts`

_shown by default · default for Management, Admin / Finance._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Finance | Conservation & Research over budget — ₹48.6 cr against ₹48.12 cr | 2 d |
| high | Finance | Nutrition & Diet over budget — ₹17.19 cr against ₹16.07 cr | 2 d |
| high | Finance | Pharmacy over budget — ₹49.34 cr against ₹45.27 cr | 2 d |
| high | Finance | Human Resources over budget — ₹38.11 cr against ₹35.62 cr | 2 d |

### Outstanding payments

`finance.outstanding` · type `list` · size `md` · id `outstanding`

_default for Admin / Finance._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Pharmacy — ₹168.94 lakh outstanding | Budget ₹45.27 cr · actual ₹49.34 cr | — | bad |
| Veterinary Services — ₹143.27 lakh outstanding | Budget ₹85.32 cr · actual ₹73.38 cr | — | neutral |
| Animal Care — ₹142.25 lakh outstanding | Budget ₹28.14 cr · actual ₹13.79 cr | — | neutral |
| Conservation & Research — ₹136.56 lakh outstanding | Budget ₹48.12 cr · actual ₹48.6 cr | — | bad |
| Feed & Nutrition — ₹117.83 lakh outstanding | Budget ₹23.71 cr · actual ₹10.91 cr | — | neutral |
| Procurement & Stores — ₹117.35 lakh outstanding | Budget ₹18.75 cr · actual ₹10.88 cr | — | neutral |
| Engineering — ₹91.78 lakh outstanding | Budget ₹77.87 cr · actual ₹63.85 cr | — | neutral |

### Cost centre summary

`finance.spendTable` · type `table` · size `lg` · id `spendTable`

_shown by default · default for Management, Admin / Finance._

| Cost centre | Budget ₹ cr | Actual ₹ cr | Capex | Outstanding ₹ lakh |
|---|---|---|---|---|
| Administration | 14.52 | 7.99 | 2.08 | 65.31 |
| Veterinary Services | 85.32 | 73.38 | 26.42 | 143.27 |
| Conservation & Research | 48.12 | 48.6 | 15.07 | 136.56 |
| Animal Care | 28.14 | 13.79 | 4 | 142.25 |
| Nutrition & Diet | 16.07 | 17.19 | 5.67 | 48.53 |
| Pharmacy | 45.27 | 49.34 | 16.78 | 168.94 |
| Engineering | 77.87 | 63.85 | 23.62 | 91.78 |
| Safety & Security | 51.35 | 34.4 | 1.72 | 52.27 |
| Finance | 34.74 | 14.94 | 1.2 | 1.09 |
| Human Resources | 35.62 | 38.11 | 7.62 | 80.1 |
| Procurement & Stores | 18.75 | 10.88 | 1.85 | 117.35 |
| Housekeeping | 23.58 | 23.11 | 4.39 | 88.57 |

_2 further row(s) not shown._

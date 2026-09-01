# Maintenance

| | |
|---|---|
| Key | `maintenance` |
| Route | `/topic/maintenance` |
| Kind | Topic dashboard |
| Icon | `Wrench` |
| Accent | `#B45309` |
| Widgets | 10 in catalog, 6 shown by default |
| Widget types | kpi ×3, alertFeed ×1, list ×1, chart ×4, table ×1 |

## Roles

**Priority module for:** Maintenance / Engineering.

**Role-specific default layouts:** Maintenance / Engineering. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Open work orders | kpi | sm | `maintenance.openTickets` |
| 2 | Equipment downtime | kpi | sm | `maintenance.downtime` |
| 3 | Critical breakdowns | alertFeed | lg | `maintenance.criticalAlerts` |
| 4 | Overdue work orders | list | md | `maintenance.overdue` |
| 5 | Priority mix | chart | md | `maintenance.priorityMix` |
| 6 | Work by trade | chart | md | `maintenance.tradeMix` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Open work orders | kpi | sm | `maintenance.openTickets` | yes |
| Equipment downtime | kpi | sm | `maintenance.downtime` | yes |
| Maintenance spend | kpi | sm | `maintenance.cost` | — |
| Critical breakdowns | alertFeed | lg | `maintenance.criticalAlerts` | yes |
| Overdue work orders | list | md | `maintenance.overdue` | yes |
| Priority mix | chart | md | `maintenance.priorityMix` | yes |
| Work by trade | chart | md | `maintenance.tradeMix` | yes |
| Status mix | chart | md | `maintenance.statusMix` | — |
| Breakdown frequency trend | chart | md | `maintenance.breakdownTrend` | — |
| Vendor & AMC status | table | lg | `maintenance.vendorAmc` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Open work orders

`maintenance.openTickets` · type `kpi` · size `sm` · id `openTickets`

_shown by default · default for Maintenance / Engineering._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 486 | Open work orders | 92 overdue | up | warn |

### Equipment downtime

`maintenance.downtime` · type `kpi` · size `sm` · id `downtime`

_shown by default · default for Maintenance / Engineering._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,666 h | Equipment downtime (30 d) | — | down | warn |

### Maintenance spend

`maintenance.cost` · type `kpi` · size `sm` · id `cost`

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| ₹184 lakh | Maintenance spend (30 d) | — | up | neutral |

### Critical breakdowns

`maintenance.criticalAlerts` · type `alertFeed` · size `lg` · id `criticalAlerts`

_shown by default · default for Maintenance / Engineering._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Maintenance | Lighting circuit fault — Desert | 5 h |
| critical | Maintenance | Filtration backwash fault — Grassland | 5 h |
| critical | Maintenance | HVAC not cooling — Coastal | 5 h |
| critical | Maintenance | Water pump failure — Coastal | 5 h |
| critical | Maintenance | Fence post replacement — Hilltop | 5 h |
| critical | Maintenance | Lighting circuit fault — Wetland | 5 h |

### Overdue work orders

`maintenance.overdue` · type `list` · size `md` · id `overdue`

_shown by default · default for Maintenance / Engineering._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Gate latch repair — Grassland | Due 13 Aug 2026 · HVAC · Ritu Iyer | Low | warn |
| Lighting circuit fault — Desert | Due 09 Sept 2026 · HVAC · Rahul Mishra | Critical | bad |
| Fence post replacement — Desert | Due 11 Sept 2026 · Civil · Vikas Mishra | Medium | warn |
| Gate latch repair — Wetland | Due 11 Aug 2026 · Plumbing · Karthik Khan | High | warn |
| Lighting circuit fault — Island | Due 30 Jun 2026 · Filtration · Karthik Khan | Medium | warn |
| Lighting circuit fault — Forest | Due 23 Jul 2026 · Electrical · Kavya Khan | Low | warn |
| Water pump failure — Grassland | Due 12 Jul 2026 · HVAC · Meghna Nair | Medium | warn |
| Gate latch repair — Wetland | Due 08 Jul 2026 · Electrical · Sanjay Bose | Low | warn |

### Priority mix

`maintenance.priorityMix` · type `chart` · size `md` · id `priorityMix`

_shown by default._

**donut chart** · 4 series · total 160

| Series | Value | Share |
|---|---|---|
| Medium | 54 | 34% |
| Low | 48 | 30% |
| High | 41 | 26% |
| Critical | 17 | 11% |

### Work by trade

`maintenance.tradeMix` · type `chart` · size `md` · id `tradeMix`

_shown by default · default for Maintenance / Engineering._

**bar chart** · 6 series · total 160

| Series | Value | Share |
|---|---|---|
| Plumbing | 34 | 21% |
| Electrical | 33 | 21% |
| Civil | 30 | 19% |
| Filtration | 27 | 17% |
| HVAC | 18 | 11% |
| Mechanical | 18 | 11% |

### Status mix

`maintenance.statusMix` · type `chart` · size `md` · id `statusMix`

_default for Maintenance / Engineering._

**donut chart** · 4 series · total 160

| Series | Value | Share |
|---|---|---|
| Open | 55 | 34% |
| Completed | 39 | 24% |
| In progress | 38 | 24% |
| Awaiting parts | 28 | 18% |

### Breakdown frequency trend

`maintenance.breakdownTrend` · type `chart` · size `md` · id `breakdownTrend`

**line chart** · unit: breakdowns · 6 series · total 814

| Series | Value | Share |
|---|---|---|
| Mar | 118 | 14% |
| Apr | 132 | 16% |
| May | 126 | 15% |
| Jun | 147 | 18% |
| Jul | 139 | 17% |
| Aug | 152 | 19% |

### Vendor & AMC status

`maintenance.vendorAmc` · type `table` · size `lg` · id `vendorAmc`

| Vendor | Category | AMC expiry (days) | Score |
|---|---|---|---|
| ColdChain Movers | Feed & fodder | 75 | 2/5 |
| ColdChain Movers | Medicines | 366 | 4/5 |
| MedEquip India | Lab consumables | 93 | 5/5 |
| GreenBuild Infra | Lab consumables | 163 | 4/5 |
| SafeGuard Solutions | Spare parts | 400 | 4/5 |
| ColdChain Movers | Lab consumables | 81 | 5/5 |
| MedEquip India | Medicines | -1 | 5/5 |
| FeedLine Traders | Lab consumables | 325 | 4/5 |

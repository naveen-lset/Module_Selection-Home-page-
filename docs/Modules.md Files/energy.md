# Electricity & Energy

| | |
|---|---|
| Key | `energy` |
| Route | `/topic/energy` |
| Kind | Topic dashboard |
| Icon | `Zap` |
| Accent | `#B45309` |
| Widgets | 9 in catalog, 6 shown by default |
| Widget types | kpi ×2, gauge ×1, chart ×4, alertFeed ×1, list ×1 |

## Roles

**Priority module for:** Maintenance / Engineering.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Electricity today | kpi | sm | `energy.totalConsumption` |
| 2 | Energy cost | kpi | sm | `energy.cost` |
| 3 | Backup power readiness | gauge | md | `energy.backupStatus` |
| 4 | Daily consumption trend | chart | lg | `energy.dailyTrend` |
| 5 | High consumption alerts | alertFeed | lg | `energy.highConsumptionAlerts` |
| 6 | Power outages | list | md | `energy.outages` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Electricity today | kpi | sm | `energy.totalConsumption` | yes |
| Energy cost | kpi | sm | `energy.cost` | yes |
| Backup power readiness | gauge | md | `energy.backupStatus` | yes |
| Daily consumption trend | chart | lg | `energy.dailyTrend` | yes |
| Consumption by site | chart | md | `energy.bySite` | — |
| Solar vs grid | chart | md | `energy.solarVsGrid` | — |
| Peak demand by block | chart | md | `energy.peakDemand` | — |
| High consumption alerts | alertFeed | lg | `energy.highConsumptionAlerts` | yes |
| Power outages | list | md | `energy.outages` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Electricity today

`energy.totalConsumption` · type `kpi` · size `sm` · id `totalConsumption`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 96,400 kWh | Electricity (today) | +7% vs target | up | warn |

### Energy cost

`energy.cost` · type `kpi` · size `sm` · id `cost`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| ₹142 lakh | Energy cost (month to date) | +6% vs plan | up | warn |

### Backup power readiness

`energy.backupStatus` · type `gauge` · size `md` · id `backupStatus`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 86 | 100 | 86% | UPS / backup readiness | % | good |

### Daily consumption trend

`energy.dailyTrend` · type `chart` · size `lg` · id `dailyTrend`

_shown by default._

**line chart** · unit: kWh · 30 series · total 26,64,571

| Series | Value | Share |
|---|---|---|
| 08-02 | 97,649 | 4% |
| 08-03 | 84,517 | 3% |
| 08-04 | 82,559 | 3% |
| 08-05 | 74,638 | 3% |
| 08-06 | 84,624 | 3% |
| 08-07 | 74,338 | 3% |
| 08-08 | 99,869 | 4% |
| 08-09 | 95,633 | 4% |
| 08-10 | 85,246 | 3% |
| 08-11 | 1,04,493 | 4% |
| 08-12 | 82,850 | 3% |
| 08-13 | 84,350 | 3% |

_18 further series not shown._

### Consumption by site

`energy.bySite` · type `chart` · size `md` · id `bySite`

**bar chart** · unit: kWh · 10 series · total 26,64,571

| Series | Value | Share |
|---|---|---|
| Riverside | 2,51,884 | 9% |
| Hilltop | 2,70,647 | 10% |
| Coastal | 2,75,839 | 10% |
| Central | 2,61,103 | 10% |
| Grassland | 2,76,017 | 10% |
| Wetland | 2,52,168 | 9% |
| Forest | 2,65,719 | 10% |
| Highland | 2,61,587 | 10% |
| Desert | 2,75,919 | 10% |
| Island | 2,73,688 | 10% |

### Solar vs grid

`energy.solarVsGrid` · type `chart` · size `md` · id `solarVsGrid`

**donut chart** · unit: kWh · 2 series · total 32,76,779

| Series | Value | Share |
|---|---|---|
| Solar generation | 6,12,208 | 19% |
| Grid consumption | 26,64,571 | 81% |

### Peak demand by block

`energy.peakDemand` · type `chart` · size `md` · id `peakDemand`

**bar chart** · unit: kWh · 6 series · total 51,200

| Series | Value | Share |
|---|---|---|
| 00-04 | 4,200 | 8% |
| 04-08 | 7,100 | 14% |
| 08-12 | 11,800 | 23% |
| 12-16 | 12,400 | 24% |
| 16-20 | 9,600 | 19% |
| 20-24 | 6,100 | 12% |

### High consumption alerts

`energy.highConsumptionAlerts` · type `alertFeed` · size `lg` · id `highConsumptionAlerts`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| medium | Energy | Central Quarantine Complex 18% above consumption target | 8 h |
| high | Energy | Aquatic life-support drawing 2.1× baseline — pump inefficiency suspected | 11 h |
| low | Energy | Generator run-hours exceeded monthly plan at Island Reserve | 2 d |

### Power outages

`energy.outages` · type `list` · size `md` · id `outages`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Grid outage — Coastal Marine Facility | 42 min · generator auto-start successful | Resolved | neutral |
| Grid outage — Island Species Reserve | 2 h 18 min · life-support on backup | Resolved | warn |
| Voltage fluctuation — Hospital Wing | Stabiliser replacement raised | Open | bad |

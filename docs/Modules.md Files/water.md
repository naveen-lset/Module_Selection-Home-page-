# Water Management

| | |
|---|---|
| Key | `water` |
| Route | `/topic/water` |
| Kind | Topic dashboard |
| Icon | `Droplets` |
| Accent | `#0891B2` |
| Widgets | 8 in catalog, 5 shown by default |
| Widget types | kpi ×1, gauge ×1, chart ×4, alertFeed ×1, table ×1 |

## Roles

**Priority module for:** Maintenance / Engineering.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Water consumption today | kpi | sm | `water.totalConsumption` |
| 2 | Reservoir level | gauge | md | `water.tankLevels` |
| 3 | Daily consumption trend | chart | lg | `water.dailyTrend` |
| 4 | Leakage & abnormal use | alertFeed | lg | `water.leakageAlerts` |
| 5 | Water quality parameters | table | md | `water.qualityParams` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Water consumption today | kpi | sm | `water.totalConsumption` | yes |
| Reservoir level | gauge | md | `water.tankLevels` | yes |
| Daily consumption trend | chart | lg | `water.dailyTrend` | yes |
| Consumption by site | chart | md | `water.bySite` | — |
| Recycled water usage | chart | md | `water.recycled` | — |
| Water cost trend | chart | md | `water.costTrend` | — |
| Leakage & abnormal use | alertFeed | lg | `water.leakageAlerts` | yes |
| Water quality parameters | table | md | `water.qualityParams` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Water consumption today

`water.totalConsumption` · type `kpi` · size `sm` · id `totalConsumption`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 4,820 kl | Water consumption (today) | +4% vs target | up | warn |

### Reservoir level

`water.tankLevels` · type `gauge` · size `md` · id `tankLevels`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 28 | 100 | 28% | Reservoir level — Desert Station | % | bad |

### Daily consumption trend

`water.dailyTrend` · type `chart` · size `lg` · id `dailyTrend`

_shown by default._

**line chart** · unit: kl · 30 series · total 1,41,486

| Series | Value | Share |
|---|---|---|
| 08-02 | 4,344 | 3% |
| 08-03 | 5,110 | 4% |
| 08-04 | 5,938 | 4% |
| 08-05 | 4,397 | 3% |
| 08-06 | 4,665 | 3% |
| 08-07 | 5,480 | 4% |
| 08-08 | 5,611 | 4% |
| 08-09 | 3,959 | 3% |
| 08-10 | 4,839 | 3% |
| 08-11 | 4,623 | 3% |
| 08-12 | 4,965 | 4% |
| 08-13 | 5,700 | 4% |

_18 further series not shown._

### Consumption by site

`water.bySite` · type `chart` · size `md` · id `bySite`

**bar chart** · unit: kl · 10 series · total 1,41,485

| Series | Value | Share |
|---|---|---|
| Riverside | 14,094 | 10% |
| Hilltop | 14,071 | 10% |
| Coastal | 14,710 | 10% |
| Central | 13,488 | 10% |
| Grassland | 14,938 | 11% |
| Wetland | 15,530 | 11% |
| Forest | 13,248 | 9% |
| Highland | 13,989 | 10% |
| Desert | 13,262 | 9% |
| Island | 14,155 | 10% |

### Recycled water usage

`water.recycled` · type `chart` · size `md` · id `recycled`

**line chart** · unit: kl · 30 series · total 32,618

| Series | Value | Share |
|---|---|---|
| 08-02 | 1,392 | 4% |
| 08-03 | 1,164 | 4% |
| 08-04 | 1,226 | 4% |
| 08-05 | 1,519 | 5% |
| 08-06 | 1,221 | 4% |
| 08-07 | 1,116 | 3% |
| 08-08 | 791 | 2% |
| 08-09 | 1,046 | 3% |
| 08-10 | 1,133 | 3% |
| 08-11 | 936 | 3% |
| 08-12 | 1,213 | 4% |
| 08-13 | 957 | 3% |

_18 further series not shown._

### Water cost trend

`water.costTrend` · type `chart` · size `md` · id `costTrend`

**bar chart** · unit: ₹ lakh · 4 series · total 85

| Series | Value | Share |
|---|---|---|
| May | 18 | 21% |
| Jun | 21 | 25% |
| Jul | 24 | 28% |
| Aug | 22 | 26% |

### Leakage & abnormal use

`water.leakageAlerts` · type `alertFeed` · size `lg` · id `leakageAlerts`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Water | Abnormal night-time flow detected — Herbivores Section main line | 6 h |
| medium | Water | Borewell 3 yield down 22% at Hilltop Campus | 1 d |
| medium | Water | Filtration backwash overdue — Aquatic Systems | 2 d |

### Water quality parameters

`water.qualityParams` · type `table` · size `md` · id `qualityParams`

_shown by default._

| Parameter | Reading | Limit | Status |
|---|---|---|---|
| pH | 7.4 | 6.5 – 8.5 | Within limit |
| Dissolved oxygen | 6.8 mg/l | > 5 mg/l | Within limit |
| Ammonia | 0.42 mg/l | < 0.5 mg/l | Watch |
| Turbidity | 3.1 NTU | < 5 NTU | Within limit |
| Coliform | Absent | Absent | Within limit |

# Food & Diet Inventory

| | |
|---|---|
| Key | `feed-inventory` |
| Route | `/topic/feed-inventory` |
| Kind | Topic dashboard |
| Icon | `Wheat` |
| Accent | `#15803D` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | kpi ×1, gauge ×1, chart ×2, alertFeed ×1, table ×2 |

## Roles

**Priority module for:** Nutritionist, Procurement.

**Role-specific default layouts:** Nutritionist, Procurement. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Feed stock cover | kpi | sm | `feed.daysCover` |
| 2 | Cold storage temperature | gauge | md | `feed.coldStorage` |
| 3 | Stock by category | chart | md | `feed.stockByCategory` |
| 4 | Reorder alerts | alertFeed | lg | `feed.reorderAlerts` |
| 5 | Expiry & spoilage tracking | table | md | `feed.expiryTracking` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Feed stock cover | kpi | sm | `feed.daysCover` | yes |
| Cold storage temperature | gauge | md | `feed.coldStorage` | yes |
| Stock by category | chart | md | `feed.stockByCategory` | yes |
| Consumption forecast | chart | md | `feed.consumptionForecast` | — |
| Reorder alerts | alertFeed | lg | `feed.reorderAlerts` | yes |
| Expiry & spoilage tracking | table | md | `feed.expiryTracking` | yes |
| Kitchen-wise stock | table | lg | `feed.kitchenStock` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Feed stock cover

`feed.daysCover` · type `kpi` · size `sm` · id `daysCover`

_shown by default · default for Nutritionist, Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 11 days | Feed stock cover | — | down | warn |

### Cold storage temperature

`feed.coldStorage` · type `gauge` · size `md` · id `coldStorage`

_shown by default · default for Nutritionist._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 4 | 8 | 50% | Cold storage temperature | °C | good |

### Stock by category

`feed.stockByCategory` · type `chart` · size `md` · id `stockByCategory`

_shown by default · default for Nutritionist._

**donut chart** · unit: kg · 5 series · total 8,320

| Series | Value | Share |
|---|---|---|
| Dry feed | 3,820 | 46% |
| Fresh produce | 2,140 | 26% |
| Frozen meat | 1,680 | 20% |
| Live feed | 420 | 5% |
| Supplements | 260 | 3% |

### Consumption forecast

`feed.consumptionForecast` · type `chart` · size `md` · id `consumptionForecast`

_default for Nutritionist._

**line chart** · unit: kg · 6 series · total 52,070

| Series | Value | Share |
|---|---|---|
| Wk 1 | 8,420 | 16% |
| Wk 2 | 8,610 | 17% |
| Wk 3 | 8,380 | 16% |
| Wk 4 | 8,740 | 17% |
| Wk 5 (f) | 8,900 | 17% |
| Wk 6 (f) | 9,020 | 17% |

### Reorder alerts

`feed.reorderAlerts` · type `alertFeed` · size `lg` · id `reorderAlerts`

_shown by default · default for Nutritionist, Procurement._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Feed | Fresh produce cover down to 2 days at Coastal Marine Facility | 4 h |
| high | Feed | Frozen meat below minimum stock at Highland Carnivore Centre | 7 h |
| medium | Feed | Live feed (crickets) reorder pending vendor confirmation | 1 d |
| medium | Feed | Supplement stock (calcium powder) at reorder level | 2 d |

### Expiry & spoilage tracking

`feed.expiryTracking` · type `table` · size `md` · id `expiryTracking`

_shown by default._

| Batch | Item | Days to expiry | Qty (kg) |
|---|---|---|---|
| FB-2291 | Frozen chicken | 4 | 320 |
| FB-2288 | Frozen fish — tilapia | 6 | 210 |
| FB-2276 | Boiled egg batch | 2 | 48 |
| FB-2261 | Banana — ripe | 1 | 96 |
| FB-2244 | Pellet feed | 38 | 1240 |
| FB-2231 | Lucerne hay | 52 | 2860 |

### Kitchen-wise stock

`feed.kitchenStock` · type `table` · size `lg` · id `kitchenStock`

_default for Procurement._

| Kitchen | Dry (kg) | Fresh (kg) | Frozen (kg) | Variance |
|---|---|---|---|---|
| Riverside kitchen | 620 | 380 | 290 | -2% |
| Hilltop kitchen | 580 | 355 | 272 | +3% |
| Coastal kitchen | 540 | 330 | 254 | -4% |
| Central kitchen | 500 | 305 | 236 | +5% |
| Grassland kitchen | 460 | 280 | 218 | -6% |
| Wetland kitchen | 420 | 255 | 200 | +7% |

# Diet & Nutrition

| | |
|---|---|
| Key | `diet` |
| Route | `/topic/diet` |
| Kind | Topic dashboard |
| Icon | `Utensils` |
| Accent | `#B45309` |
| Widgets | 8 in catalog, 6 shown by default |
| Widget types | gauge ×1, kpi ×1, table ×2, list ×2, chart ×2 |

## Roles

**Priority module for:** Paravet, Keeper / Animal Care, Nutritionist.

**Role-specific default layouts:** Keeper / Animal Care, Nutritionist. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Diet compliance | gauge | md | `diet.compliance` |
| 2 | Average feed wastage | kpi | sm | `diet.wastage` |
| 3 | Feeding schedule | table | lg | `diet.feedingSchedule` |
| 4 | Medical & special diets | list | md | `diet.specialDiets` |
| 5 | Body-condition trend | chart | md | `diet.bodyConditionTrend` |
| 6 | Kitchen production plan | table | lg | `diet.kitchenPlan` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Diet compliance | gauge | md | `diet.compliance` | yes |
| Average feed wastage | kpi | sm | `diet.wastage` | yes |
| Feeding schedule | table | lg | `diet.feedingSchedule` | yes |
| Medical & special diets | list | md | `diet.specialDiets` | yes |
| Diet reviews due | list | md | `diet.upcomingChanges` | — |
| Body-condition trend | chart | md | `diet.bodyConditionTrend` | yes |
| Diet cost by species | chart | md | `diet.costBySpecies` | — |
| Kitchen production plan | table | lg | `diet.kitchenPlan` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Diet compliance

`diet.compliance` · type `gauge` · size `md` · id `compliance`

_shown by default · default for Keeper / Animal Care, Nutritionist._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 81 | 100 | 81% | Diet compliance | % | warn |

### Average feed wastage

`diet.wastage` · type `kpi` · size `sm` · id `wastage`

_shown by default · default for Nutritionist._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 12% | Average feed wastage | — | down | good |

### Feeding schedule

`diet.feedingSchedule` · type `table` · size `lg` · id `feedingSchedule`

_shown by default · default for Keeper / Animal Care, Nutritionist._

| Plan | Scope | Feeds/day | Qty (kg) | Compliance |
|---|---|---|---|---|
| Bengal Tiger — standard plan | Individual | 2 | 1.54 | 89% |
| Asiatic Lion — standard plan | Individual | 2 | 48.86 | 74% |
| Indian Leopard — standard plan | Group | 2 | 44.2 | 80% |
| Snow Leopard — standard plan | Species | 3 | 0.99 | 93% |
| Clouded Leopard — standard plan | Group | 3 | 45.98 | 72% |
| Fishing Cat — standard plan | Species | 4 | 38.69 | 90% |
| Asian Elephant — standard plan | Species | 1 | 58.9 | 95% |
| Indian Rhinoceros — standard plan | Species | 3 | 59.24 | 91% |

### Medical & special diets

`diet.specialDiets` · type `list` · size `md` · id `specialDiets`

_shown by default · default for Keeper / Animal Care._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Asian Elephant — standard plan | Therapeutic · supplements: none | Medical diet | warn |
| Lion-tailed Macaque — standard plan | Therapeutic · supplements: none | Medical diet | warn |
| Chimpanzee — standard plan | Therapeutic · supplements: Multivitamin | Medical diet | warn |
| Painted Stork — standard plan | Therapeutic · supplements: Vitamin D3 | Medical diet | warn |
| Great Hornbill — standard plan | Therapeutic · supplements: Multivitamin | Medical diet | warn |
| White-rumped Vulture — standard plan | Therapeutic · supplements: Multivitamin, Mineral mix, Calcium powder | Medical diet | warn |
| Barn Owl — standard plan | Therapeutic · supplements: Calcium powder, Omega-3 oil | Medical diet | warn |

### Diet reviews due

`diet.upcomingChanges` · type `list` · size `md` · id `upcomingChanges`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Asiatic Lion — standard plan — diet review due | Compliance 74% · approved by Karthik Thomas | — | warn |
| Clouded Leopard — standard plan — diet review due | Compliance 72% · approved by Karthik Thomas | — | warn |
| Himalayan Black Bear — standard plan — diet review due | Compliance 64% · approved by Rahul Thomas | — | warn |
| Red Panda — standard plan — diet review due | Compliance 67% · approved by Fatima Bose | — | warn |
| Indian Wolf — standard plan — diet review due | Compliance 79% · approved by Vikas Das | — | warn |
| Dhole — standard plan — diet review due | Compliance 65% · approved by Karthik Das | — | warn |

### Body-condition trend

`diet.bodyConditionTrend` · type `chart` · size `md` · id `bodyConditionTrend`

_shown by default · default for Nutritionist._

**line chart** · unit: BCS · 6 series · total 19.6

| Series | Value | Share |
|---|---|---|
| Mar | 3.1 | 16% |
| Apr | 3.2 | 16% |
| May | 3.2 | 16% |
| Jun | 3.3 | 17% |
| Jul | 3.4 | 17% |
| Aug | 3.4 | 17% |

### Diet cost by species

`diet.costBySpecies` · type `chart` · size `md` · id `costBySpecies`

_default for Nutritionist._

**bar chart** · unit: ₹/day · 8 series · total 33,021

| Series | Value | Share |
|---|---|---|
| Snail | 4,199 | 13% |
| Sambar | 4,193 | 13% |
| Stingray | 4,179 | 13% |
| Shark | 4,176 | 13% |
| Dhole | 4,152 | 13% |
| Hyena | 4,146 | 13% |
| Cat | 4,029 | 12% |
| Arowana | 3,947 | 12% |

### Kitchen production plan

`diet.kitchenPlan` · type `table` · size `lg` · id `kitchenPlan`

_shown by default · default for Nutritionist._

| Kitchen | Plans | Daily qty (kg) | Cost ₹/day |
|---|---|---|---|
| Riverside Rescue Centre kitchen | 8 | 298.4 | 12,957 |
| Hilltop Rehabilitation Campus kitchen | 8 | 240.2 | 19,087 |
| Coastal Marine Facility kitchen | 8 | 236.0 | 16,819 |
| Central Quarantine Complex kitchen | 8 | 306.5 | 15,998 |
| Grassland Conservation Park kitchen | 8 | 232.4 | 16,958 |
| Wetland Bird Sanctuary Unit kitchen | 8 | 233.6 | 14,945 |

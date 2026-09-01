# Other Utilities

| | |
|---|---|
| Key | `utilities` |
| Route | `/topic/utilities` |
| Kind | Topic dashboard |
| Icon | `Flame` |
| Accent | `#7C3AED` |
| Widgets | 5 in catalog, 4 shown by default |
| Widget types | list ×1, gauge ×1, chart ×2, table ×1 |

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Fuel, LPG & oxygen levels | list | md | `utilities.fuelLevels` |
| 2 | Network availability | gauge | md | `utilities.networkAvailability` |
| 3 | Waste generation mix | chart | md | `utilities.wasteMix` |
| 4 | Treatment plant status | table | lg | `utilities.treatmentStatus` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Fuel, LPG & oxygen levels | list | md | `utilities.fuelLevels` | yes |
| Network availability | gauge | md | `utilities.networkAvailability` | yes |
| Waste generation mix | chart | md | `utilities.wasteMix` | yes |
| Utility cost split | chart | md | `utilities.costTrend` | — |
| Treatment plant status | table | lg | `utilities.treatmentStatus` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Fuel, LPG & oxygen levels

`utilities.fuelLevels` · type `list` · size `md` · id `fuelLevels`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Diesel | 1,849 l consumed today · 62% tank | OK | neutral |
| LPG (feed kitchen) | 18 cylinders in stock · 4 days cover | Watch | warn |
| Medical oxygen | 9 cylinders available · hospital wing | OK | good |
| Petrol (patrol vehicles) | 340 l in stock | OK | neutral |

### Network availability

`utilities.networkAvailability` · type `gauge` · size `md` · id `networkAvailability`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 97 | 100 | 97% | Network availability (30 d) | % | good |

### Waste generation mix

`utilities.wasteMix` · type `chart` · size `md` · id `wasteMix`

_shown by default._

**donut chart** · unit: kg/month · 4 series · total 8,530

| Series | Value | Share |
|---|---|---|
| Organic waste | 4,820 | 57% |
| Biomedical waste | 310 | 4% |
| Recyclable | 1,240 | 15% |
| General waste | 2,160 | 25% |

### Utility cost split

`utilities.costTrend` · type `chart` · size `md` · id `costTrend`

**bar chart** · unit: ₹ lakh · 5 series · total 83

| Series | Value | Share |
|---|---|---|
| Diesel | 34 | 41% |
| LPG | 12 | 14% |
| Water | 22 | 27% |
| Waste | 9 | 11% |
| Internet | 6 | 7% |

### Treatment plant status

`utilities.treatmentStatus` · type `table` · size `lg` · id `treatmentStatus`

_shown by default._

| Plant | Capacity | Load | Status |
|---|---|---|---|
| STP — Riverside | 450 kld | 68% | Operational |
| STP — Central | 300 kld | 81% | Operational |
| ETP — Hospital wing | 60 kld | 54% | Operational |
| Composting unit | 6 t/day | 72% | Operational |
| Biomedical waste store | 400 kg | 46% | Pickup due |

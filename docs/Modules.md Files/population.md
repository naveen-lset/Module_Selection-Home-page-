# Animal Population Planning

| | |
|---|---|
| Key | `population` |
| Route | `/topic/population` |
| Kind | Topic dashboard |
| Icon | `PieChart` |
| Accent | `#2563EB` |
| Widgets | 5 in catalog, 4 shown by default |
| Widget types | gauge ×1, chart ×1, list ×3 |

## Roles

**Priority module for:** Biologist.

**Role-specific default layouts:** Biologist. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Holding vs approved capacity | gauge | md | `population.carryingCapacity` |
| 2 | Population vs target | chart | lg | `population.vsTarget` |
| 3 | Unbalanced sex ratios | list | md | `population.sexRatioFlags` |
| 4 | Inbreeding risk | list | md | `population.inbreedingRisk` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Holding vs approved capacity | gauge | md | `population.carryingCapacity` | yes |
| Population vs target | chart | lg | `population.vsTarget` | yes |
| Unbalanced sex ratios | list | md | `population.sexRatioFlags` | yes |
| Inbreeding risk | list | md | `population.inbreedingRisk` | yes |
| Planned exchanges | list | md | `population.plannedTransfers` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Holding vs approved capacity

`population.carryingCapacity` · type `gauge` · size `md` · id `carryingCapacity`

_shown by default · default for Biologist._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 1500 | 3854 | 39% | Holding against approved capacity | — | bad |

### Population vs target

`population.vsTarget` · type `chart` · size `lg` · id `vsTarget`

_shown by default · default for Biologist._

**bar chart** · unit: % of target · 8 series · total 631

| Series | Value | Share |
|---|---|---|
| Tiger | 60 | 10% |
| Lion | 67 | 11% |
| Leopard | 74 | 12% |
| Leopard | 81 | 13% |
| Leopard | 88 | 14% |
| Cat | 95 | 15% |
| Elephant | 102 | 16% |
| Rhinoceros | 64 | 10% |

### Unbalanced sex ratios

`population.sexRatioFlags` · type `list` · size `md` · id `sexRatioFlags`

_shown by default · default for Biologist._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Bengal Tiger — skewed sex ratio | 3M : 1F in current holding | — | warn |
| Asiatic Lion — skewed sex ratio | 4M : 1F in current holding | — | warn |
| Indian Leopard — skewed sex ratio | 5M : 1F in current holding | — | warn |
| Snow Leopard — skewed sex ratio | 6M : 1F in current holding | — | warn |
| Clouded Leopard — skewed sex ratio | 7M : 1F in current holding | — | warn |
| Fishing Cat — skewed sex ratio | 8M : 1F in current holding | — | warn |

### Inbreeding risk

`population.inbreedingRisk` · type `list` · size `md` · id `inbreedingRisk`

_shown by default · default for Biologist._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Indian Star Tortoise — low genetic diversity | Index 0.42 · founder exchange recommended | — | bad |
| Mugger Crocodile — low genetic diversity | Index 0.43 · founder exchange recommended | — | bad |
| Cane Toad — low genetic diversity | Index 0.44 · founder exchange recommended | — | bad |
| Ostrich — low genetic diversity | Index 0.45 · founder exchange recommended | — | bad |
| Snow Leopard — low genetic diversity | Index 0.46 · founder exchange recommended | — | bad |
| Snow Leopard — low genetic diversity | Index 0.47 · founder exchange recommended | — | bad |

### Planned exchanges

`population.plannedTransfers` · type `list` · size `md` · id `plannedTransfers`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Bengal Tiger — planned exchange | From ISO-125 · 28 Aug 2026 | Planned | neutral |
| Snow Leopard — planned exchange | From HER-151 · 17 Aug 2026 | Planned | neutral |
| Asian Elephant — planned exchange | From SMA-075 · 05 Sept 2026 | Planned | neutral |
| Himalayan Black Bear — planned exchange | From NOC-065 · 13 Dec 2026 | Planned | neutral |
| Golden Jackal — planned exchange | From PRI-078 · 23 Dec 2026 | Planned | neutral |
| Rhesus Macaque — planned exchange | From INV-115 · 02 Feb 2027 | Planned | neutral |

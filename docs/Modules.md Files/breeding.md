# Breeding & Conservation

| | |
|---|---|
| Key | `breeding` |
| Route | `/topic/breeding` |
| Kind | Topic dashboard |
| Icon | `Egg` |
| Accent | `#0891B2` |
| Widgets | 8 in catalog, 6 shown by default |
| Widget types | kpi ×1, gauge ×1, list ×3, chart ×2, table ×1 |

## Roles

**Priority module for:** Biologist.

**Role-specific default layouts:** Biologist. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Active breeding pairs | kpi | sm | `breeding.activePairs` |
| 2 | Breeding targets achieved | gauge | md | `breeding.targets` |
| 3 | Expected births & hatchings | list | md | `breeding.expectedBirths` |
| 4 | Reproductive status mix | chart | md | `breeding.statusMix` |
| 5 | Hand-rearing cases | list | md | `breeding.handRearing` |
| 6 | Studbook records | table | lg | `breeding.studbook` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Active breeding pairs | kpi | sm | `breeding.activePairs` | yes |
| Breeding targets achieved | gauge | md | `breeding.targets` | yes |
| Expected births & hatchings | list | md | `breeding.expectedBirths` | yes |
| Hand-rearing cases | list | md | `breeding.handRearing` | yes |
| Failed breeding attempts | list | md | `breeding.failedAttempts` | — |
| Reproductive status mix | chart | md | `breeding.statusMix` | yes |
| Genetic diversity index | chart | md | `breeding.geneticDiversity` | — |
| Studbook records | table | lg | `breeding.studbook` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Active breeding pairs

`breeding.activePairs` · type `kpi` · size `sm` · id `activePairs`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 54 | Active breeding pairs | 18 gravid | up | neutral |

### Breeding targets achieved

`breeding.targets` · type `gauge` · size `md` · id `targets`

_shown by default · default for Biologist._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 18 | 40 | 45% | Breeding targets achieved | — | bad |

### Expected births & hatchings

`breeding.expectedBirths` · type `list` · size `md` · id `expectedBirths`

_shown by default · default for Biologist._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Mugger Crocodile — PAIR-016 | Expected 12 Aug 2026 · LAR-138 | Pregnant/Gravid | neutral |
| Snow Leopard — PAIR-002 | Expected 17 Aug 2026 · HER-151 | Pregnant/Gravid | neutral |
| Bengal Tiger — PAIR-001 | Expected 28 Aug 2026 · ISO-125 | Pregnant/Gravid | neutral |
| Blackbuck — PAIR-031 | Expected 02 Sept 2026 · REP-168 | Incubating | neutral |
| Asian Elephant — PAIR-003 | Expected 05 Sept 2026 · SMA-075 | Pregnant/Gravid | neutral |
| Golden Jackal — PAIR-029 | Expected 20 Sept 2026 · SMA-144 | Incubating | neutral |
| Snow Leopard — PAIR-050 | Expected 04 Nov 2026 · ELE-017 | Incubating | neutral |
| Cane Toad — PAIR-044 | Expected 13 Nov 2026 · AQU-109 | Pregnant/Gravid | neutral |

### Hand-rearing cases

`breeding.handRearing` · type `list` · size `md` · id `handRearing`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Golden Jackal — hand-rearing | 0 offspring · survival 45% | — | warn |
| Chimpanzee — hand-rearing | 0 offspring · survival 89% | — | good |
| Mugger Crocodile — hand-rearing | 0 offspring · survival 61% | — | warn |
| Asian Arowana — hand-rearing | 6 offspring · survival 54% | — | warn |
| Cane Toad — hand-rearing | 0 offspring · survival 46% | — | warn |
| Blacktip Reef Shark — hand-rearing | 0 offspring · survival 81% | — | good |

### Failed breeding attempts

`breeding.failedAttempts` · type `list` · size `md` · id `failedAttempts`

_default for Biologist._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Greater Adjutant — failed attempt | PAIR-010 · review recommended | — | bad |
| Indian Ornamental Tarantula — failed attempt | PAIR-023 · review recommended | — | bad |
| Atlas Moth — failed attempt | PAIR-024 · review recommended | — | bad |
| Himalayan Black Bear — failed attempt | PAIR-052 · review recommended | — | bad |
| Blackbuck — failed attempt | PAIR-055 · review recommended | — | bad |

### Reproductive status mix

`breeding.statusMix` · type `chart` · size `md` · id `statusMix`

_shown by default · default for Biologist._

**donut chart** · 6 series · total 64

| Series | Value | Share |
|---|---|---|
| Offspring present | 18 | 28% |
| Paired | 15 | 23% |
| Pregnant/Gravid | 13 | 20% |
| Incubating | 8 | 13% |
| Failed | 5 | 8% |
| Contracepted | 5 | 8% |

### Genetic diversity index

`breeding.geneticDiversity` · type `chart` · size `md` · id `geneticDiversity`

_default for Biologist._

**bar chart** · unit: index · 8 series · total 362

| Series | Value | Share |
|---|---|---|
| Tortoise | 42 | 12% |
| Crocodile | 43 | 12% |
| Toad | 44 | 12% |
| Ostrich | 45 | 12% |
| Leopard | 46 | 13% |
| Leopard | 47 | 13% |
| Leopard | 47 | 13% |
| Shark | 48 | 13% |

### Studbook records

`breeding.studbook` · type `table` · size `lg` · id `studbook`

_shown by default · default for Biologist._

| Studbook | Species | Status | Offspring | Survival % |
|---|---|---|---|---|
| SB-0001-779 | Bengal Tiger | Pregnant/Gravid | 1 | 83 |
| SB-0004-763 | Snow Leopard | Pregnant/Gravid | 1 | 92 |
| SB-0007-219 | Asian Elephant | Pregnant/Gravid | 2 | 98 |
| SB-0010-867 | Himalayan Black Bear | Incubating | 2 | 73 |
| SB-0013-307 | Golden Jackal | Paired | 0 | 45 |
| SB-0016-601 | Rhesus Macaque | Incubating | 1 | 73 |
| SB-0019-391 | Blackbuck | Paired | 0 | 69 |
| SB-0022-833 | Gaur | Offspring present | 2 | 64 |

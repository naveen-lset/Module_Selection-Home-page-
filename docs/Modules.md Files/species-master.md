# Species & Taxonomy Master

| | |
|---|---|
| Key | `species-master` |
| Route | `/topic/species-master` |
| Kind | Topic dashboard |
| Icon | `Dna` |
| Accent | `#0891B2` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | kpi ×1, chart ×3, list ×1, table ×1 |

## Roles

**Priority module for:** Biologist.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Species in master data | kpi | sm | `species.totals` |
| 2 | IUCN status mix | chart | md | `species.iucnMix` |
| 3 | CITES appendix mix | chart | md | `species.citesMix` |
| 4 | Dangerous species | list | md | `species.dangerous` |
| 5 | Species directory | table | lg | `species.directory` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Species in master data | kpi | sm | `species.totals` | yes |
| IUCN status mix | chart | md | `species.iucnMix` | yes |
| CITES appendix mix | chart | md | `species.citesMix` | yes |
| Class mix | chart | md | `species.classMix` | — |
| Dangerous species | list | md | `species.dangerous` | yes |
| Species directory | table | lg | `species.directory` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Species in master data

`species.totals` · type `kpi` · size `sm` · id `totals`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 2,143 | Species in master data | 486 subspecies | flat | neutral |

### IUCN status mix

`species.iucnMix` · type `chart` · size `md` · id `iucnMix`

_shown by default._

**donut chart** · 6 series · total 72

| Series | Value | Share |
|---|---|---|
| LC | 25 | 35% |
| EN | 17 | 24% |
| VU | 17 | 24% |
| NT | 6 | 8% |
| CR | 4 | 6% |
| DD | 3 | 4% |

### CITES appendix mix

`species.citesMix` · type `chart` · size `md` · id `citesMix`

_shown by default._

**bar chart** · 4 series · total 72

| Series | Value | Share |
|---|---|---|
| App I | 28 | 39% |
| App II | 20 | 28% |
| App None | 18 | 25% |
| App III | 6 | 8% |

### Class mix

`species.classMix` · type `chart` · size `md` · id `classMix`

**donut chart** · 6 series · total 72

| Series | Value | Share |
|---|---|---|
| Mammal | 25 | 35% |
| Bird | 15 | 21% |
| Reptile | 12 | 17% |
| Fish | 8 | 11% |
| Amphibian | 6 | 8% |
| Invertebrate | 6 | 8% |

### Dangerous species

`species.dangerous` · type `list` · size `md` · id `dangerous`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Bengal Tiger | Panthera tigris tigris · High risk | High | warn |
| Asiatic Lion | Panthera leo persica · High risk | High | warn |
| Indian Leopard | Panthera pardus fusca · High risk | High | warn |
| Snow Leopard | Panthera uncia · High risk | High | warn |
| Clouded Leopard | Neofelis nebulosa · High risk | High | warn |
| Fishing Cat | Prionailurus viverrinus · High risk | High | warn |
| Asian Elephant | Elephas maximus · Extreme risk | Extreme | bad |
| Indian Rhinoceros | Rhinoceros unicornis · High risk | High | warn |

### Species directory

`species.directory` · type `table` · size `lg` · id `directory`

_shown by default._

| Common name | Scientific name | Class | IUCN | CITES |
|---|---|---|---|---|
| Bengal Tiger | Panthera tigris tigris | Mammal | EN | I |
| Asiatic Lion | Panthera leo persica | Mammal | EN | I |
| Indian Leopard | Panthera pardus fusca | Mammal | VU | I |
| Snow Leopard | Panthera uncia | Mammal | VU | I |
| Clouded Leopard | Neofelis nebulosa | Mammal | VU | I |
| Fishing Cat | Prionailurus viverrinus | Mammal | VU | II |
| Asian Elephant | Elephas maximus | Mammal | EN | I |
| Indian Rhinoceros | Rhinoceros unicornis | Mammal | VU | I |
| Sloth Bear | Melursus ursinus | Mammal | VU | I |
| Himalayan Black Bear | Ursus thibetanus laniger | Mammal | VU | I |

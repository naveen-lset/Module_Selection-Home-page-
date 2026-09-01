# Animal Collection

| | |
|---|---|
| Key | `animal-collection` |
| Route | `/topic/animal-collection` |
| Kind | Topic dashboard |
| Icon | `PawPrint` |
| Accent | `#0F766E` |
| Widgets | 15 in catalog, 8 shown by default |
| Widget types | kpi ×3, chart ×7, list ×3, timeline ×1, table ×1 |

## Roles

**Priority module for:** Biologist, Paravet, Keeper / Animal Care, Nutritionist.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Total animals | kpi | sm | `animals.total` |
| 2 | Species / subspecies | kpi | sm | `animals.speciesTotal` |
| 3 | Quarantine / isolation / hospital | kpi | md | `animals.inCare` |
| 4 | Animals by class | chart | md | `animals.byClass` |
| 5 | Sex distribution | chart | md | `animals.bySex` |
| 6 | Conservation status | list | md | `animals.conservationStatus` |
| 7 | Births, deaths and transfers | timeline | lg | `animals.recentEvents` |
| 8 | Animals by site | table | lg | `animals.bySite` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Total animals | kpi | sm | `animals.total` | yes |
| Species / subspecies | kpi | sm | `animals.speciesTotal` | yes |
| Quarantine / isolation / hospital | kpi | md | `animals.inCare` | yes |
| Animals by class | chart | md | `animals.byClass` | yes |
| Sex distribution | chart | md | `animals.bySex` | yes |
| Life-stage distribution | chart | md | `animals.byLifeStage` | — |
| Wild-born vs captive-born | chart | md | `animals.byOrigin` | — |
| Native vs exotic species | chart | md | `animals.nativeExotic` | — |
| Health status mix | chart | md | `animals.healthStatusMix` | — |
| Identification status | chart | md | `animals.identificationStatus` | — |
| Conservation status | list | md | `animals.conservationStatus` | yes |
| New arrivals | list | md | `animals.newArrivals` | — |
| Upcoming planned movements | list | md | `animals.plannedMovements` | — |
| Births, deaths and transfers | timeline | lg | `animals.recentEvents` | yes |
| Animals by site | table | lg | `animals.bySite` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Total animals

`animals.total` · type `kpi` · size `sm` · id `total`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,04,382 | Total animals | +1,428 in 30 d | up | neutral |

### Species / subspecies

`animals.speciesTotal` · type `kpi` · size `sm` · id `speciesTotal`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 2,143 / 486 | Species / subspecies | — | — | neutral |

### Quarantine / isolation / hospital

`animals.inCare` · type `kpi` · size `md` · id `inCare`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 742 / 268 / 431 | Quarantine / isolation / hospital | — | — | warn |

### Animals by class

`animals.byClass` · type `chart` · size `md` · id `byClass`

_shown by default._

**donut chart** · 6 series · total 1,04,382

| Series | Value | Share |
|---|---|---|
| Mammal | 18,240 | 17% |
| Bird | 21,460 | 21% |
| Reptile | 9,870 | 9% |
| Amphibian | 4,310 | 4% |
| Fish | 26,480 | 25% |
| Invertebrate | 24,022 | 23% |

### Sex distribution

`animals.bySex` · type `chart` · size `md` · id `bySex`

_shown by default._

**bar chart** · 4 series · total 1,04,382

| Series | Value | Share |
|---|---|---|
| Male | 46,120 | 44% |
| Female | 48,310 | 46% |
| Unknown | 5,240 | 5% |
| Unsexed | 4,712 | 5% |

### Life-stage distribution

`animals.byLifeStage` · type `chart` · size `md` · id `byLifeStage`

**bar chart** · 5 series · total 1,04,382

| Series | Value | Share |
|---|---|---|
| Infant | 6,120 | 6% |
| Juvenile | 14,830 | 14% |
| Sub-adult | 19,210 | 18% |
| Adult | 57,840 | 55% |
| Geriatric | 6,382 | 6% |

### Wild-born vs captive-born

`animals.byOrigin` · type `chart` · size `md` · id `byOrigin`

**donut chart** · 2 series · total 1,04,382

| Series | Value | Share |
|---|---|---|
| Wild-born | 41,870 | 40% |
| Captive-born | 62,512 | 60% |

### Native vs exotic species

`animals.nativeExotic` · type `chart` · size `md` · id `nativeExotic`

**donut chart** · 2 series · total 2,143

| Series | Value | Share |
|---|---|---|
| Native species | 1,382 | 64% |
| Exotic species | 761 | 36% |

### Health status mix

`animals.healthStatusMix` · type `chart` · size `md` · id `healthStatusMix`

**donut chart** · 5 series · total 800

| Series | Value | Share |
|---|---|---|
| Healthy | 550 | 69% |
| Under observation | 90 | 11% |
| Quarantine | 84 | 11% |
| Under treatment | 60 | 8% |
| Critical | 16 | 2% |

### Identification status

`animals.identificationStatus` · type `chart` · size `md` · id `identificationStatus`

**donut chart** · 6 series · total 800

| Series | Value | Share |
|---|---|---|
| Microchip | 354 | 44% |
| Photo ID | 133 | 17% |
| Leg ring | 106 | 13% |
| Ear tag | 101 | 13% |
| Tattoo | 58 | 7% |
| None | 48 | 6% |

### Conservation status

`animals.conservationStatus` · type `list` · size `md` · id `conservationStatus`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Endangered species | 318 species | EN | bad |
| Threatened species | 496 species | VU/NT | warn |
| CITES-listed species | 604 species | CITES | neutral |

### New arrivals

`animals.newArrivals` · type `list` · size `md` · id `newArrivals`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Rhea (Zebra Shark) | Forest Department rescue · 28 Aug 2026 | Wild-born | neutral |
| Lakshmi (Red Panda) | Rehabilitation intake · 14 Jul 2026 | Captive-born | neutral |
| Sona (Dhole) | Seizure — wildlife crime · 13 Jul 2026 | Wild-born | neutral |
| Pinky (Bengal Tiger) | Rehabilitation intake · 17 Jul 2026 | Wild-born | neutral |
| Ila (Emperor Scorpion) | Captive birth — in-house · 07 Aug 2026 | Captive-born | neutral |
| Moti (King Cobra) | Road accident rescue · 31 Jul 2026 | Captive-born | neutral |
| Dev (Clouded Leopard) | Seizure — wildlife crime · 20 Jul 2026 | Captive-born | neutral |
| Kavi (Asian Elephant) | Forest Department rescue · 14 Jul 2026 | Wild-born | neutral |

### Upcoming planned movements

`animals.plannedMovements` · type `list` · size `md` · id `plannedMovements`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Bengal Tiger — PAIR-001 | Planned move to ISO-125 · 28 Aug 2026 | Pregnant/Gravid | neutral |
| Snow Leopard — PAIR-002 | Planned move to HER-151 · 17 Aug 2026 | Pregnant/Gravid | neutral |
| Asian Elephant — PAIR-003 | Planned move to SMA-075 · 05 Sept 2026 | Pregnant/Gravid | neutral |
| Himalayan Black Bear — PAIR-004 | Planned move to NOC-065 · 13 Dec 2026 | Incubating | neutral |
| Golden Jackal — PAIR-005 | Planned move to PRI-078 · 23 Dec 2026 | Paired | neutral |
| Rhesus Macaque — PAIR-006 | Planned move to INV-115 · 02 Feb 2027 | Incubating | neutral |
| Blackbuck — PAIR-007 | Planned move to SMA-073 · 09 Nov 2026 | Paired | neutral |

### Births, deaths and transfers

`animals.recentEvents` · type `timeline` · size `lg` · id `recentEvents`

_shown by default._

| Date | Event | Detail |
|---|---|---|
| 30 Aug 2026 | 612 births recorded (30 d) | Highest in Aviary Complex and Herbivores sections |
| 29 Aug 2026 | 289 mortalities recorded (30 d) | All necropsies completed or in progress |
| 28 Aug 2026 | 874 inter-enclosure transfers | Includes 96 inter-site movements |
| 26 Aug 2026 | 11 animals reported missing | 3 confirmed escapes — all recovered |

### Animals by site

`animals.bySite` · type `table` · size `lg` · id `bySite`

_shown by default._

| Site | Animals | Capacity | Occupancy % |
|---|---|---|---|
| Riverside Rescue Centre | 197 | 486 | 41% |
| Hilltop Rehabilitation Campus | 184 | 431 | 43% |
| Coastal Marine Facility | 138 | 280 | 49% |
| Central Quarantine Complex | 187 | 444 | 42% |
| Grassland Conservation Park | 169 | 402 | 42% |
| Wetland Bird Sanctuary Unit | 159 | 412 | 39% |
| Forest Edge Care Facility | 152 | 488 | 31% |
| Highland Carnivore Centre | 88 | 301 | 29% |
| Desert Species Station | 127 | 306 | 42% |
| Island Species Reserve | 99 | 304 | 33% |

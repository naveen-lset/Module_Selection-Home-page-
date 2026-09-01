# Transport & Logistics

| | |
|---|---|
| Key | `transport` |
| Route | `/topic/transport` |
| Kind | Topic dashboard |
| Icon | `Truck` |
| Accent | `#4B5563` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | kpi ×1, chart ×3, list ×3 |

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Vehicles available | kpi | sm | `transport.availability` |
| 2 | Vehicle status | chart | md | `transport.statusMix` |
| 3 | Active trips | list | md | `transport.activeTrips` |
| 4 | Fitness & insurance expiry | list | md | `transport.documentExpiry` |
| 5 | Breakdowns & maintenance | list | md | `transport.breakdowns` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Vehicles available | kpi | sm | `transport.availability` | yes |
| Vehicle status | chart | md | `transport.statusMix` | yes |
| Fleet composition | chart | md | `transport.kindMix` | — |
| Fuel use by site | chart | md | `transport.fuelUse` | — |
| Active trips | list | md | `transport.activeTrips` | yes |
| Fitness & insurance expiry | list | md | `transport.documentExpiry` | yes |
| Breakdowns & maintenance | list | md | `transport.breakdowns` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Vehicles available

`transport.availability` · type `kpi` · size `sm` · id `availability`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 16 / 40 | Vehicles available | — | — | good |

### Vehicle status

`transport.statusMix` · type `chart` · size `md` · id `statusMix`

_shown by default._

**donut chart** · 4 series · total 40

| Series | Value | Share |
|---|---|---|
| Available | 16 | 40% |
| On trip | 14 | 35% |
| Under maintenance | 8 | 20% |
| Breakdown | 2 | 5% |

### Fleet composition

`transport.kindMix` · type `chart` · size `md` · id `kindMix`

**bar chart** · 5 series · total 40

| Series | Value | Share |
|---|---|---|
| Staff bus | 10 | 25% |
| Utility pickup | 10 | 25% |
| Feed truck | 8 | 20% |
| Animal ambulance | 8 | 20% |
| Cold-chain van | 4 | 10% |

### Fuel use by site

`transport.fuelUse` · type `chart` · size `md` · id `fuelUse`

**bar chart** · unit: l/day · 10 series · total 1,548

| Series | Value | Share |
|---|---|---|
| Riverside | 81 | 5% |
| Hilltop | 226 | 15% |
| Coastal | 196 | 13% |
| Central | 144 | 9% |
| Grassland | 233 | 15% |
| Wetland | 122 | 8% |
| Forest | 331 | 21% |
| Highland | 21 | 1% |
| Desert | 140 | 9% |
| Island | 54 | 3% |

### Active trips

`transport.activeTrips` · type `list` · size `md` · id `activeTrips`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| MH-26-CD-6054 — Cold-chain van | Rescue call-out · Hilltop | On trip | neutral |
| MH-38-EF-4454 — Staff bus | Staff shuttle · Forest | On trip | neutral |
| MH-45-AB-4705 — Staff bus | Inter-site material movement · Hilltop | On trip | neutral |
| MH-29-GH-6018 — Staff bus | Animal transfer · Island | On trip | neutral |
| MH-13-CD-4801 — Cold-chain van | Feed collection · Hilltop | On trip | neutral |
| MH-12-AB-6417 — Animal ambulance | Feed collection · Island | On trip | neutral |
| MH-38-CD-8898 — Staff bus | Staff shuttle · Hilltop | On trip | neutral |
| MH-28-GH-7778 — Animal ambulance | Staff shuttle · Coastal | On trip | neutral |

### Fitness & insurance expiry

`transport.documentExpiry` · type `list` · size `md` · id `documentExpiry`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| MH-45-AB-4705 — Staff bus | Fitness expired · insurance 190 d | — | bad |
| MH-16-CD-2678 — Feed truck | Fitness 5 d · insurance 276 d | — | neutral |
| MH-35-GH-1711 — Staff bus | Fitness 6 d · insurance 400 d | — | neutral |
| MH-13-GH-4019 — Utility pickup | Fitness 12 d · insurance 97 d | — | neutral |
| MH-37-GH-5385 — Feed truck | Fitness 14 d · insurance 381 d | — | neutral |
| MH-31-EF-5173 — Utility pickup | Fitness 46 d · insurance 24 d | — | neutral |
| MH-22-GH-4789 — Staff bus | Fitness 53 d · insurance 141 d | — | neutral |

### Breakdowns & maintenance

`transport.breakdowns` · type `list` · size `md` · id `breakdowns`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| MH-31-CD-9469 — Under maintenance | Animal ambulance · Forest | — | warn |
| MH-20-CD-5408 — Under maintenance | Animal ambulance · Grassland | — | warn |
| MH-31-EF-5173 — Under maintenance | Utility pickup · Grassland | — | warn |
| MH-23-CD-6036 — Under maintenance | Animal ambulance · Desert | — | warn |
| MH-34-GH-4400 — Under maintenance | Staff bus · Hilltop | — | warn |
| MH-12-EF-1416 — Under maintenance | Feed truck · Desert | — | warn |

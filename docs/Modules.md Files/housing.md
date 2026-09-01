# Enclosures & Housing

| | |
|---|---|
| Key | `housing` |
| Route | `/housing` |
| Kind | Topic dashboard |
| Icon | `Building2` |
| Accent | `#2563EB` |
| Widgets | 10 in catalog, 6 shown by default |
| Widget types | kpi ×1, gauge ×1, chart ×3, alertFeed ×1, list ×2, table ×2 |

## Roles

**Priority module for:** Management, Keeper / Animal Care.

**Role-specific default layouts:** Keeper / Animal Care. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Total enclosures | kpi | sm | `housing.enclosureTotals` |
| 2 | Biosecurity compliance | gauge | md | `housing.biosecurity` |
| 3 | Enclosure status | chart | md | `housing.statusBreakdown` |
| 4 | Overcrowding alerts | alertFeed | lg | `housing.overcrowdingAlerts` |
| 5 | Inspections due | list | md | `housing.inspectionsDue` |
| 6 | Site directory | table | lg | `housing.siteDirectory` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Total enclosures | kpi | sm | `housing.enclosureTotals` | yes |
| Biosecurity compliance | gauge | md | `housing.biosecurity` | yes |
| Enclosure status | chart | md | `housing.statusBreakdown` | yes |
| Occupancy by site | chart | md | `housing.occupancyBySite` | — |
| Lowest section welfare scores | chart | md | `housing.auditScores` | — |
| Overcrowding alerts | alertFeed | lg | `housing.overcrowdingAlerts` | yes |
| Inspections due | list | md | `housing.inspectionsDue` | yes |
| Structural repair flags | list | md | `housing.structuralFlags` | — |
| Site directory | table | lg | `housing.siteDirectory` | yes |
| Environment & hygiene outliers | table | lg | `housing.environmentOutliers` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Total enclosures

`housing.enclosureTotals` · type `kpi` · size `sm` · id `enclosureTotals`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,840 | Total enclosures | 1,596 occupied | flat | neutral |

### Biosecurity compliance

`housing.biosecurity` · type `gauge` · size `md` · id `biosecurity`

_shown by default · default for Keeper / Animal Care._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 94 | 100 | 94% | Biosecurity compliance | % | good |

### Enclosure status

`housing.statusBreakdown` · type `chart` · size `md` · id `statusBreakdown`

_shown by default._

**donut chart** · 3 series · total 1,840

| Series | Value | Share |
|---|---|---|
| Occupied | 1,596 | 87% |
| Vacant | 172 | 9% |
| Under maintenance | 72 | 4% |

### Occupancy by site

`housing.occupancyBySite` · type `chart` · size `md` · id `occupancyBySite`

**bar chart** · unit: % · 10 series · total 391

| Series | Value | Share |
|---|---|---|
| Riverside | 41 | 10% |
| Hilltop | 43 | 11% |
| Coastal | 49 | 13% |
| Central | 42 | 11% |
| Grassland | 42 | 11% |
| Wetland | 39 | 10% |
| Forest | 31 | 8% |
| Highland | 29 | 7% |
| Desert | 42 | 11% |
| Island | 33 | 8% |

### Lowest section welfare scores

`housing.auditScores` · type `chart` · size `md` · id `auditScores`

**bar chart** · unit: % · 8 series · total 564

| Series | Value | Share |
|---|---|---|
| Crocodile Enclave | 68 | 12% |
| Elephant Care | 70 | 12% |
| Reptile House | 70 | 12% |
| Quarantine Wing | 70 | 12% |
| Invertebrate House | 71 | 13% |
| Herbivores | 71 | 13% |
| Elephant Care | 71 | 13% |
| Nocturnal House | 73 | 13% |

### Overcrowding alerts

`housing.overcrowdingAlerts` · type `alertFeed` · size `lg` · id `overcrowdingAlerts`

_shown by default · default for Keeper / Animal Care._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Housing | REP-032 — 38 animals against capacity 33 | 1 d |
| high | Housing | CRO-103 — 18 animals against capacity 16 | 1 d |
| high | Housing | AMP-110 — 26 animals against capacity 23 | 1 d |
| high | Housing | INV-115 — 15 animals against capacity 13 | 1 d |

### Inspections due

`housing.inspectionsDue` · type `list` · size `md` · id `inspectionsDue`

_shown by default · default for Keeper / Animal Care._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| REP-100 — Reptile House Enclosure 4 | Next inspection 11 Aug 2026 | Vacant | neutral |
| AVI-158 — Aviary Complex Enclosure 1 | Next inspection 11 Aug 2026 | Vacant | neutral |
| AVI-025 — Aviary Complex Enclosure 4 | Next inspection 14 Aug 2026 | Occupied | neutral |
| ELE-157 — Elephant Care Enclosure 5 | Next inspection 17 Aug 2026 | Under maintenance | neutral |
| LAR-004 — Large Carnivores Enclosure 4 | Next inspection 19 Aug 2026 | Quarantine | neutral |
| NEO-061 — Neonatal & Hand-rearing Enclosure 1 | Next inspection 19 Aug 2026 | Under maintenance | neutral |
| CRO-102 — Crocodile Enclave Enclosure 2 | Next inspection 19 Aug 2026 | Vacant | neutral |
| AMP-044 — Amphibian Unit Enclosure 3 | Next inspection 20 Aug 2026 | Occupied | neutral |

### Structural repair flags

`housing.structuralFlags` · type `list` · size `md` · id `structuralFlags`

_default for Keeper / Animal Care._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| REP-031 — structural repair needed | Hilltop Rehabilitation Campus · 2 open issues | — | warn |
| CRO-035 — structural repair needed | Hilltop Rehabilitation Campus · 3 open issues | — | warn |
| AMP-044 — structural repair needed | Hilltop Rehabilitation Campus · 0 open issues | — | warn |
| ISO-055 — structural repair needed | Coastal Marine Facility · 0 open issues | — | warn |
| HOS-058 — structural repair needed | Coastal Marine Facility · 0 open issues | — | warn |
| NEO-063 — structural repair needed | Central Quarantine Complex · 1 open issues | — | warn |
| NEO-064 — structural repair needed | Central Quarantine Complex · 0 open issues | — | warn |
| SMA-073 — structural repair needed | Central Quarantine Complex · 2 open issues | — | warn |

### Site directory

`housing.siteDirectory` · type `table` · size `lg` · id `siteDirectory`

_shown by default._

| Site | Region | Sections | Enclosures | Alerts | Score |
|---|---|---|---|---|---|
| Riverside Rescue Centre | North Zone | 6 | 25 | 0 | 85% |
| Hilltop Rehabilitation Campus | Himalayan Zone | 5 | 19 | 4 | 79% |
| Coastal Marine Facility | West Coast | 4 | 16 | 12 | 71% |
| Central Quarantine Complex | Central Zone | 5 | 20 | 3 | 90% |
| Grassland Conservation Park | Deccan Zone | 4 | 16 | 5 | 96% |
| Wetland Bird Sanctuary Unit | East Zone | 4 | 17 | 8 | 73% |
| Forest Edge Care Facility | Western Ghats | 5 | 20 | 2 | 80% |
| Highland Carnivore Centre | North-East Zone | 4 | 15 | 3 | 88% |
| Desert Species Station | Arid Zone | 4 | 17 | 13 | 77% |
| Island Species Reserve | Andaman Zone | 4 | 15 | 15 | 94% |

### Environment & hygiene outliers

`housing.environmentOutliers` · type `table` · size `lg` · id `environmentOutliers`

_default for Keeper / Animal Care._

| Enclosure | Temp °C | Humidity % | Water quality | Hygiene |
|---|---|---|---|---|
| LAR-001 | 28.7 | 76 | N/A | 67% |
| SMA-006 | 20.1 | 59 | N/A | 65% |
| SMA-009 | 26.2 | 42 | N/A | 67% |
| PRI-012 | 26.6 | 82 | N/A | 65% |
| PRI-013 | 21.4 | 86 | N/A | 64% |
| HER-014 | 29.5 | 78 | Good | 65% |
| HER-015 | 26 | 61 | N/A | 63% |
| ELE-019 | 24.8 | 84 | N/A | 66% |

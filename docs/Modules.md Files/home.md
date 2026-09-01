# Command Centre

| | |
|---|---|
| Key | `home` |
| Route | `/` |
| Kind | Home dashboard |
| Icon | `Activity` |
| Accent | `#0F766E` |
| Widgets | 16 in catalog, 4 shown by default |
| Widget types | kpi ×15, gauge ×1 |

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** Management, Veterinarian, Biologist, Paravet, Keeper / Animal Care, Nutritionist, Pharmacist, Maintenance / Engineering, Security, Admin / Finance, HR / People, Procurement. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Total animals | kpi | sm | `home.animalsTotal` |
| 2 | Under treatment | kpi | sm | `home.underTreatment` |
| 3 | Critical animal alerts | kpi | sm | `home.criticalAlerts` |
| 4 | Facility health score | gauge | md | `home.facilityScore` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Total animals | kpi | sm | `home.animalsTotal` | yes |
| Total species | kpi | sm | `home.speciesTotal` | — |
| Under treatment | kpi | sm | `home.underTreatment` | yes |
| Births / deaths (30 d) | kpi | sm | `home.birthsDeaths` | — |
| Enclosures occupied | kpi | sm | `home.enclosuresOccupied` | — |
| Critical animal alerts | kpi | sm | `home.criticalAlerts` | yes |
| Staff present | kpi | sm | `home.staffPresent` | — |
| Open maintenance tickets | kpi | sm | `home.openTickets` | — |
| Non-working critical equipment | kpi | sm | `home.equipmentDown` | — |
| Feed stock availability | kpi | sm | `home.feedStock` | — |
| Pharmacy stock alerts | kpi | sm | `home.pharmacyAlerts` | — |
| Water consumption | kpi | sm | `home.waterUse` | — |
| Electricity consumption | kpi | sm | `home.electricityUse` | — |
| Active safety incidents | kpi | sm | `home.safetyIncidents` | — |
| Pending approvals | kpi | sm | `home.pendingApprovals` | — |
| Facility health score | gauge | md | `home.facilityScore` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Total animals

`home.animalsTotal` · type `kpi` · size `sm` · id `animalsTotal`

_shown by default · default for Management, Veterinarian, Biologist, Paravet, Nutritionist._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,04,382 | Total animals | +1,428 (30 d) | up | neutral |

### Total species

`home.speciesTotal` · type `kpi` · size `sm` · id `speciesTotal`

_default for Biologist._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 2,143 | Total species | 486 subspecies | flat | neutral |

### Under treatment

`home.underTreatment` · type `kpi` · size `sm` · id `underTreatment`

_shown by default · default for Management, Veterinarian, Paravet, Keeper / Animal Care, Nutritionist, Pharmacist._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,186 | Animals under treatment | 47 critical | up | warn |

### Births / deaths (30 d)

`home.birthsDeaths` · type `kpi` · size `sm` · id `birthsDeaths`

_default for Biologist._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 612 / 289 | Births / deaths (30 d) | — | up | neutral |

### Enclosures occupied

`home.enclosuresOccupied` · type `kpi` · size `sm` · id `enclosuresOccupied`

_default for Keeper / Animal Care._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,596 / 1,840 | Enclosures occupied | — | — | neutral |

### Critical animal alerts

`home.criticalAlerts` · type `kpi` · size `sm` · id `criticalAlerts`

_shown by default · default for Management, Veterinarian, Biologist, Paravet, Keeper / Animal Care, Nutritionist, Pharmacist, Security._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 12 | Critical animal alerts | — | up | bad |

### Staff present

`home.staffPresent` · type `kpi` · size `sm` · id `staffPresent`

_default for Management, Security, HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 2,617 | Staff present today | 247 on leave | flat | neutral |

### Open maintenance tickets

`home.openTickets` · type `kpi` · size `sm` · id `openTickets`

_default for Management, Maintenance / Engineering, Admin / Finance, Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 486 | Open maintenance tickets | 92 overdue | — | warn |

### Non-working critical equipment

`home.equipmentDown` · type `kpi` · size `sm` · id `equipmentDown`

_default for Maintenance / Engineering, Security._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 14 | Non-working critical equipment | — | — | bad |

### Feed stock availability

`home.feedStock` · type `kpi` · size `sm` · id `feedStock`

_default for Paravet, Keeper / Animal Care, Nutritionist, Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 11 days | Feed stock cover | — | down | warn |

### Pharmacy stock alerts

`home.pharmacyAlerts` · type `kpi` · size `sm` · id `pharmacyAlerts`

_default for Veterinarian, Pharmacist, Admin / Finance, Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 63 | Pharmacy stock alerts | — | — | warn |

### Water consumption

`home.waterUse` · type `kpi` · size `sm` · id `waterUse`

_default for Maintenance / Engineering._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 4,820 kl | Water consumption (today) | +4% vs target | up | neutral |

### Electricity consumption

`home.electricityUse` · type `kpi` · size `sm` · id `electricityUse`

_default for Maintenance / Engineering._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 96,400 kWh | Electricity (today) | +7% vs target | up | neutral |

### Active safety incidents

`home.safetyIncidents` · type `kpi` · size `sm` · id `safetyIncidents`

_default for Management, Security, HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 6 | Active safety incidents | — | — | bad |

### Pending approvals

`home.pendingApprovals` · type `kpi` · size `sm` · id `pendingApprovals`

_default for Management, Pharmacist, Admin / Finance, HR / People, Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 74 | Pending approvals | — | — | warn |

### Facility health score

`home.facilityScore` · type `gauge` · size `md` · id `facilityScore`

_shown by default · default for Management, Admin / Finance, HR / People._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 87 | 100 | 87% | Overall facility health score | % | good |

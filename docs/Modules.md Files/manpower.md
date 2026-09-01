# Manpower

| | |
|---|---|
| Key | `manpower` |
| Route | `/topic/manpower` |
| Kind | Topic dashboard |
| Icon | `Users` |
| Accent | `#0F766E` |
| Widgets | 10 in catalog, 6 shown by default |
| Widget types | kpi ×4, gauge ×1, chart ×3, list ×1, table ×1 |

## Roles

**Priority module for:** HR / People.

**Role-specific default layouts:** HR / People. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Total manpower | kpi | sm | `manpower.total` |
| 2 | Present today | kpi | sm | `manpower.attendanceToday` |
| 3 | Vacant positions | kpi | sm | `manpower.vacancies` |
| 4 | Vets / biologists / paravets | kpi | md | `manpower.clinicalTeam` |
| 5 | Department-wise headcount | chart | md | `manpower.byDepartment` |
| 6 | Role-wise strength | table | lg | `manpower.roleTable` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Total manpower | kpi | sm | `manpower.total` | yes |
| Present today | kpi | sm | `manpower.attendanceToday` | yes |
| Vacant positions | kpi | sm | `manpower.vacancies` | yes |
| Vets / biologists / paravets | kpi | md | `manpower.clinicalTeam` | yes |
| Keeper-to-enclosure ratio | gauge | md | `manpower.ratios` | — |
| Department-wise headcount | chart | md | `manpower.byDepartment` | yes |
| Shift distribution | chart | md | `manpower.shiftMix` | — |
| Overtime by department | chart | md | `manpower.overtime` | — |
| Certifications expired | list | md | `manpower.certifications` | — |
| Role-wise strength | table | lg | `manpower.roleTable` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Total manpower

`manpower.total` · type `kpi` · size `sm` · id `total`

_shown by default · default for HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 3,012 | Total manpower | 137 vacancies | flat | neutral |

### Present today

`manpower.attendanceToday` · type `kpi` · size `sm` · id `attendanceToday`

_shown by default · default for HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 2,617 | Present today | 148 absent | — | good |

### Vacant positions

`manpower.vacancies` · type `kpi` · size `sm` · id `vacancies`

_shown by default · default for HR / People._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 137 | Vacant positions | — | — | warn |

### Vets / biologists / paravets

`manpower.clinicalTeam` · type `kpi` · size `md` · id `clinicalTeam`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 118 / 64 / 186 | Vets / biologists / paravets | — | — | neutral |

### Keeper-to-enclosure ratio

`manpower.ratios` · type `gauge` · size `md` · id `ratios`

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 1042 | 1840 | 57% | Keeper-to-enclosure ratio (target 1:3) | — | warn |

### Department-wise headcount

`manpower.byDepartment` · type `chart` · size `md` · id `byDepartment`

_shown by default · default for HR / People._

**bar chart** · unit: staff · 12 series · total 6,712

| Series | Value | Share |
|---|---|---|
| Administration | 972 | 14% |
| Veterinary | 1,026 | 15% |
| Conservation | 518 | 8% |
| Animal | 950 | 14% |
| Nutrition | 454 | 7% |
| Pharmacy | 784 | 12% |
| Engineering | 109 | 2% |
| Safety | 814 | 12% |
| Finance | 71 | 1% |
| Human | 182 | 3% |
| Procurement | 411 | 6% |
| Housekeeping | 421 | 6% |

### Shift distribution

`manpower.shiftMix` · type `chart` · size `md` · id `shiftMix`

_default for HR / People._

**donut chart** · 4 series · total 250

| Series | Value | Share |
|---|---|---|
| Evening | 80 | 32% |
| Morning | 72 | 29% |
| General | 62 | 25% |
| Night | 36 | 14% |

### Overtime by department

`manpower.overtime` · type `chart` · size `md` · id `overtime`

**bar chart** · unit: ₹ lakh · 12 series · total 85

| Series | Value | Share |
|---|---|---|
| Administration | 4 | 5% |
| Veterinary | 2 | 2% |
| Conservation | 15 | 18% |
| Animal | 11 | 13% |
| Nutrition | 18 | 21% |
| Pharmacy | 14 | 16% |
| Engineering | 1 | 1% |
| Safety | 1 | 1% |
| Finance | 1 | 1% |
| Human | 11 | 13% |
| Procurement | 4 | 5% |
| Housekeeping | 3 | 4% |

### Certifications expired

`manpower.certifications` · type `list` · size `md` · id `certifications`

_default for HR / People._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Vikas Patil — certification expired | Senior Animal Keeper · Grassland | — | warn |
| Rahul Thomas — certification expired | Security Supervisor · Grassland | — | warn |
| Rahul Iyer — certification expired | Animal Nutritionist · Grassland | — | warn |
| Lakshmi Gupta — certification expired | Pharmacy In-charge · Island | — | warn |
| Rahul Khan — certification expired | Operations Head · Riverside | — | warn |
| Rahul Patil — certification expired | Security Supervisor · Hilltop | — | warn |
| Sneha Das — certification expired | Pharmacy In-charge · Riverside | — | warn |
| Divya Sharma — certification expired | Senior Animal Keeper · Forest | — | warn |

### Role-wise strength

`manpower.roleTable` · type `table` · size `lg` · id `roleTable`

_shown by default._

| Role | Department | Sample count | Facility count |
|---|---|---|---|
| Management | Administration | 7 | 84 |
| Veterinarian | Veterinary Services | 22 | 264 |
| Biologist | Conservation & Research | 13 | 156 |
| Paravet | Veterinary Services | 24 | 288 |
| Keeper / Animal Care | Animal Care | 70 | 840 |
| Nutritionist | Nutrition & Diet | 13 | 156 |
| Pharmacist | Pharmacy | 8 | 96 |
| Maintenance / Engineering | Engineering | 35 | 420 |
| Security | Safety & Security | 28 | 336 |
| Admin / Finance | Finance | 14 | 168 |
| HR / People | Human Resources | 5 | 60 |
| Procurement | Procurement & Stores | 11 | 132 |

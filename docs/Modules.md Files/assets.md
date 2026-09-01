# Assets

| | |
|---|---|
| Key | `assets` |
| Route | `/topic/assets` |
| Kind | Topic dashboard |
| Icon | `Boxes` |
| Accent | `#4B5563` |
| Widgets | 9 in catalog, 6 shown by default |
| Widget types | kpi ×1, gauge ×1, alertFeed ×1, chart ×3, list ×2, table ×1 |

## Roles

**Priority module for:** Maintenance / Engineering.

**Role-specific default layouts:** Maintenance / Engineering. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Total assets | kpi | sm | `assets.total` |
| 2 | Assets under valid AMC | gauge | md | `assets.warrantyAmc` |
| 3 | Non-working critical assets | alertFeed | lg | `assets.nonWorkingCritical` |
| 4 | Assets by category | chart | md | `assets.categoryMix` |
| 5 | Working status | chart | md | `assets.statusMix` |
| 6 | Preventive maintenance due | list | md | `assets.pmDue` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Total assets | kpi | sm | `assets.total` | yes |
| Assets under valid AMC | gauge | md | `assets.warrantyAmc` | yes |
| Non-working critical assets | alertFeed | lg | `assets.nonWorkingCritical` | yes |
| Assets by category | chart | md | `assets.categoryMix` | yes |
| Working status | chart | md | `assets.statusMix` | yes |
| Asset value by site | chart | md | `assets.valueBySite` | — |
| Preventive maintenance due | list | md | `assets.pmDue` | yes |
| Physical verification pending | list | md | `assets.unverified` | — |
| Asset register | table | lg | `assets.register` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Total assets

`assets.total` · type `kpi` · size `sm` · id `total`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 5,720 | Total assets | 1430 critical | flat | neutral |

### Assets under valid AMC

`assets.warrantyAmc` · type `gauge` · size `md` · id `warrantyAmc`

_shown by default · default for Maintenance / Engineering._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 145 | 220 | 66% | Assets under valid AMC | — | warn |

### Non-working critical assets

`assets.nonWorkingCritical` · type `alertFeed` · size `lg` · id `nonWorkingCritical`

_shown by default · default for Maintenance / Engineering._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Assets | Lab equipment unit 1 non-working — Desert (custodian: Veterinary Officer) | 1 d |
| critical | Assets | Enclosure fitting unit 2 non-working — Coastal (custodian: Kitchen Supervisor) | 1 d |
| critical | Assets | IT equipment unit 3 non-working — Wetland (custodian: Site Engineer) | 1 d |
| critical | Assets | Kitchen equipment unit 4 non-working — Riverside (custodian: Security Supervisor) | 1 d |
| critical | Assets | Pump/Motor unit 5 non-working — Hilltop (custodian: Security Supervisor) | 1 d |
| critical | Assets | Pump/Motor unit 6 non-working — Coastal (custodian: Security Supervisor) | 1 d |

### Assets by category

`assets.categoryMix` · type `chart` · size `md` · id `categoryMix`

_shown by default._

**donut chart** · 7 series · total 220

| Series | Value | Share |
|---|---|---|
| Lab equipment | 41 | 19% |
| Pump/Motor | 38 | 17% |
| Medical equipment | 36 | 16% |
| Kitchen equipment | 34 | 15% |
| IT equipment | 29 | 13% |
| Enclosure fitting | 22 | 10% |
| Vehicle | 20 | 9% |

### Working status

`assets.statusMix` · type `chart` · size `md` · id `statusMix`

_shown by default · default for Maintenance / Engineering._

**bar chart** · 5 series · total 220

| Series | Value | Share |
|---|---|---|
| Working | 151 | 69% |
| Non-working | 24 | 11% |
| Partially working | 19 | 9% |
| Under repair | 14 | 6% |
| Retired | 12 | 5% |

### Asset value by site

`assets.valueBySite` · type `chart` · size `md` · id `valueBySite`

**bar chart** · unit: ₹ lakh · 10 series · total 2,786

| Series | Value | Share |
|---|---|---|
| Riverside | 222 | 8% |
| Hilltop | 301 | 11% |
| Coastal | 284 | 10% |
| Central | 227 | 8% |
| Grassland | 322 | 12% |
| Wetland | 314 | 11% |
| Forest | 233 | 8% |
| Highland | 330 | 12% |
| Desert | 246 | 9% |
| Island | 307 | 11% |

### Preventive maintenance due

`assets.pmDue` · type `list` · size `md` · id `pmDue`

_shown by default · default for Maintenance / Engineering._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Medical equipment unit 105 | Preventive maintenance overdue by 24 d | Fair | bad |
| Lab equipment unit 110 | Preventive maintenance overdue by 24 d | Good | bad |
| Pump/Motor unit 161 | Preventive maintenance overdue by 24 d | Fair | bad |
| Kitchen equipment unit 72 | Preventive maintenance overdue by 23 d | Poor | bad |
| Lab equipment unit 178 | Preventive maintenance overdue by 23 d | Fair | bad |
| Pump/Motor unit 86 | Preventive maintenance overdue by 22 d | Fair | bad |
| IT equipment unit 164 | Preventive maintenance overdue by 22 d | Fair | bad |
| Medical equipment unit 104 | Preventive maintenance overdue by 21 d | Good | bad |

### Physical verification pending

`assets.unverified` · type `list` · size `md` · id `unverified`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Kitchen equipment unit 4 — physical verification pending | Riverside · QR QR-940468 | — | warn |
| Medical equipment unit 11 — physical verification pending | Grassland · QR QR-744997 | — | warn |
| IT equipment unit 13 — physical verification pending | Forest · QR QR-794242 | — | warn |
| IT equipment unit 20 — physical verification pending | Grassland · QR QR-457900 | — | warn |
| IT equipment unit 21 — physical verification pending | Forest · QR QR-739388 | — | warn |
| Enclosure fitting unit 29 — physical verification pending | Coastal · QR QR-805748 | — | warn |
| Medical equipment unit 39 — physical verification pending | Highland · QR QR-853136 | — | warn |

### Asset register

`assets.register` · type `table` · size `lg` · id `register`

| Asset | Category | Site | Status | Value ₹ |
|---|---|---|---|---|
| Lab equipment unit 1 | Lab equipment | Desert | Non-working | 5,66,645 |
| Enclosure fitting unit 2 | Enclosure fitting | Coastal | Non-working | 15,86,359 |
| IT equipment unit 3 | IT equipment | Wetland | Non-working | 9,39,183 |
| Kitchen equipment unit 4 | Kitchen equipment | Riverside | Non-working | 19,85,469 |
| Pump/Motor unit 5 | Pump/Motor | Hilltop | Non-working | 2,36,895 |
| Pump/Motor unit 6 | Pump/Motor | Coastal | Non-working | 21,73,074 |
| Lab equipment unit 7 | Lab equipment | Wetland | Working | 2,07,446 |
| Enclosure fitting unit 8 | Enclosure fitting | Island | Working | 10,17,137 |

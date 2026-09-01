# Alerts & Key Indicators

| | |
|---|---|
| Key | `alerts` |
| Route | `/topic/alerts` |
| Kind | Topic dashboard |
| Icon | `BellRing` |
| Accent | `#B91C1C` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | alertFeed ×1, list ×2, chart ×2, table ×1 |

## Roles

**Priority module for:** Management, Veterinarian, Security, Admin / Finance.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | All alerts | alertFeed | lg | `alerts.feed` |
| 2 | Critical alerts | list | md | `alerts.criticalList` |
| 3 | Alerts by domain | chart | md | `alerts.domainMix` |
| 4 | Alerts by severity | chart | md | `alerts.severityMix` |
| 5 | Overdue items | table | lg | `alerts.overdueTable` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| All alerts | alertFeed | lg | `alerts.feed` | yes |
| Critical alerts | list | md | `alerts.criticalList` | yes |
| Budget overrun flags | list | md | `alerts.budgetFlags` | — |
| Alerts by domain | chart | md | `alerts.domainMix` | yes |
| Alerts by severity | chart | md | `alerts.severityMix` | yes |
| Overdue items | table | lg | `alerts.overdueTable` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### All alerts

`alerts.feed` · type `alertFeed` · size `lg` · id `feed`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Medical | Critical case — Bengal Tiger ANM-0042 not responding to treatment | 12 min |
| critical | Medical | Suspected infectious disease in Quarantine Wing — samples sent | 9 h |
| critical | Animal Collection | Animal reported missing — Blackbuck, Grassland Park | 4 d |
| high | Housing | Enclosure CAR-014 occupancy exceeds capacity by 6 | 2 d |
| high | Housing | Biosecurity non-compliance flagged in Isolation Wing | 2 h |
| high | Pharmacy | Ketamine HCl stock below reorder level | 12 min |
| medium | Pharmacy | 10 medicine batches expiring within 30 days | 1 d |
| high | Diet | Feed stock cover down to 11 days — fresh produce | 1 d |
| critical | Maintenance | Water pump failure — Coastal Marine Facility | 48 min |
| high | Maintenance | 92 work orders overdue across sites | 5 h |

### Critical alerts

`alerts.criticalList` · type `list` · size `md` · id `criticalList`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Critical case — Bengal Tiger ANM-0042 not responding to treatment | Medical · raised 12 min ago | Critical | bad |
| Suspected infectious disease in Quarantine Wing — samples sent | Medical · raised 9 h ago | Critical | bad |
| Animal reported missing — Blackbuck, Grassland Park | Animal Collection · raised 4 d ago | Critical | bad |
| Water pump failure — Coastal Marine Facility | Maintenance · raised 48 min ago | Critical | bad |
| Critical case — Bengal Tiger ANM-0042 not responding to treatment | Medical · raised 12 min ago | Critical | bad |
| Suspected infectious disease in Quarantine Wing — samples sent | Medical · raised 2 d ago | Critical | bad |
| Animal reported missing — Blackbuck, Grassland Park | Animal Collection · raised 1 d ago | Critical | bad |
| Water pump failure — Coastal Marine Facility | Maintenance · raised 1 d ago | Critical | bad |

### Budget overrun flags

`alerts.budgetFlags` · type `list` · size `md` · id `budgetFlags`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Conservation & Research over budget | ₹48.6 cr actual vs ₹48.12 cr budget | — | bad |
| Nutrition & Diet over budget | ₹17.19 cr actual vs ₹16.07 cr budget | — | bad |
| Pharmacy over budget | ₹49.34 cr actual vs ₹45.27 cr budget | — | bad |
| Human Resources over budget | ₹38.11 cr actual vs ₹35.62 cr budget | — | bad |

### Alerts by domain

`alerts.domainMix` · type `chart` · size `md` · id `domainMix`

_shown by default._

**bar chart** · 17 series · total 64

| Series | Value | Share |
|---|---|---|
| Medical | 6 | 9% |
| Housing | 6 | 9% |
| Pharmacy | 6 | 9% |
| Maintenance | 6 | 9% |
| Utilities | 6 | 9% |
| Animal Collection | 3 | 5% |
| Diet | 3 | 5% |
| IoT | 3 | 5% |
| Manpower | 3 | 5% |
| Safety | 3 | 5% |
| Compliance | 3 | 5% |
| Finance | 3 | 5% |

_5 further series not shown._

### Alerts by severity

`alerts.severityMix` · type `chart` · size `md` · id `severityMix`

_shown by default._

**donut chart** · 4 series · total 64

| Series | Value | Share |
|---|---|---|
| high | 30 | 47% |
| medium | 19 | 30% |
| critical | 12 | 19% |
| low | 3 | 5% |

### Overdue items

`alerts.overdueTable` · type `table` · size `lg` · id `overdueTable`

_shown by default._

| Domain | Item | Overdue by | Owner |
|---|---|---|---|
| Maintenance | 92 work orders past due date | up to 34 d | Engineering |
| Compliance | 6 statutory items past deadline | up to 45 d | Admin |
| Medical | 12 case follow-ups missed | up to 9 d | Veterinary Services |
| Assets | 15 devices past calibration date | up to 40 d | Engineering |
| SOPs | 18 SOPs past review date | up to 60 d | Conservation & Research |

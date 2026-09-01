# LAR-001 — Large Carnivores Enclosure 1

| | |
|---|---|
| Key | `enclosure@ENC-0001` |
| Route | `/housing/site/SITE-0001/section/SEC-0001/enclosure/ENC-0001` |
| Kind | Housing level — enclosure |
| Icon | `Building2` |
| Accent | `#0F766E` |
| Widgets | 10 in catalog, 6 shown by default |
| Widget types | kpi ×2, gauge ×3, chart ×1, list ×2, table ×2 |

> This dashboard is generated per enclosure by a factory in `src/config/housingPages.ts`, so one exists for every enclosure in the facility. The figures below are for **LAR-001 — Large Carnivores Enclosure 1** (`ENC-0001`); every `dataKey` is scoped with an `@` suffix and resolved by `resolveEntityData`.

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Enclosure status | kpi | md | `enclosure@ENC-0001.status` |
| 2 | Occupancy against capacity | gauge | md | `enclosure@ENC-0001.capacity` |
| 3 | Hygiene score | gauge | md | `enclosure@ENC-0001.hygiene` |
| 4 | Animals housed here | table | lg | `enclosure@ENC-0001.occupants` |
| 5 | Inspection & hygiene | list | md | `enclosure@ENC-0001.inspection` |
| 6 | Open maintenance issues | list | md | `enclosure@ENC-0001.maintenance` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Enclosure status | kpi | md | `enclosure@ENC-0001.status` | yes |
| Biosecurity | kpi | sm | `enclosure@ENC-0001.biosecurity` | — |
| Occupancy against capacity | gauge | md | `enclosure@ENC-0001.capacity` | yes |
| Hygiene score | gauge | md | `enclosure@ENC-0001.hygiene` | yes |
| Audit score | gauge | md | `enclosure@ENC-0001.audit` | — |
| Occupant health mix | chart | md | `enclosure@ENC-0001.healthMix` | — |
| Inspection & hygiene | list | md | `enclosure@ENC-0001.inspection` | yes |
| Open maintenance issues | list | md | `enclosure@ENC-0001.maintenance` | yes |
| Environment readings | table | md | `enclosure@ENC-0001.environment` | — |
| Animals housed here | table | lg | `enclosure@ENC-0001.occupants` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Enclosure status

`enclosure@ENC-0001.status` · type `kpi` · size `md` · id `status`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| Occupied | Enclosure status | Aviary · Good | — | neutral |

### Biosecurity

`enclosure@ENC-0001.biosecurity` · type `kpi` · size `sm` · id `biosecurity`

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| Non-compliant | Biosecurity | — | — | bad |

### Occupancy against capacity

`enclosure@ENC-0001.capacity` · type `gauge` · size `md` · id `capacity`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 12 | 39 | 31% | Occupancy against capacity | — | warn |

### Hygiene score

`enclosure@ENC-0001.hygiene` · type `gauge` · size `md` · id `hygiene`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 67 | 100 | 67% | Hygiene score | % | warn |

### Audit score

`enclosure@ENC-0001.audit` · type `gauge` · size `md` · id `audit`

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 79 | 100 | 79% | Audit score | % | warn |

### Occupant health mix

`enclosure@ENC-0001.healthMix` · type `chart` · size `md` · id `healthMix`

**donut chart** · 1 series · total 6

| Series | Value | Share |
|---|---|---|
| Healthy | 6 | 100% |

### Inspection & hygiene

`enclosure@ENC-0001.inspection` · type `list` · size `md` · id `inspection`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Last inspection 25 Aug 2026 | Audit score 79% | — | neutral |
| Next inspection 17 Sept 2026 | Scheduled | — | neutral |
| Hygiene score 67% | Below target — cleaning review required | — | warn |

### Open maintenance issues

`enclosure@ENC-0001.maintenance` · type `list` · size `md` · id `maintenance`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| 5 open issues recorded | No active work orders against this enclosure | — | good |

### Environment readings

`enclosure@ENC-0001.environment` · type `table` · size `md` · id `environment`

| Parameter | Reading |
|---|---|
| Temperature | 28.7 °C |
| Humidity | 76 % |
| Water quality | N/A |
| Structural condition | Good |
| Type | Aviary |

### Animals housed here

`enclosure@ENC-0001.occupants` · type `table` · size `lg` · id `occupants`

_shown by default._

| Animal | Species | Sex | Life stage | Health |
|---|---|---|---|---|
| ANM-0194 | Indian Rhinoceros | Female | Adult | Healthy |
| ANM-0212 | Clouded Leopard | Male | Infant | Healthy |
| ANM-0218 | Sloth Bear | Male | Adult | Healthy |
| ANM-0322 | Asiatic Lion | Female | Adult | Healthy |
| ANM-0415 | Chital | Female | Adult | Healthy |
| ANM-0630 | Rhesus Macaque | Female | Geriatric | Healthy |

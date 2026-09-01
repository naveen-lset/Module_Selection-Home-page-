# Nila (Indian Rhinoceros) · ANM-0194

| | |
|---|---|
| Key | `animal@ANM-0194` |
| Route | `/animal/ANM-0194` |
| Kind | Individual animal |
| Icon | `UserCheck` |
| Accent | `#0F766E` |
| Widgets | 7 in catalog, 6 shown by default |
| Widget types | kpi ×1, gauge ×2, list ×1, table ×2, timeline ×1 |

> This dashboard is generated per animal by a factory in `src/config/housingPages.ts`, so one exists for every animal in the facility. The figures below are for **Nila (Indian Rhinoceros) (ACC-2026-00194)** (`ANM-0194`); every `dataKey` is scoped with an `@` suffix and resolved by `resolveEntityData`.

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Health status | kpi | md | `animal@ANM-0194.health` |
| 2 | Welfare score | gauge | md | `animal@ANM-0194.welfare` |
| 3 | Body condition score | gauge | md | `animal@ANM-0194.bcs` |
| 4 | Identity & housing | table | lg | `animal@ANM-0194.identity` |
| 5 | Life history | timeline | lg | `animal@ANM-0194.timeline` |
| 6 | Medical history | list | md | `animal@ANM-0194.cases` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Health status | kpi | md | `animal@ANM-0194.health` | yes |
| Welfare score | gauge | md | `animal@ANM-0194.welfare` | yes |
| Body condition score | gauge | md | `animal@ANM-0194.bcs` | yes |
| Medical history | list | md | `animal@ANM-0194.cases` | yes |
| Identity & housing | table | lg | `animal@ANM-0194.identity` | yes |
| Indian Rhinoceros — species profile | table | lg | `animal@ANM-0194.speciesProfile` | — |
| Life history | timeline | lg | `animal@ANM-0194.timeline` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Health status

`animal@ANM-0194.health` · type `kpi` · size `md` · id `health`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| Healthy | Health status | 547.14 kg | — | good |

### Welfare score

`animal@ANM-0194.welfare` · type `gauge` · size `md` · id `welfare`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 70 | 100 | 70% | Welfare score | % | warn |

### Body condition score

`animal@ANM-0194.bcs` · type `gauge` · size `md` · id `bcs`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 5 | 5 | 100% | Body condition score | — | warn |

### Medical history

`animal@ANM-0194.cases` · type `list` · size `md` · id `cases`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| No medical cases on record | Routine preventive care only | — | good |

### Identity & housing

`animal@ANM-0194.identity` · type `table` · size `lg` · id `identity`

_shown by default._

| Field | Value |
|---|---|
| Animal ID | ANM-0194 |
| Accession no. | ACC-2026-00194 |
| Name | Nila (Indian Rhinoceros) |
| Species | Indian Rhinoceros (Rhinoceros unicornis) |
| Sex | Female |
| Life stage | Adult |
| Date of birth | 15 May 2017 |
| Origin | Wild-born |
| Acquisition | Human-conflict rescue |
| ID method | Tattoo · TAT-228787 |
| Enclosure | LAR-001 — Large Carnivores Enclosure 1 |
| Social group | Nursery group |

_2 further row(s) not shown._

### Indian Rhinoceros — species profile

`animal@ANM-0194.speciesProfile` · type `table` · size `lg` · id `speciesProfile`

| Species attribute | Value |
|---|---|
| Class / order / family | Mammal · Perissodactyla · Rhinocerotidae |
| IUCN status | VU |
| CITES appendix | I |
| Native range | Assam, India |
| Habitat | Tropical dry forest |
| Lifespan | 23 years |
| Adult weight | 541.72 kg |
| Social structure | Fission-fusion group |
| Natural diet | Grazer — grasses |
| Activity pattern | Crepuscular |

### Life history

`animal@ANM-0194.timeline` · type `timeline` · size `lg` · id `timeline`

_shown by default._

| Date | Event | Detail |
|---|---|---|
| 15 May 2017 | Wild-born — Indian Rhinoceros | Human-conflict rescue |
| 14 Jul 2024 | Arrived at facility | Housed in LAR-001 |
| 14 Jul 2024 | Identification — Tattoo | TAT-228787 |

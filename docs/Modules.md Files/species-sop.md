# Species SOPs & Guidelines

| | |
|---|---|
| Key | `species-sop` |
| Route | `/topic/species-sop` |
| Kind | Topic dashboard |
| Icon | `BookOpen` |
| Accent | `#7C3AED` |
| Widgets | 4 in catalog, 4 shown by default |
| Widget types | gauge ×1, list ×1, chart ×1, table ×1 |

## Roles

**Priority module for:** Veterinarian, Biologist.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Staff acknowledgment | gauge | md | `sop.acknowledgment` |
| 2 | SOP review due | list | md | `sop.reviewDue` |
| 3 | SOP status | chart | md | `sop.statusMix` |
| 4 | SOP library | table | lg | `sop.library` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Staff acknowledgment | gauge | md | `sop.acknowledgment` | yes |
| SOP review due | list | md | `sop.reviewDue` | yes |
| SOP status | chart | md | `sop.statusMix` | yes |
| SOP library | table | lg | `sop.library` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Staff acknowledgment

`sop.acknowledgment` · type `gauge` · size `md` · id `acknowledgment`

_shown by default._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 71 | 100 | 71% | Staff SOP acknowledgment | % | warn |

### SOP review due

`sop.reviewDue` · type `list` · size `md` · id `reviewDue`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Asian Elephant — husbandry SOP | Review overdue by 59 days | v4.5 | bad |
| Crested Serpent Eagle — husbandry SOP | Review overdue by 52 days | v2.3 | bad |
| Hoolock Gibbon — husbandry SOP | Review overdue by 44 days | v3.6 | bad |
| Malabar Gliding Frog — husbandry SOP | Review overdue by 38 days | v2.1 | bad |
| Bumblebee Shrimp — husbandry SOP | Review overdue by 31 days | v4.9 | bad |
| Himalayan Monal — husbandry SOP | Review overdue by 30 days | v2.8 | bad |
| Fishing Cat — husbandry SOP | Review overdue by 23 days | v3.9 | bad |
| Indian Rock Python — husbandry SOP | Review overdue by 22 days | v2.6 | bad |

### SOP status

`sop.statusMix` · type `chart` · size `md` · id `statusMix`

_shown by default._

**donut chart** · 3 series · total 72

| Series | Value | Share |
|---|---|---|
| Approved | 45 | 63% |
| Under review | 18 | 25% |
| Draft | 9 | 13% |

### SOP library

`sop.library` · type `table` · size `lg` · id `library`

_shown by default._

| SOP | Version | Owner | Acknowledged | Status |
|---|---|---|---|---|
| Bengal Tiger — husbandry SOP | v1.7 | Priya Khan | 79% | Under review |
| Asiatic Lion — husbandry SOP | v1.3 | Sanjay Pillai | 63% | Approved |
| Indian Leopard — husbandry SOP | v4.3 | Joseph Iyer | 46% | Approved |
| Snow Leopard — husbandry SOP | v4.8 | Joseph Iyer | 71% | Under review |
| Clouded Leopard — husbandry SOP | v2.1 | Kavya Singh | 89% | Draft |
| Fishing Cat — husbandry SOP | v3.9 | Rohit Sharma | 46% | Approved |
| Asian Elephant — husbandry SOP | v4.5 | Divya Khan | 99% | Approved |
| Indian Rhinoceros — husbandry SOP | v2.5 | Sanjay Das | 60% | Approved |

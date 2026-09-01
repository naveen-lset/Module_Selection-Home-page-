# Daily Operations

| | |
|---|---|
| Key | `daily-ops` |
| Route | `/topic/daily-ops` |
| Kind | Topic dashboard |
| Icon | `ListChecks` |
| Accent | `#0F766E` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | gauge ×1, alertFeed ×1, list ×2, chart ×1, table ×1 |

## Roles

**Priority module for:** Management, Keeper / Animal Care.

**Role-specific default layouts:** Keeper / Animal Care. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Daily checklist completion | gauge | md | `ops.checklistCompletion` |
| 2 | Pending & escalated tasks | alertFeed | lg | `ops.pendingTasks` |
| 3 | Shift handover | list | md | `ops.shiftHandover` |
| 4 | Daily command-centre summary | table | lg | `ops.dailySummary` |
| 5 | Site-wise operational score | chart | md | `ops.siteScores` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Daily checklist completion | gauge | md | `ops.checklistCompletion` | yes |
| Pending & escalated tasks | alertFeed | lg | `ops.pendingTasks` | yes |
| Shift handover | list | md | `ops.shiftHandover` | yes |
| Site operational scores | list | md | `ops.roundsStatus` | — |
| Site-wise operational score | chart | md | `ops.siteScores` | yes |
| Daily command-centre summary | table | lg | `ops.dailySummary` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Daily checklist completion

`ops.checklistCompletion` · type `gauge` · size `md` · id `checklistCompletion`

_shown by default · default for Keeper / Animal Care._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 92 | 100 | 92% | Daily checklist completion | % | good |

### Pending & escalated tasks

`ops.pendingTasks` · type `alertFeed` · size `lg` · id `pendingTasks`

_shown by default · default for Keeper / Animal Care._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Operations | Animal count verification pending — Grassland Conservation Park | 4 h |
| medium | Operations | Evening feed distribution not marked complete — Aviary Complex | 2 h |
| medium | Operations | Enrichment schedule incomplete — Primates Section | 5 h |
| low | Operations | Cleaning checklist unsigned — Reptile House | 7 h |

### Shift handover

`ops.shiftHandover` · type `list` · size `md` · id `shiftHandover`

_shown by default · default for Keeper / Animal Care._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Morning → Evening handover (Large Carnivores) | Completed 14:05 · 2 observations logged | Done | good |
| Morning → Evening handover (Hospital Wing) | Completed 14:20 · 3 cases flagged for night watch | Done | good |
| Evening → Night handover (Aquatic Systems) | Pending — pump status to be confirmed | Pending | warn |
| Evening → Night handover (Quarantine Wing) | Pending sign-off by duty vet | Pending | warn |

### Site operational scores

`ops.roundsStatus` · type `list` · size `md` · id `roundsStatus`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Riverside Rescue Centre — operational score 85% | 0 open alerts · 238 staff on roll | — | good |
| Hilltop Rehabilitation Campus — operational score 79% | 4 open alerts · 405 staff on roll | — | warn |
| Coastal Marine Facility — operational score 71% | 12 open alerts · 323 staff on roll | — | warn |
| Central Quarantine Complex — operational score 90% | 3 open alerts · 192 staff on roll | — | good |
| Grassland Conservation Park — operational score 96% | 5 open alerts · 130 staff on roll | — | good |
| Wetland Bird Sanctuary Unit — operational score 73% | 8 open alerts · 141 staff on roll | — | warn |
| Forest Edge Care Facility — operational score 80% | 2 open alerts · 279 staff on roll | — | good |

### Site-wise operational score

`ops.siteScores` · type `chart` · size `md` · id `siteScores`

_shown by default._

**bar chart** · unit: % · 10 series · total 833

| Series | Value | Share |
|---|---|---|
| Riverside | 85 | 10% |
| Hilltop | 79 | 9% |
| Coastal | 71 | 9% |
| Central | 90 | 11% |
| Grassland | 96 | 12% |
| Wetland | 73 | 9% |
| Forest | 80 | 10% |
| Highland | 88 | 11% |
| Desert | 77 | 9% |
| Island | 94 | 11% |

### Daily command-centre summary

`ops.dailySummary` · type `table` · size `lg` · id `dailySummary`

_shown by default · default for Keeper / Animal Care._

| Activity | Planned | Completed | Status |
|---|---|---|---|
| Feeding rounds | 412 | 398 | 96% |
| Cleaning rounds | 380 | 366 | 96% |
| Medical rounds | 96 | 91 | 95% |
| Maintenance rounds | 74 | 62 | 84% |
| Enrichment sessions | 210 | 178 | 85% |
| Animal count verification | 45 | 41 | 91% |

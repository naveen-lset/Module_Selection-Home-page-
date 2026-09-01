# Safety, Security & Emergency

| | |
|---|---|
| Key | `safety` |
| Route | `/topic/safety` |
| Kind | Topic dashboard |
| Icon | `ShieldAlert` |
| Accent | `#B91C1C` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | alertFeed ×1, gauge ×1, chart ×1, list ×3, table ×1 |

## Roles

**Priority module for:** Security.

**Role-specific default layouts:** Security. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Active security incidents | alertFeed | lg | `safety.activeIncidents` |
| 2 | CCTV cameras online | gauge | md | `safety.cctvStatus` |
| 3 | Drill schedule & results | list | md | `safety.drills` |
| 4 | Dangerous animal protocols | list | md | `safety.dangerousAnimalProtocols` |
| 5 | Security deployment | table | lg | `safety.securityDeployment` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Active security incidents | alertFeed | lg | `safety.activeIncidents` | yes |
| CCTV cameras online | gauge | md | `safety.cctvStatus` | yes |
| Incident kinds | chart | md | `safety.incidentKindMix` | — |
| Drill schedule & results | list | md | `safety.drills` | yes |
| Dangerous animal protocols | list | md | `safety.dangerousAnimalProtocols` | yes |
| Staff injury reports | list | md | `safety.injuryReports` | — |
| Security deployment | table | lg | `safety.securityDeployment` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Active security incidents

`safety.activeIncidents` · type `alertFeed` · size `lg` · id `activeIncidents`

_shown by default · default for Security._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Security | Theft — Hilltop (Open) | 8 h |
| critical | Security | Perimeter breach — Grassland (Open) | 8 h |
| critical | Security | Animal escape attempt — Grassland (Open) | 8 h |
| critical | Security | Theft — Wetland (Open) | 8 h |
| medium | Security | Unauthorised entry — Forest (Open) | 8 h |
| low | Security | Theft — Riverside (Open) | 8 h |

### CCTV cameras online

`safety.cctvStatus` · type `gauge` · size `md` · id `cctvStatus`

_shown by default · default for Security._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 17 | 27 | 63% | CCTV cameras online | — | bad |

### Incident kinds

`safety.incidentKindMix` · type `chart` · size `md` · id `incidentKindMix`

**donut chart** · 6 series · total 44

| Series | Value | Share |
|---|---|---|
| Theft | 10 | 23% |
| Perimeter breach | 9 | 20% |
| Unauthorised entry | 7 | 16% |
| Animal escape attempt | 6 | 14% |
| Visitor incident | 6 | 14% |
| CCTV outage | 6 | 14% |

### Drill schedule & results

`safety.drills` · type `list` · size `md` · id `drills`

_shown by default · default for Security._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Animal escape drill — Large Carnivores | Completed 12 Aug 2026 · score 82% | Completed | good |
| Fire evacuation drill — Hospital Wing | Due 15 Sep 2026 | Scheduled | neutral |
| Flood response drill — Riverside | Overdue by 9 days | Overdue | bad |
| Chemical immobilisation drill | Due 28 Sep 2026 | Scheduled | neutral |

### Dangerous animal protocols

`safety.dangerousAnimalProtocols` · type `list` · size `md` · id `dangerousAnimalProtocols`

_shown by default · default for Security._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Asian Elephant — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |
| King Cobra — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |
| Spectacled Cobra — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |
| Russell's Viper — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |
| Mugger Crocodile — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |
| Gharial — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |
| Saltwater Crocodile — dangerous animal protocol | Two-keeper rule · capture kit verified weekly | Extreme | bad |

### Staff injury reports

`safety.injuryReports` · type `list` · size `md` · id `injuryReports`

_default for Security._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Bite / scratch — Central | 03 Jul 2026 · Open · root cause: Under investigation | — | warn |
| Bite / scratch — Riverside | 31 Aug 2026 · Closed · root cause: Third-party lapse | — | warn |
| Staff injury — Riverside | 30 May 2026 · Closed · root cause: Equipment failure | — | warn |
| Bite / scratch — Desert | 05 May 2026 · Closed · root cause: Design inadequacy | — | warn |
| Staff injury — Central | 13 Jun 2026 · Open · root cause: Design inadequacy | — | warn |

### Security deployment

`safety.securityDeployment` · type `table` · size `lg` · id `securityDeployment`

_shown by default · default for Security._

| Site | Guards deployed | Shifts | CCTV | Access control |
|---|---|---|---|---|
| Riverside Rescue Centre | 18 | 3 | 2 | 0 |
| Hilltop Rehabilitation Campus | 36 | 3 | 2 | 2 |
| Coastal Marine Facility | 18 | 3 | 2 | 5 |
| Central Quarantine Complex | 6 | 3 | 3 | 1 |
| Grassland Conservation Park | 12 | 3 | 3 | 3 |
| Wetland Bird Sanctuary Unit | 24 | 3 | 3 | 1 |
| Forest Edge Care Facility | 24 | 3 | 4 | 2 |
| Highland Carnivore Centre | 12 | 3 | 1 | 1 |

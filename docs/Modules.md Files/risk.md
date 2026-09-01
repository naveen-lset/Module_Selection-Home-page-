# Risk Register

| | |
|---|---|
| Key | `risk` |
| Route | `/topic/risk` |
| Kind | Topic dashboard |
| Icon | `Shield` |
| Accent | `#B91C1C` |
| Widgets | 5 in catalog, 4 shown by default |
| Widget types | chart ×2, list ×2, table ×1 |

## Roles

**Priority module for:** Security.

**Role-specific default layouts:** Security. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Risks by severity | chart | md | `risk.bySeverity` |
| 2 | Open critical risks | list | md | `risk.openCritical` |
| 3 | Mitigation in progress | list | md | `risk.ownerActions` |
| 4 | Risk register | table | lg | `risk.register` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Risks by severity | chart | md | `risk.bySeverity` | yes |
| Risks by category | chart | md | `risk.categoryMix` | — |
| Open critical risks | list | md | `risk.openCritical` | yes |
| Mitigation in progress | list | md | `risk.ownerActions` | yes |
| Risk register | table | lg | `risk.register` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Risks by severity

`risk.bySeverity` · type `chart` · size `md` · id `bySeverity`

_shown by default · default for Security._

**donut chart** · 4 series · total 26

| Series | Value | Share |
|---|---|---|
| high | 11 | 42% |
| medium | 8 | 31% |
| critical | 4 | 15% |
| low | 3 | 12% |

### Risks by category

`risk.categoryMix` · type `chart` · size `md` · id `categoryMix`

**bar chart** · 9 series · total 26

| Series | Value | Share |
|---|---|---|
| Fire / weather | 5 | 19% |
| Medicine shortage | 4 | 15% |
| Financial | 3 | 12% |
| Legal & regulatory | 3 | 12% |
| Staff shortage | 3 | 12% |
| Feed supply | 2 | 8% |
| Disease outbreak | 2 | 8% |
| Utility disruption | 2 | 8% |
| Reputation | 2 | 8% |

### Open critical risks

`risk.openCritical` · type `list` · size `md` · id `openCritical`

_shown by default · default for Security._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Night-shift keeper shortfall | Financial · owner Karthik Pillai · Generator AMC upgraded | Possible | bad |
| Adverse publicity from welfare complaint | Medicine shortage · owner Nisha Sharma · Second supplier onboarded | Rare | bad |
| Loss of animal records due to backup failure | Financial · owner Ritu Patil · Vaccination + surveillance plan | Almost certain | bad |
| Night-shift keeper shortfall | Fire / weather · owner Meghna Gupta · Buffer stock policy | Likely | bad |

### Mitigation in progress

`risk.ownerActions` · type `list` · size `md` · id `ownerActions`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Cost overrun on hospital expansion — mitigating | Compliance calendar tracking · owner Fatima Singh | — | warn |
| Loss of animal records due to backup failure — mitigating | Flood barrier construction · owner Ritu Khan | — | warn |
| Escape risk from ageing carnivore fencing — mitigating | Compliance calendar tracking · owner Sanjay Mishra | — | warn |
| Escape risk from ageing carnivore fencing — mitigating | Buffer stock policy · owner Fatima Singh | — | warn |
| Avian influenza incursion via wild birds — mitigating | Quarterly fence audit · owner Rahul Khan | — | warn |
| Failure of aquatic life-support pumps — mitigating | Compliance calendar tracking · owner Divya Nair | — | warn |
| Loss of animal records due to backup failure — mitigating | Generator AMC upgraded · owner Sneha Patil | — | warn |

### Risk register

`risk.register` · type `table` · size `lg` · id `register`

_shown by default · default for Security._

| Risk | Category | Severity | Likelihood | Status |
|---|---|---|---|---|
| Night-shift keeper shortfall | Financial | critical | Possible | Open |
| Adverse publicity from welfare complaint | Medicine shortage | critical | Rare | Open |
| Loss of animal records due to backup failure | Financial | critical | Almost certain | Open |
| Night-shift keeper shortfall | Fire / weather | critical | Likely | Open |
| Grid outage exceeding generator autonomy | Financial | medium | Rare | Open |
| Grid outage exceeding generator autonomy | Legal & regulatory | high | Likely | Closed |
| Non-renewal of statutory licence | Fire / weather | high | Likely | Open |
| Failure of aquatic life-support pumps | Medicine shortage | medium | Likely | Monitored |

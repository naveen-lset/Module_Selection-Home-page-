# Animal Welfare & Behaviour

| | |
|---|---|
| Key | `welfare` |
| Route | `/topic/welfare` |
| Kind | Topic dashboard |
| Icon | `HeartPulse` |
| Accent | `#DB2777` |
| Widgets | 7 in catalog, 6 shown by default |
| Widget types | gauge ×1, kpi ×1, alertFeed ×1, chart ×2, list ×2 |

## Roles

**Priority module for:** Veterinarian, Biologist, Paravet, Keeper / Animal Care, Nutritionist.

**Role-specific default layouts:** Biologist, Keeper / Animal Care. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Average welfare score | gauge | md | `welfare.scoreAverage` |
| 2 | Assessments due | kpi | sm | `welfare.assessmentsDue` |
| 3 | Behavioural concerns | alertFeed | lg | `welfare.concernAlerts` |
| 4 | Abnormal behaviour | list | md | `welfare.abnormalBehaviour` |
| 5 | Enrichment response | chart | md | `welfare.enrichmentCompletion` |
| 6 | Keeper diary | list | md | `welfare.keeperDiary` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Average welfare score | gauge | md | `welfare.scoreAverage` | yes |
| Assessments due | kpi | sm | `welfare.assessmentsDue` | yes |
| Behavioural concerns | alertFeed | lg | `welfare.concernAlerts` | yes |
| Enrichment response | chart | md | `welfare.enrichmentCompletion` | yes |
| Appetite observations | chart | md | `welfare.appetiteMix` | — |
| Abnormal behaviour | list | md | `welfare.abnormalBehaviour` | yes |
| Keeper diary | list | md | `welfare.keeperDiary` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Average welfare score

`welfare.scoreAverage` · type `gauge` · size `md` · id `scoreAverage`

_shown by default · default for Biologist._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 63 | 100 | 63% | Average welfare score | % | bad |

### Assessments due

`welfare.assessmentsDue` · type `kpi` · size `sm` · id `assessmentsDue`

_shown by default · default for Keeper / Animal Care._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 157 | Assessments due this week | — | — | warn |

### Behavioural concerns

`welfare.concernAlerts` · type `alertFeed` · size `lg` · id `concernAlerts`

_shown by default · default for Keeper / Animal Care._

| Severity | Domain | Message | Age |
|---|---|---|---|
| medium | Welfare | Over-grooming — animal ANM-0706 (score 99) | 1 d |
| medium | Welfare | Head bobbing — animal ANM-0670 (score 71) | 1 d |
| medium | Welfare | Reduced social interaction — animal ANM-0720 (score 70) | 1 d |
| high | Welfare | Pacing along fence line — animal ANM-0609 (score 44) | 1 d |
| medium | Welfare | Pacing along fence line — animal ANM-0741 (score 74) | 1 d |
| high | Welfare | Head bobbing — animal ANM-0047 (score 44) | 1 d |

### Enrichment response

`welfare.enrichmentCompletion` · type `chart` · size `md` · id `enrichmentCompletion`

_shown by default · default for Biologist._

**bar chart** · 3 series · total 180

| Series | Value | Share |
|---|---|---|
| Positive | 111 | 62% |
| Neutral | 53 | 29% |
| No response | 16 | 9% |

### Appetite observations

`welfare.appetiteMix` · type `chart` · size `md` · id `appetiteMix`

**donut chart** · 4 series · total 180

| Series | Value | Share |
|---|---|---|
| Normal | 119 | 66% |
| Reduced | 36 | 20% |
| Increased | 15 | 8% |
| Absent | 10 | 6% |

### Abnormal behaviour

`welfare.abnormalBehaviour` · type `list` · size `md` · id `abnormalBehaviour`

_shown by default · default for Biologist, Keeper / Animal Care._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Over-grooming | Animal ANM-0706 · Increase enrichment frequency | 99% | warn |
| Head bobbing | Animal ANM-0670 · Increase enrichment frequency | 71% | warn |
| Reduced social interaction | Animal ANM-0720 · Enclosure modification proposed | 70% | warn |
| Pacing along fence line | Animal ANM-0609 · Increase enrichment frequency | 44% | warn |
| Pacing along fence line | Animal ANM-0741 · Enclosure modification proposed | 74% | warn |
| Head bobbing | Animal ANM-0047 · Social grouping review | 44% | warn |
| Repetitive swimming pattern | Animal ANM-0078 · Increase enrichment frequency | 43% | warn |
| Over-grooming | Animal ANM-0039 · Increase enrichment frequency | 70% | warn |

### Keeper diary

`welfare.keeperDiary` · type `list` · size `md` · id `keeperDiary`

_shown by default · default for Biologist, Keeper / Animal Care._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| 22 Aug 2026 — animal ANM-0706 | Appetite normal, activity normal · Scent trail | — | neutral |
| 23 Aug 2026 — animal ANM-0317 | Appetite normal, activity normal · Water sprinkler play | — | neutral |
| 22 Aug 2026 — animal ANM-0670 | Appetite normal, activity normal · Scent trail | — | neutral |
| 19 Aug 2026 — animal ANM-0452 | Appetite absent, activity normal · Novel object | — | neutral |
| 17 Aug 2026 — animal ANM-0418 | Appetite normal, activity restless · Novel object | — | neutral |
| 18 Aug 2026 — animal ANM-0596 | Appetite reduced, activity restless · Wallow refresh | — | neutral |
| 27 Aug 2026 — animal ANM-0720 | Appetite reduced, activity normal · Browse branches | — | neutral |
| 19 Aug 2026 — animal ANM-0609 | Appetite normal, activity restless · Wallow refresh | — | neutral |

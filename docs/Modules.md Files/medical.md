# Medical & Veterinary Care

| | |
|---|---|
| Key | `medical` |
| Route | `/topic/medical` |
| Kind | Topic dashboard |
| Icon | `Stethoscope` |
| Accent | `#B91C1C` |
| Widgets | 12 in catalog, 7 shown by default |
| Widget types | kpi ×2, alertFeed ×2, chart ×4, list ×3, table ×1 |

## Roles

**Priority module for:** Veterinarian, Paravet, Pharmacist.

**Role-specific default layouts:** Veterinarian, Paravet. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Animals under treatment | kpi | sm | `medical.activeCases` |
| 2 | Under observation | kpi | sm | `medical.underObservation` |
| 3 | Critical & emergency cases | alertFeed | lg | `medical.criticalCases` |
| 4 | Follow-ups due | list | md | `medical.followUpsDue` |
| 5 | Laboratory results pending | list | md | `medical.labPending` |
| 6 | Case status mix | chart | md | `medical.caseStatusMix` |
| 7 | Procedures & next due dates | table | lg | `medical.vaccinationSchedule` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Animals under treatment | kpi | sm | `medical.activeCases` | yes |
| Under observation | kpi | sm | `medical.underObservation` | yes |
| Critical & emergency cases | alertFeed | lg | `medical.criticalCases` | yes |
| Disease surveillance | alertFeed | md | `medical.diseaseSurveillance` | — |
| Case status mix | chart | md | `medical.caseStatusMix` | yes |
| Veterinary team workload | chart | md | `medical.vetWorkload` | — |
| Health score by site | chart | md | `medical.healthScoreBySite` | — |
| Mortality trend | chart | md | `medical.mortalityTrend` | — |
| Follow-ups due | list | md | `medical.followUpsDue` | yes |
| Laboratory results pending | list | md | `medical.labPending` | yes |
| Isolation required | list | md | `medical.isolationCases` | — |
| Procedures & next due dates | table | lg | `medical.vaccinationSchedule` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Animals under treatment

`medical.activeCases` · type `kpi` · size `sm` · id `activeCases`

_shown by default · default for Veterinarian, Paravet._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 1,186 | Animals under treatment | 47 critical | up | warn |

### Under observation

`medical.underObservation` · type `kpi` · size `sm` · id `underObservation`

_shown by default._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 913 | Under observation | — | — | neutral |

### Critical & emergency cases

`medical.criticalCases` · type `alertFeed` · size `lg` · id `criticalCases`

_shown by default · default for Veterinarian._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Medical | Skin lesion — Under investigation (case MED-0001) | 6 h |
| critical | Medical | Ocular discharge — Conjunctivitis (case MED-0002) | 6 h |
| critical | Medical | Skin lesion — Bacterial dermatitis (case MED-0003) | 6 h |
| critical | Medical | Inappetence — Stress-induced colitis (case MED-0004) | 6 h |
| critical | Medical | Inappetence — Nutritional deficiency (case MED-0005) | 6 h |
| critical | Medical | Parasite load — Endoparasitism (case MED-0006) | 6 h |

### Disease surveillance

`medical.diseaseSurveillance` · type `alertFeed` · size `md` · id `diseaseSurveillance`

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Medical | Critical case — Bengal Tiger ANM-0042 not responding to treatment | 12 min |
| critical | Medical | Suspected infectious disease in Quarantine Wing — samples sent | 9 h |
| critical | Medical | Critical case — Bengal Tiger ANM-0042 not responding to treatment | 12 min |
| critical | Medical | Suspected infectious disease in Quarantine Wing — samples sent | 2 d |
| critical | Medical | Critical case — Bengal Tiger ANM-0042 not responding to treatment | 2 h |

### Case status mix

`medical.caseStatusMix` · type `chart` · size `md` · id `caseStatusMix`

_shown by default._

**donut chart** · 5 series · total 140

| Series | Value | Share |
|---|---|---|
| Stable | 45 | 32% |
| Recovering | 39 | 28% |
| Closed | 25 | 18% |
| Serious | 23 | 16% |
| Critical | 8 | 6% |

### Veterinary team workload

`medical.vetWorkload` · type `chart` · size `md` · id `vetWorkload`

**bar chart** · unit: cases · 8 series · total 44

| Series | Value | Share |
|---|---|---|
| Clinician 1 | 7 | 16% |
| Clinician 2 | 6 | 14% |
| Clinician 3 | 6 | 14% |
| Clinician 4 | 5 | 11% |
| Clinician 5 | 5 | 11% |
| Clinician 6 | 5 | 11% |
| Clinician 7 | 5 | 11% |
| Clinician 8 | 5 | 11% |

### Health score by site

`medical.healthScoreBySite` · type `chart` · size `md` · id `healthScoreBySite`

_default for Veterinarian._

**bar chart** · unit: % · 10 series · total 696

| Series | Value | Share |
|---|---|---|
| Riverside | 65 | 9% |
| Hilltop | 69 | 10% |
| Coastal | 78 | 11% |
| Central | 66 | 9% |
| Grassland | 72 | 10% |
| Wetland | 71 | 10% |
| Forest | 66 | 9% |
| Highland | 56 | 8% |
| Desert | 73 | 10% |
| Island | 80 | 11% |

### Mortality trend

`medical.mortalityTrend` · type `chart` · size `md` · id `mortalityTrend`

**line chart** · unit: deaths · 6 series · total 1,647

| Series | Value | Share |
|---|---|---|
| Mar | 246 | 15% |
| Apr | 271 | 16% |
| May | 258 | 16% |
| Jun | 302 | 18% |
| Jul | 281 | 17% |
| Aug | 289 | 18% |

### Follow-ups due

`medical.followUpsDue` · type `list` · size `md` · id `followUpsDue`

_shown by default · default for Veterinarian, Paravet._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Under investigation — follow-up overdue | Due 31 Aug 2026 · Topical antifungal | Critical | bad |
| Conjunctivitis — follow-up overdue | Due 03 Sept 2026 · Antibiotic course — 7 days | Critical | bad |
| Bacterial dermatitis — follow-up overdue | Due 16 Sept 2026 · Anthelmintic dose | Critical | bad |
| Stress-induced colitis — follow-up overdue | Due 04 Sept 2026 · Antibiotic course — 7 days | Critical | bad |
| Nutritional deficiency — follow-up overdue | Due 07 Sept 2026 · Nebulisation | Critical | bad |
| Endoparasitism — follow-up overdue | Due 07 Sept 2026 · Wound dressing — alternate days | Critical | bad |
| Endoparasitism — follow-up overdue | Due 01 Sept 2026 · Topical antifungal | Critical | bad |
| Under investigation — follow-up overdue | Due 19 Sept 2026 · Antibiotic course — 7 days | Critical | bad |

### Laboratory results pending

`medical.labPending` · type `list` · size `md` · id `labPending`

_shown by default · default for Veterinarian, Paravet._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Lab result pending — case MED-0002 | Conjunctivitis | Lab | warn |
| Lab result pending — case MED-0003 | Bacterial dermatitis | Lab | warn |
| Lab result pending — case MED-0005 | Nutritional deficiency | Lab | warn |
| Lab result pending — case MED-0011 | Stress-induced colitis | Lab | warn |
| Lab result pending — case MED-0020 | Endoparasitism | Lab | warn |
| Lab result pending — case MED-0028 | Nutritional deficiency | Lab | warn |
| Lab result pending — case MED-0032 | Pododermatitis | Lab | warn |
| Lab result pending — case MED-0034 | Endoparasitism | Lab | warn |

### Isolation required

`medical.isolationCases` · type `list` · size `md` · id `isolationCases`

_default for Veterinarian, Paravet._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Isolation required — Under investigation | Animal ANM-0485 · opened 04 Jul 2026 | — | warn |
| Isolation required — Nutritional deficiency | Animal ANM-0320 · opened 28 Jul 2026 | — | warn |
| Isolation required — Endoparasitism | Animal ANM-0374 · opened 14 Aug 2026 | — | warn |
| Isolation required — Under investigation | Animal ANM-0159 · opened 04 Aug 2026 | — | warn |
| Isolation required — Bacterial dermatitis | Animal ANM-0166 · opened 19 Jul 2026 | — | warn |
| Isolation required — Pododermatitis | Animal ANM-0050 · opened 30 Jul 2026 | — | warn |

### Procedures & next due dates

`medical.vaccinationSchedule` · type `table` · size `lg` · id `vaccinationSchedule`

_shown by default · default for Veterinarian, Paravet._

| Case | Animal | Procedure | Next due |
|---|---|---|---|
| MED-0001 | ANM-0485 | Endoscopy | 31 Aug 2026 |
| MED-0002 | ANM-0721 | None | 03 Sept 2026 |
| MED-0003 | ANM-0307 | Radiography | 16 Sept 2026 |
| MED-0004 | ANM-0297 | Dental procedure | 04 Sept 2026 |
| MED-0005 | ANM-0320 | Blood sampling | 07 Sept 2026 |
| MED-0006 | ANM-0507 | Surgical repair | 07 Sept 2026 |
| MED-0007 | ANM-0374 | Wound debridement | 01 Sept 2026 |
| MED-0008 | ANM-0159 | Surgical repair | 19 Sept 2026 |

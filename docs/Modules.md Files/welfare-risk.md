# Welfare Risk Overview

| | |
|---|---|
| Key | `welfare-risk` |
| Route | `/topic/welfare-risk` |
| Kind | Topic dashboard |
| Icon | `Activity` |
| Accent | `#DB2777` |
| Widgets | 5 in catalog, 4 shown by default |
| Widget types | list ×3, alertFeed ×1, table ×1 |

## Roles

**Priority module for:** no role — it sits in the general list.

**Role-specific default layouts:** none — every role sees the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Declining welfare scores | list | md | `welfareRisk.declining` |
| 2 | Overcrowding & unsuitable housing | alertFeed | lg | `welfareRisk.overcrowding` |
| 3 | Long-term solitary housing | list | md | `welfareRisk.solitary` |
| 4 | Corrective actions | table | lg | `welfareRisk.correctiveActions` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Declining welfare scores | list | md | `welfareRisk.declining` | yes |
| Overcrowding & unsuitable housing | alertFeed | lg | `welfareRisk.overcrowding` | yes |
| Long-term solitary housing | list | md | `welfareRisk.solitary` | yes |
| High-risk geriatric animals | list | md | `welfareRisk.geriatric` | — |
| Corrective actions | table | lg | `welfareRisk.correctiveActions` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Declining welfare scores

`welfareRisk.declining` · type `list` · size `md` · id `declining`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Animal ANM-0222 — welfare score 30 | Increase enrichment frequency | — | bad |
| Animal ANM-0787 — welfare score 31 | Diet review requested | — | bad |
| Animal ANM-0113 — welfare score 31 | Enclosure modification proposed | — | bad |
| Animal ANM-0639 — welfare score 33 | Enclosure modification proposed | — | bad |
| Animal ANM-0722 — welfare score 33 | Increase enrichment frequency | — | bad |
| Animal ANM-0058 — welfare score 33 | Routine monitoring | — | bad |
| Animal ANM-0332 — welfare score 33 | Increase enrichment frequency | — | bad |
| Animal ANM-0077 — welfare score 33 | Diet review requested | — | bad |

### Overcrowding & unsuitable housing

`welfareRisk.overcrowding` · type `alertFeed` · size `lg` · id `overcrowding`

_shown by default._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Welfare risk | REP-032 overcrowded — 38/33 · Reptile House Section | 2 d |
| high | Welfare risk | CRO-103 overcrowded — 18/16 · Crocodile Enclave Section | 2 d |
| high | Welfare risk | AMP-110 overcrowded — 26/23 · Amphibian Unit Section | 2 d |
| high | Welfare risk | INV-115 overcrowded — 15/13 · Invertebrate House Section | 2 d |

### Long-term solitary housing

`welfareRisk.solitary` · type `list` · size `md` · id `solitary`

_shown by default._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Kavi (Malabar Gliding Frog) | Long-term solitary housing · AMP-178 | — | warn |
| Meera (Spectacled Cobra) | Long-term solitary housing · REP-169 | — | warn |
| Chotu (Indian Rhinoceros) | Long-term solitary housing · HER-149 | — | warn |
| Yash (Emu) | Long-term solitary housing · RAP-028 | — | warn |
| Sarika (Asian Elephant) | Long-term solitary housing · LAR-141 | — | warn |
| Ganga (Lion-tailed Macaque) | Long-term solitary housing · SMA-006 | — | warn |
| Tara (Fishing Cat) | Long-term solitary housing · LAR-072 | — | warn |

### High-risk geriatric animals

`welfareRisk.geriatric` · type `list` · size `md` · id `geriatric`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Meera (Clouded Leopard) | Geriatric care · welfare 88% | Geriatric | neutral |
| Chotu (Indian Rhinoceros) | Geriatric care · welfare 67% | Geriatric | warn |
| Kabir (Freshwater Stingray) | Geriatric care · welfare 44% | Geriatric | warn |
| Rana (Lion-tailed Macaque) | Geriatric care · welfare 54% | Geriatric | warn |
| Shanti (Spectacled Cobra) | Geriatric care · welfare 99% | Geriatric | neutral |
| Zoya (Golden Mahseer) | Geriatric care · welfare 98% | Geriatric | neutral |
| Raja (Cane Toad) | Geriatric care · welfare 62% | Geriatric | warn |

### Corrective actions

`welfareRisk.correctiveActions` · type `table` · size `lg` · id `correctiveActions`

_shown by default._

| Observation | Animal | Action required | Raised |
|---|---|---|---|
| Over-grooming | ANM-0706 | Increase enrichment frequency | 22 Aug 2026 |
| Head bobbing | ANM-0670 | Increase enrichment frequency | 22 Aug 2026 |
| Reduced social interaction | ANM-0720 | Enclosure modification proposed | 27 Aug 2026 |
| Pacing along fence line | ANM-0609 | Increase enrichment frequency | 19 Aug 2026 |
| Pacing along fence line | ANM-0741 | Enclosure modification proposed | 29 Aug 2026 |
| Head bobbing | ANM-0047 | Social grouping review | 17 Aug 2026 |
| Repetitive swimming pattern | ANM-0078 | Increase enrichment frequency | 24 Aug 2026 |
| Over-grooming | ANM-0039 | Increase enrichment frequency | 20 Aug 2026 |

# Individual Animal Profiles

| | |
|---|---|
| Key | `animal-profile` |
| Route | `/topic/animal-profile` |
| Kind | Topic dashboard |
| Icon | `UserCheck` |
| Accent | `#0F766E` |
| Widgets | 4 in catalog, 4 shown by default |
| Widget types | gauge ×1, list ×1, timeline ×1, table ×1 |

## Roles

**Priority module for:** Veterinarian.

**Role-specific default layouts:** Veterinarian. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Animals with verified ID | gauge | md | `profile.idCompliance` |
| 2 | Critical animals | list | md | `profile.criticalAnimals` |
| 3 | Recent intakes | timeline | lg | `profile.recentIntakes` |
| 4 | Animal directory | table | lg | `profile.directory` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Animals with verified ID | gauge | md | `profile.idCompliance` | yes |
| Critical animals | list | md | `profile.criticalAnimals` | yes |
| Recent intakes | timeline | lg | `profile.recentIntakes` | yes |
| Animal directory | table | lg | `profile.directory` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Animals with verified ID

`profile.idCompliance` · type `gauge` · size `md` · id `idCompliance`

_shown by default · default for Veterinarian._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 752 | 800 | 94% | Animals with verified ID | — | good |

### Critical animals

`profile.criticalAnimals` · type `list` · size `md` · id `criticalAnimals`

_shown by default · default for Veterinarian._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Nila (Red Panda) | HOS-129 · BCS 2/5 | Critical | bad |
| Sarika (Gaur) | ELE-087 · BCS 5/5 | Critical | bad |
| Zoya (Golden Mahseer) | HOS-129 · BCS 4/5 | Critical | bad |
| Rhea (Zebra Shark) | AQU-106 · BCS 4/5 | Critical | bad |
| Tara (Purple Frog) | AMP-112 · BCS 5/5 | Critical | bad |
| Pinky (Bengal Tiger) | NOC-068 · BCS 4/5 | Critical | bad |
| Shanti (Indian Softshell Turtle) | CRO-035 · BCS 4/5 | Critical | bad |
| Sarika (Asian Elephant) | SMA-076 · BCS 4/5 | Critical | bad |

### Recent intakes

`profile.recentIntakes` · type `timeline` · size `lg` · id `recentIntakes`

_shown by default._

| Date | Event | Detail |
|---|---|---|
| 31 Aug 2026 | Mihir (Freshwater Stingray) | Human-conflict rescue · AQU-041 |
| 30 Aug 2026 | Gauri (Saltwater Crocodile) | Seizure — wildlife crime · REP-030 |
| 28 Aug 2026 | Rhea (Zebra Shark) | Forest Department rescue · AQU-106 |
| 27 Aug 2026 | Sarika (Lion-tailed Macaque) | Rehabilitation intake · ELE-088 |
| 21 Aug 2026 | Kavi (Asiatic Lion) | Surrendered — private captivity · LAR-001 |
| 14 Aug 2026 | Raja (Himalayan Newt) | Captive birth — in-house · AMP-044 |

### Animal directory

`profile.directory` · type `table` · size `lg` · id `directory`

_shown by default · default for Veterinarian._

| ID | Name | Species | Enclosure | Health |
|---|---|---|---|---|
| ANM-0001 | Meera (Clouded Leopard) | Clouded Leopard | PRI-079 | Healthy |
| ANM-0002 | Bahadur (Lion-tailed Macaque) | Lion-tailed Macaque | LAR-005 | Quarantine |
| ANM-0003 | Pinky (Alexandrine Parakeet) | Alexandrine Parakeet | RAP-163 | Healthy |
| ANM-0004 | Gauri (Indian Leopard) | Indian Leopard | ELE-018 | Healthy |
| ANM-0005 | Mihir (Spectacled Cobra) | Spectacled Cobra | NOC-069 | Healthy |
| ANM-0006 | Rana (Striped Hyena) | Striped Hyena | PRI-078 | Healthy |
| ANM-0007 | Arjun (Deccan Mahseer) | Deccan Mahseer | AQU-106 | Under treatment |
| ANM-0008 | Moti (Indian Softshell Turtle) | Indian Softshell Turtle | CRO-035 | Healthy |
| ANM-0009 | Arjun (Bengal Monitor) | Bengal Monitor | CRO-034 | Under observation |
| ANM-0010 | Sona (Himalayan Black Bear) | Himalayan Black Bear | LAR-139 | Under treatment |

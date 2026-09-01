# Inventory & Stores

| | |
|---|---|
| Key | `stores` |
| Route | `/topic/stores` |
| Kind | Topic dashboard |
| Icon | `Warehouse` |
| Accent | `#4B5563` |
| Widgets | 6 in catalog, 5 shown by default |
| Widget types | kpi ×1, alertFeed ×1, chart ×1, list ×2, table ×1 |

## Roles

**Priority module for:** Pharmacist, Procurement.

**Role-specific default layouts:** Procurement. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Store stock value | kpi | sm | `stores.totalValue` |
| 2 | Minimum stock alerts | alertFeed | lg | `stores.reorderAlerts` |
| 3 | Value by category | chart | md | `stores.valueByCategory` |
| 4 | Slow & non-moving stock | list | md | `stores.nonMoving` |
| 5 | Stock register | table | lg | `stores.stockTable` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Store stock value | kpi | sm | `stores.totalValue` | yes |
| Minimum stock alerts | alertFeed | lg | `stores.reorderAlerts` | yes |
| Value by category | chart | md | `stores.valueByCategory` | yes |
| Slow & non-moving stock | list | md | `stores.nonMoving` | yes |
| Damaged items | list | md | `stores.damaged` | — |
| Stock register | table | lg | `stores.stockTable` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Store stock value

`stores.totalValue` · type `kpi` · size `sm` · id `totalValue`

_shown by default · default for Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| ₹296 lakh | Store stock value | — | flat | neutral |

### Minimum stock alerts

`stores.reorderAlerts` · type `alertFeed` · size `lg` · id `reorderAlerts`

_shown by default · default for Procurement._

| Severity | Domain | Message | Age |
|---|---|---|---|
| medium | Stores | Store item 1 (PPE & safety) — 16 box against reorder 58 | 1 d |
| medium | Stores | Store item 2 (PPE & safety) — 11 pcs against reorder 25 | 1 d |
| medium | Stores | Store item 3 (Spare parts) — 12 box against reorder 13 | 1 d |
| medium | Stores | Store item 4 (Office supplies) — 33 litre against reorder 49 | 1 d |
| medium | Stores | Store item 5 (Uniforms) — 75 set against reorder 81 | 1 d |
| medium | Stores | Store item 6 (Animal care equipment) — 54 kg against reorder 64 | 1 d |

### Value by category

`stores.valueByCategory` · type `chart` · size `md` · id `valueByCategory`

_shown by default._

**donut chart** · unit: ₹ lakh · 6 series · total 296

| Series | Value | Share |
|---|---|---|
| PPE & safety | 49 | 17% |
| Spare parts | 39 | 13% |
| Office supplies | 60 | 20% |
| Uniforms | 69 | 23% |
| Animal care equipment | 40 | 14% |
| Housekeeping | 39 | 13% |

### Slow & non-moving stock

`stores.nonMoving` · type `list` · size `md` · id `nonMoving`

_shown by default · default for Procurement._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Store item 1 — non-moving | Last issued 06 Jul 2026 · value ₹3,01,063 | — | warn |
| Store item 2 — non-moving | Last issued 20 May 2026 · value ₹2,28,170 | — | warn |
| Store item 3 — non-moving | Last issued 08 Apr 2026 · value ₹2,83,029 | — | warn |
| Store item 4 — non-moving | Last issued 27 Mar 2026 · value ₹30,448 | — | warn |
| Store item 5 — non-moving | Last issued 23 Jul 2026 · value ₹2,58,993 | — | warn |
| Store item 6 — non-moving | Last issued 31 Jul 2026 · value ₹1,76,023 | — | warn |
| Store item 7 — non-moving | Last issued 11 Aug 2026 · value ₹2,09,174 | — | warn |
| Store item 8 — non-moving | Last issued 09 Apr 2026 · value ₹1,93,202 | — | warn |

### Damaged items

`stores.damaged` · type `list` · size `md` · id `damaged`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Store item 2 — 4 damaged | PPE & safety · Central | — | bad |
| Store item 4 — 1 damaged | Office supplies · Coastal | — | bad |
| Store item 5 — 1 damaged | Uniforms · Central | — | bad |
| Store item 6 — 4 damaged | Animal care equipment · Coastal | — | bad |
| Store item 7 — 1 damaged | PPE & safety · Hilltop | — | bad |
| Store item 8 — 1 damaged | Animal care equipment · Desert | — | bad |
| Store item 13 — 1 damaged | Office supplies · Hilltop | — | bad |

### Stock register

`stores.stockTable` · type `table` · size `lg` · id `stockTable`

_shown by default · default for Procurement._

| Item | Category | Qty | Reorder | Value ₹ |
|---|---|---|---|---|
| Store item 1 | PPE & safety | 16 | 58 | 3,01,063 |
| Store item 2 | PPE & safety | 11 | 25 | 2,28,170 |
| Store item 3 | Spare parts | 12 | 13 | 2,83,029 |
| Store item 4 | Office supplies | 33 | 49 | 30,448 |
| Store item 5 | Uniforms | 75 | 81 | 2,58,993 |
| Store item 6 | Animal care equipment | 54 | 64 | 1,76,023 |
| Store item 7 | PPE & safety | 62 | 68 | 2,09,174 |
| Store item 8 | Animal care equipment | 3 | 34 | 1,93,202 |

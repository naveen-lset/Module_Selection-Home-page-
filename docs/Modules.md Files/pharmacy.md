# Pharmacy

| | |
|---|---|
| Key | `pharmacy` |
| Route | `/topic/pharmacy` |
| Kind | Topic dashboard |
| Icon | `Pill` |
| Accent | `#7C3AED` |
| Widgets | 8 in catalog, 6 shown by default |
| Widget types | kpi ×1, gauge ×1, alertFeed ×1, chart ×1, table ×3, list ×1 |

## Roles

**Priority module for:** Veterinarian, Paravet, Pharmacist, Procurement.

**Role-specific default layouts:** Veterinarian, Paravet, Pharmacist. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Stock value | kpi | sm | `pharmacy.stockValue` |
| 2 | Emergency medicine availability | gauge | md | `pharmacy.emergencyAvailability` |
| 3 | Stock alerts | alertFeed | lg | `pharmacy.stockAlerts` |
| 4 | Low stock | table | md | `pharmacy.lowStock` |
| 5 | Near expiry | table | md | `pharmacy.nearExpiry` |
| 6 | Controlled drugs | table | md | `pharmacy.controlledDrugs` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Stock value | kpi | sm | `pharmacy.stockValue` | yes |
| Emergency medicine availability | gauge | md | `pharmacy.emergencyAvailability` | yes |
| Stock alerts | alertFeed | lg | `pharmacy.stockAlerts` | yes |
| Category mix | chart | md | `pharmacy.categoryMix` | — |
| Low stock | table | md | `pharmacy.lowStock` | yes |
| Near expiry | table | md | `pharmacy.nearExpiry` | yes |
| Controlled drugs | table | md | `pharmacy.controlledDrugs` | yes |
| Pending medicine orders | list | md | `pharmacy.pendingOrders` | — |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Stock value

`pharmacy.stockValue` · type `kpi` · size `sm` · id `stockValue`

_shown by default · default for Pharmacist._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| ₹1,88,12,601 | Pharmacy stock value | — | — | neutral |

### Emergency medicine availability

`pharmacy.emergencyAvailability` · type `gauge` · size `md` · id `emergencyAvailability`

_shown by default · default for Veterinarian, Pharmacist._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 20 | 20 | 100% | Emergency medicine availability | — | good |

### Stock alerts

`pharmacy.stockAlerts` · type `alertFeed` · size `lg` · id `stockAlerts`

_shown by default · default for Veterinarian, Paravet, Pharmacist._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Pharmacy | Enrofloxacin inj. — batch 1 — out of stock | 3 h |
| critical | Pharmacy | Meloxicam inj. — batch 2 — out of stock | 3 h |
| critical | Pharmacy | Ivermectin — batch 3 — out of stock | 3 h |
| critical | Pharmacy | Ceftriaxone — batch 4 — out of stock | 3 h |
| high | Pharmacy | Ketamine HCl — batch 5 — stock 43 below reorder 108 | 3 h |
| high | Pharmacy | Xylazine — batch 6 — stock 67 below reorder 79 | 3 h |

### Category mix

`pharmacy.categoryMix` · type `chart` · size `md` · id `categoryMix`

_default for Pharmacist._

**donut chart** · 4 series · total 96

| Series | Value | Share |
|---|---|---|
| Medicine | 55 | 57% |
| Consumable | 21 | 22% |
| Controlled drug | 10 | 10% |
| Vaccine | 10 | 10% |

### Low stock

`pharmacy.lowStock` · type `table` · size `md` · id `lowStock`

_shown by default · default for Paravet, Pharmacist._

| Item | Qty | Reorder | Supplier |
|---|---|---|---|
| Enrofloxacin inj. — batch 1 | 0 | 106 | Aarogya Distributors |
| Meloxicam inj. — batch 2 | 0 | 53 | National Vet Depot |
| Ivermectin — batch 3 | 0 | 29 | ZooCare Logistics |
| Ceftriaxone — batch 4 | 0 | 89 | Wildlife Medico Supplies |
| Ketamine HCl — batch 5 | 43 | 108 | Wildlife Medico Supplies |
| Xylazine — batch 6 | 67 | 79 | Wildlife Medico Supplies |
| Vitamin AD3E — batch 7 | 15 | 27 | ZooCare Logistics |
| Calcium borogluconate — batch 8 | 11 | 36 | Wildlife Medico Supplies |

### Near expiry

`pharmacy.nearExpiry` · type `table` · size `md` · id `nearExpiry`

_shown by default · default for Veterinarian, Paravet, Pharmacist._

| Item | Batch | Days to expiry | Qty |
|---|---|---|---|
| Ceftriaxone — batch 4 | B12507 | -17 | 0 |
| Ketamine HCl — batch 5 | B26994 | -16 | 43 |
| Ivermectin — batch 3 | B16120 | -12 | 0 |
| Dexamethasone — batch 10 | B24498 | -9 | 8 |
| Xylazine — batch 6 | B70788 | -6 | 67 |
| Calcium borogluconate — batch 8 | B76458 | 18 | 11 |
| Metronidazole — batch 9 | B22775 | 18 | 45 |
| Meloxicam inj. — batch 2 | B37629 | 32 | 0 |

### Controlled drugs

`pharmacy.controlledDrugs` · type `table` · size `md` · id `controlledDrugs`

_shown by default · default for Veterinarian, Pharmacist._

| Item | Batch | Qty | Storage °C |
|---|---|---|---|
| Ketamine HCl — batch 5 | B26994 | 43 | 19.2 |
| Xylazine — batch 6 | B70788 | 67 | 25 |
| Ketamine HCl — batch 25 | B46955 | 55 | 18.7 |
| Xylazine — batch 26 | B97817 | 70 | 24.1 |
| Ketamine HCl — batch 45 | B37162 | 28 | 21.9 |
| Xylazine — batch 46 | B22727 | 318 | 25.3 |

### Pending medicine orders

`pharmacy.pendingOrders` · type `list` · size `md` · id `pendingOrders`

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| PO/2026/0002 — ColdChain Movers | ₹277.07 lakh · expected 08 Sept 2026 | Pending approval | neutral |
| PO/2026/0007 — MedEquip India | ₹116 lakh · expected 07 Oct 2026 | Pending approval | neutral |
| PO/2026/0043 — SafeGuard Solutions | ₹71.39 lakh · expected 17 Oct 2026 | Pending approval | neutral |
| PO/2026/0051 — SafeGuard Solutions | ₹243.3 lakh · expected 29 Oct 2026 | Pending approval | neutral |
| PO/2026/0052 — MedEquip India | ₹281.21 lakh · expected 23 Sept 2026 | Approved | neutral |
| PO/2026/0053 — ColdChain Movers | ₹244.65 lakh · expected 13 Oct 2026 | Pending approval | neutral |

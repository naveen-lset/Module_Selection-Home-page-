# Procurement & Vendors

| | |
|---|---|
| Key | `procurement` |
| Route | `/topic/procurement` |
| Kind | Topic dashboard |
| Icon | `ShoppingCart` |
| Accent | `#0F766E` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | kpi ×1, list ×2, chart ×3, table ×1 |

## Roles

**Priority module for:** Pharmacist, Admin / Finance, Procurement.

**Role-specific default layouts:** Pharmacist, Admin / Finance, Procurement. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Open purchase orders | kpi | sm | `procurement.openOrders` |
| 2 | Pending approvals | list | md | `procurement.pendingApprovals` |
| 3 | Order status mix | chart | md | `procurement.statusMix` |
| 4 | Vendor performance | chart | md | `procurement.vendorScores` |
| 5 | Deliveries in progress | table | lg | `procurement.deliveries` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Open purchase orders | kpi | sm | `procurement.openOrders` | yes |
| Pending approvals | list | md | `procurement.pendingApprovals` | yes |
| Contract expiries | list | md | `procurement.contractExpiries` | — |
| Order status mix | chart | md | `procurement.statusMix` | yes |
| Vendor performance | chart | md | `procurement.vendorScores` | yes |
| Category-wise spend | chart | md | `procurement.categorySpend` | — |
| Deliveries in progress | table | lg | `procurement.deliveries` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Open purchase orders

`procurement.openOrders` · type `kpi` · size `sm` · id `openOrders`

_shown by default · default for Pharmacist, Admin / Finance, Procurement._

| Value | Label | Delta | Trend | Tone |
|---|---|---|---|---|
| 58 | Open purchase orders | 22 pending approval | up | neutral |

### Pending approvals

`procurement.pendingApprovals` · type `list` · size `md` · id `pendingApprovals`

_shown by default · default for Pharmacist, Admin / Finance, Procurement._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| PO/2026/0001 — ColdChain Movers | Feed & fodder · ₹84.5 lakh | Routine | warn |
| PO/2026/0002 — ColdChain Movers | Medicines · ₹277.07 lakh | Routine | warn |
| PO/2026/0003 — MedEquip India | Lab consumables · ₹31.67 lakh | Routine | warn |
| PO/2026/0004 — GreenBuild Infra | Lab consumables · ₹98.84 lakh | Routine | warn |
| PO/2026/0005 — SafeGuard Solutions | Spare parts · ₹132.51 lakh | Emergency | bad |
| PO/2026/0006 — ColdChain Movers | Lab consumables · ₹264.29 lakh | Routine | warn |
| PO/2026/0007 — MedEquip India | Medicines · ₹116 lakh | Routine | warn |
| PO/2026/0008 — FeedLine Traders | Lab consumables · ₹156.9 lakh | Emergency | bad |

### Contract expiries

`procurement.contractExpiries` · type `list` · size `md` · id `contractExpiries`

_default for Admin / Finance, Procurement._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| ColdChain Movers — Feed & fodder | Contract expired 10 d ago | — | bad |
| MedEquip India — Medicines | Contract expired 1 d ago | — | bad |
| AquaTech Systems — Lab consumables | Contract expired 1 d ago | — | bad |
| MedEquip India — Spare parts | Expires in 5 d | — | bad |
| MedEquip India — Spare parts | Expires in 16 d | — | bad |
| MedEquip India — PPE | Expires in 21 d | — | bad |
| GreenBuild Infra — IT equipment | Expires in 22 d | — | bad |

### Order status mix

`procurement.statusMix` · type `chart` · size `md` · id `statusMix`

_shown by default · default for Procurement._

**donut chart** · 6 series · total 78

| Series | Value | Share |
|---|---|---|
| Pending approval | 22 | 28% |
| Approved | 22 | 28% |
| Delivered | 19 | 24% |
| Dispatched | 12 | 15% |
| Draft | 2 | 3% |
| Rejected | 1 | 1% |

### Vendor performance

`procurement.vendorScores` · type `chart` · size `md` · id `vendorScores`

_shown by default · default for Procurement._

**bar chart** · unit: /5 · 7 series · total 20.4

| Series | Value | Share |
|---|---|---|
| ColdChain | 2.5 | 12% |
| MedEquip | 2.9 | 14% |
| GreenBuild | 3.3 | 16% |
| SafeGuard | 2.5 | 12% |
| FeedLine | 3.2 | 16% |
| PowerGrid | 3 | 15% |
| AquaTech | 3 | 15% |

### Category-wise spend

`procurement.categorySpend` · type `chart` · size `md` · id `categorySpend`

_default for Admin / Finance._

**bar chart** · unit: ₹ lakh · 7 series · total 11,739

| Series | Value | Share |
|---|---|---|
| Feed & fodder | 740 | 6% |
| Medicines | 1,813 | 15% |
| Lab consumables | 2,216 | 19% |
| Spare parts | 1,896 | 16% |
| IT equipment | 1,031 | 9% |
| PPE | 1,918 | 16% |
| Civil works | 2,125 | 18% |

### Deliveries in progress

`procurement.deliveries` · type `table` · size `lg` · id `deliveries`

_shown by default · default for Pharmacist, Procurement._

| PO | Vendor | Expected | Status |
|---|---|---|---|
| PO/2026/0011 | PowerGrid Services | 10 Sept 2026 | Approved |
| PO/2026/0012 | GreenBuild Infra | 21 Oct 2026 | Approved |
| PO/2026/0014 | AquaTech Systems | 20 Oct 2026 | Dispatched |
| PO/2026/0015 | PowerGrid Services | 02 Oct 2026 | Dispatched |
| PO/2026/0016 | SafeGuard Solutions | 11 Sept 2026 | Dispatched |
| PO/2026/0017 | GreenBuild Infra | 06 Sept 2026 | Dispatched |
| PO/2026/0018 | AquaTech Systems | 12 Oct 2026 | Approved |
| PO/2026/0021 | ColdChain Movers | 04 Oct 2026 | Dispatched |

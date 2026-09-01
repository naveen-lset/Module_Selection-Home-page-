# Module data reference

39 dashboards · 299 widget definitions. Generated from the live config and the
widget-data registry — do not edit by hand.

```bash
npx vite-node scripts/generate-module-docs.ts
```

Each page lists its route, the roles that treat it as a priority, its default layout, its full
widget catalog, and the resolved figures behind every `dataKey`.

## Dashboards

| Module | Key | Route | Widgets | Default |
|---|---|---|---|---|
| [Command Centre](home.md) | `home` | `/` | 16 | 4 |
| [Riverside Rescue Centre](level-site.md) | `site@SITE-0001` | `/housing/site/SITE-0001` | 10 | 6 |
| [Large Carnivores Section](level-section.md) | `section@SEC-0001` | `/housing/site/SITE-0001/section/SEC-0001` | 9 | 5 |
| [LAR-001 — Large Carnivores Enclosure 1](level-enclosure.md) | `enclosure@ENC-0001` | `/housing/site/SITE-0001/section/SEC-0001/enclosure/ENC-0001` | 10 | 6 |
| [Nila (Indian Rhinoceros) · ANM-0194](level-animal.md) | `animal@ANM-0194` | `/animal/ANM-0194` | 7 | 6 |

## Topic modules

| Module | Key | Route | Widgets | Default |
|---|---|---|---|---|
| [Animal Collection](animal-collection.md) | `animal-collection` | `/topic/animal-collection` | 15 | 8 |
| [Enclosures & Housing](housing.md) | `housing` | `/housing` | 10 | 6 |
| [Medical & Veterinary Care](medical.md) | `medical` | `/topic/medical` | 12 | 7 |
| [Pharmacy](pharmacy.md) | `pharmacy` | `/topic/pharmacy` | 8 | 6 |
| [Diet & Nutrition](diet.md) | `diet` | `/topic/diet` | 8 | 6 |
| [Food & Diet Inventory](feed-inventory.md) | `feed-inventory` | `/topic/feed-inventory` | 7 | 5 |
| [Breeding & Conservation](breeding.md) | `breeding` | `/topic/breeding` | 8 | 6 |
| [Animal Welfare & Behaviour](welfare.md) | `welfare` | `/topic/welfare` | 7 | 6 |
| [Maintenance](maintenance.md) | `maintenance` | `/topic/maintenance` | 10 | 6 |
| [Assets](assets.md) | `assets` | `/topic/assets` | 9 | 6 |
| [Electronic & IoT Equipment](iot.md) | `iot` | `/topic/iot` | 8 | 6 |
| [Manpower](manpower.md) | `manpower` | `/topic/manpower` | 10 | 6 |
| [Attendance & Leave](attendance.md) | `attendance` | `/topic/attendance` | 7 | 5 |
| [Payroll, Bonus & Rewards](payroll.md) | `payroll` | `/topic/payroll` | 6 | 5 |
| [Water Management](water.md) | `water` | `/topic/water` | 8 | 5 |
| [Electricity & Energy](energy.md) | `energy` | `/topic/energy` | 9 | 6 |
| [Other Utilities](utilities.md) | `utilities` | `/topic/utilities` | 5 | 4 |
| [Inventory & Stores](stores.md) | `stores` | `/topic/stores` | 6 | 5 |
| [Procurement & Vendors](procurement.md) | `procurement` | `/topic/procurement` | 7 | 5 |
| [Safety, Security & Emergency](safety.md) | `safety` | `/topic/safety` | 7 | 5 |
| [Compliance & Audits](compliance.md) | `compliance` | `/topic/compliance` | 6 | 4 |
| [Projects & Infrastructure](projects.md) | `projects` | `/topic/projects` | 6 | 5 |
| [Transport & Logistics](transport.md) | `transport` | `/topic/transport` | 7 | 5 |
| [Finance & Budget](finance.md) | `finance` | `/topic/finance` | 7 | 5 |
| [Daily Operations](daily-ops.md) | `daily-ops` | `/topic/daily-ops` | 6 | 5 |
| [Alerts & Key Indicators](alerts.md) | `alerts` | `/topic/alerts` | 6 | 5 |
| [Species SOPs & Guidelines](species-sop.md) | `species-sop` | `/topic/species-sop` | 4 | 4 |
| [Species & Taxonomy Master](species-master.md) | `species-master` | `/topic/species-master` | 6 | 5 |
| [Individual Animal Profiles](animal-profile.md) | `animal-profile` | `/topic/animal-profile` | 4 | 4 |
| [Incident Management](incidents.md) | `incidents` | `/topic/incidents` | 6 | 5 |
| [Risk Register](risk.md) | `risk` | `/topic/risk` | 5 | 4 |
| [Welfare Risk Overview](welfare-risk.md) | `welfare-risk` | `/topic/welfare-risk` | 5 | 4 |
| [Animal Population Planning](population.md) | `population` | `/topic/population` | 5 | 4 |
| [Executive Action Dashboard](executive.md) | `executive` | `/topic/executive` | 7 | 5 |

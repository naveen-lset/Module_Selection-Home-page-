# Electronic & IoT Equipment

| | |
|---|---|
| Key | `iot` |
| Route | `/topic/iot` |
| Kind | Topic dashboard |
| Icon | `Cpu` |
| Accent | `#2563EB` |
| Widgets | 8 in catalog, 6 shown by default |
| Widget types | gauge ×1, alertFeed ×1, chart ×3, list ×2, table ×1 |

## Roles

**Priority module for:** Maintenance / Engineering, Security.

**Role-specific default layouts:** Maintenance / Engineering. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Devices online | gauge | md | `iot.onlineGauge` |
| 2 | Offline device alerts | alertFeed | lg | `iot.offlineAlerts` |
| 3 | Device health | chart | md | `iot.healthMix` |
| 4 | Low battery | list | md | `iot.batteryLow` |
| 5 | Calibration overdue | list | md | `iot.calibrationDue` |
| 6 | Device register | table | lg | `iot.deviceTable` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Devices online | gauge | md | `iot.onlineGauge` | yes |
| Offline device alerts | alertFeed | lg | `iot.offlineAlerts` | yes |
| Device health | chart | md | `iot.healthMix` | yes |
| Connectivity status | chart | md | `iot.connectivityMix` | — |
| Devices by kind | chart | md | `iot.kindMix` | — |
| Low battery | list | md | `iot.batteryLow` | yes |
| Calibration overdue | list | md | `iot.calibrationDue` | yes |
| Device register | table | lg | `iot.deviceTable` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Devices online

`iot.onlineGauge` · type `gauge` · size `md` · id `onlineGauge`

_shown by default · default for Maintenance / Engineering._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 128 | 180 | 71% | Devices online | — | good |

### Offline device alerts

`iot.offlineAlerts` · type `alertFeed` · size `lg` · id `offlineAlerts`

_shown by default · default for Maintenance / Engineering._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | IoT | Display kiosk 1 offline — last data 4349 min ago (Forest) | 3 h |
| high | IoT | Smart meter 2 offline — last data 1698 min ago (Highland) | 3 h |
| high | IoT | CCTV camera 3 offline — last data 677 min ago (Forest) | 3 h |
| high | IoT | CCTV camera 4 offline — last data 4502 min ago (Wetland) | 3 h |
| high | IoT | Humidity sensor 5 offline — last data 1236 min ago (Hilltop) | 3 h |
| high | IoT | Network switch 6 offline — last data 3861 min ago (Grassland) | 3 h |

### Device health

`iot.healthMix` · type `chart` · size `md` · id `healthMix`

_shown by default._

**donut chart** · 3 series · total 180

| Series | Value | Share |
|---|---|---|
| Working | 131 | 73% |
| Faulty | 26 | 14% |
| Degraded | 23 | 13% |

### Connectivity status

`iot.connectivityMix` · type `chart` · size `md` · id `connectivityMix`

**bar chart** · 3 series · total 180

| Series | Value | Share |
|---|---|---|
| Online | 128 | 71% |
| Offline | 29 | 16% |
| Intermittent | 23 | 13% |

### Devices by kind

`iot.kindMix` · type `chart` · size `md` · id `kindMix`

**donut chart** · 8 series · total 180

| Series | Value | Share |
|---|---|---|
| CCTV camera | 27 | 15% |
| Display kiosk | 26 | 14% |
| Smart meter | 25 | 14% |
| Network switch | 22 | 12% |
| Temperature sensor | 21 | 12% |
| Water quality sensor | 21 | 12% |
| Humidity sensor | 20 | 11% |
| Access control | 18 | 10% |

### Low battery

`iot.batteryLow` · type `list` · size `md` · id `batteryLow`

_shown by default · default for Maintenance / Engineering._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| CCTV camera 28 | Battery 4% · Online | CCTV camera | bad |
| Display kiosk 132 | Battery 4% · Online | Display kiosk | bad |
| Smart meter 2 | Battery 5% · Offline | Smart meter | bad |
| CCTV camera 124 | Battery 5% · Online | CCTV camera | bad |
| Access control 171 | Battery 5% · Online | Access control | bad |
| Water quality sensor 11 | Battery 6% · Offline | Water quality sensor | bad |
| CCTV camera 140 | Battery 6% · Online | CCTV camera | bad |
| Temperature sensor 180 | Battery 6% · Online | Temperature sensor | bad |

### Calibration overdue

`iot.calibrationDue` · type `list` · size `md` · id `calibrationDue`

_shown by default · default for Maintenance / Engineering._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Display kiosk 1 — calibration overdue | 11 days overdue · firmware v1.8.5 | — | bad |
| Smart meter 2 — calibration overdue | 6 days overdue · firmware v1.2.7 | — | bad |
| CCTV camera 3 — calibration overdue | 27 days overdue · firmware v3.0.2 | — | bad |
| CCTV camera 4 — calibration overdue | 25 days overdue · firmware v2.7.8 | — | bad |
| Humidity sensor 5 — calibration overdue | 14 days overdue · firmware v4.8.4 | — | bad |
| Network switch 6 — calibration overdue | 29 days overdue · firmware v1.5.4 | — | bad |
| Smart meter 7 — calibration overdue | 30 days overdue · firmware v2.0.3 | — | bad |

### Device register

`iot.deviceTable` · type `table` · size `lg` · id `deviceTable`

_shown by default._

| Device | Kind | Site | Connectivity | Last data |
|---|---|---|---|---|
| Display kiosk 1 | Display kiosk | Forest | Offline | 4349 min |
| Smart meter 2 | Smart meter | Highland | Offline | 1698 min |
| CCTV camera 3 | CCTV camera | Forest | Offline | 677 min |
| CCTV camera 4 | CCTV camera | Wetland | Offline | 4502 min |
| Humidity sensor 5 | Humidity sensor | Hilltop | Offline | 1236 min |
| Network switch 6 | Network switch | Grassland | Offline | 3861 min |
| Smart meter 7 | Smart meter | Wetland | Offline | 2551 min |
| Network switch 8 | Network switch | Island | Offline | 1346 min |

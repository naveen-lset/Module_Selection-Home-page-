# Attendance & Leave

| | |
|---|---|
| Key | `attendance` |
| Route | `/topic/attendance` |
| Kind | Topic dashboard |
| Icon | `CalendarCheck` |
| Accent | `#2563EB` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | gauge ×1, alertFeed ×1, list ×2, chart ×2, table ×1 |

## Roles

**Priority module for:** HR / People.

**Role-specific default layouts:** HR / People. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Attendance today | gauge | md | `attendance.todayPct` |
| 2 | Manpower shortage alerts | alertFeed | lg | `attendance.shortageAlerts` |
| 3 | Leave applications pending | list | md | `attendance.pendingLeave` |
| 4 | Shift roster | table | lg | `attendance.shiftRoster` |
| 5 | Attendance trend | chart | md | `attendance.trend` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Attendance today | gauge | md | `attendance.todayPct` | yes |
| Manpower shortage alerts | alertFeed | lg | `attendance.shortageAlerts` | yes |
| Leave applications pending | list | md | `attendance.pendingLeave` | yes |
| Upcoming leave impact | list | md | `attendance.upcomingImpact` | — |
| Leave type mix | chart | md | `attendance.leaveTypeMix` | — |
| Attendance trend | chart | md | `attendance.trend` | yes |
| Shift roster | table | lg | `attendance.shiftRoster` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Attendance today

`attendance.todayPct` · type `gauge` · size `md` · id `todayPct`

_shown by default · default for HR / People._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 87 | 100 | 87% | Attendance today | % | good |

### Manpower shortage alerts

`attendance.shortageAlerts` · type `alertFeed` · size `lg` · id `shortageAlerts`

_shown by default · default for HR / People._

| Severity | Domain | Message | Age |
|---|---|---|---|
| high | Manpower | Night-shift keeper shortage at Hilltop Campus | 4 d |
| high | Manpower | Night-shift keeper shortage at Hilltop Campus | 5 h |
| high | Manpower | Night-shift keeper shortage at Hilltop Campus | 12 min |

### Leave applications pending

`attendance.pendingLeave` · type `list` · size `md` · id `pendingLeave`

_shown by default · default for HR / People._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Joseph Gupta — Casual leave | 12 days from 29 Aug 2026 · substitute pending | Pending | bad |
| Rahul Mishra — Sick leave | 3 days from 29 Aug 2026 · substitute arranged | Pending | warn |
| Karthik Gupta — Sick leave | 8 days from 28 Sept 2026 · substitute arranged | Pending | warn |
| Nisha Iyer — Sick leave | 7 days from 26 Sept 2026 · substitute pending | Pending | bad |
| Deepak Kulkarni — Sick leave | 2 days from 21 Sept 2026 · substitute arranged | Pending | warn |
| Arun Kulkarni — Earned leave | 10 days from 21 Sept 2026 · substitute arranged | Pending | warn |
| Lakshmi Patil — Sick leave | 6 days from 24 Sept 2026 · substitute arranged | Pending | warn |
| Anita Khan — Casual leave | 1 days from 05 Oct 2026 · substitute arranged | Pending | warn |

### Upcoming leave impact

`attendance.upcomingImpact` · type `list` · size `md` · id `upcomingImpact`

_default for HR / People._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Sneha Nair — 11 d leave from 19 Sept 2026 | Substitute NOT arranged | — | warn |
| Divya Das — 4 d leave from 20 Sept 2026 | Substitute NOT arranged | — | warn |
| Priya Khan — 4 d leave from 06 Oct 2026 | Substitute arranged | — | neutral |
| Kavya Singh — 5 d leave from 07 Sept 2026 | Substitute arranged | — | neutral |
| Divya Nair — 9 d leave from 04 Oct 2026 | Substitute arranged | — | neutral |
| Divya Kulkarni — 12 d leave from 24 Sept 2026 | Substitute arranged | — | neutral |
| Rahul Thomas — 2 d leave from 29 Sept 2026 | Substitute arranged | — | neutral |

### Leave type mix

`attendance.leaveTypeMix` · type `chart` · size `md` · id `leaveTypeMix`

**donut chart** · 5 series · total 64

| Series | Value | Share |
|---|---|---|
| Sick | 21 | 33% |
| Casual | 17 | 27% |
| Earned | 17 | 27% |
| Compensatory | 7 | 11% |
| Unpaid | 2 | 3% |

### Attendance trend

`attendance.trend` · type `chart` · size `md` · id `trend`

_shown by default · default for HR / People._

**line chart** · unit: % · 7 series · total 603

| Series | Value | Share |
|---|---|---|
| Mon | 88 | 15% |
| Tue | 90 | 15% |
| Wed | 87 | 14% |
| Thu | 86 | 14% |
| Fri | 89 | 15% |
| Sat | 84 | 14% |
| Sun | 79 | 13% |

### Shift roster

`attendance.shiftRoster` · type `table` · size `lg` · id `shiftRoster`

_shown by default · default for HR / People._

| Staff | Role | Shift | Site | Status |
|---|---|---|---|---|
| Vikas Patil | Keeper / Animal Care | Evening | Grassland | Absent |
| Sneha Iyer | Maintenance / Engineering | General | Hilltop | On leave |
| Rahul Thomas | Security | Morning | Grassland | Present |
| Aarav Menon | Paravet | Night | Grassland | Present |
| Nisha Chauhan | Veterinarian | Morning | Forest | Present |
| Sanjay Pillai | Biologist | Morning | Desert | Present |
| Rahul Iyer | Nutritionist | Morning | Grassland | Present |
| Lakshmi Gupta | Pharmacist | Night | Island | Present |

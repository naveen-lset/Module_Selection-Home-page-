# Executive Action Dashboard

| | |
|---|---|
| Key | `executive` |
| Route | `/topic/executive` |
| Kind | Topic dashboard |
| Icon | `Target` |
| Accent | `#111827` |
| Widgets | 7 in catalog, 5 shown by default |
| Widget types | gauge ×1, alertFeed ×1, list ×1, chart ×2, timeline ×1, table ×1 |

## Roles

**Priority module for:** Management.

**Role-specific default layouts:** Management. Other roles get the module default below.

## Default layout

| # | Widget | Type | Size | dataKey |
|---|---|---|---|---|
| 1 | Facility health score | gauge | md | `exec.facilityScore` |
| 2 | Matters requiring attention | alertFeed | lg | `exec.actionFeed` |
| 3 | Approvals awaiting management | list | md | `exec.approvals` |
| 4 | Overdue high-priority actions | table | lg | `exec.overdueTable` |
| 5 | Facility score trend | chart | md | `exec.trendComparison` |

## Widget catalog

| Widget | Type | Size | dataKey | Default |
|---|---|---|---|---|
| Facility health score | gauge | md | `exec.facilityScore` | yes |
| Matters requiring attention | alertFeed | lg | `exec.actionFeed` | yes |
| Approvals awaiting management | list | md | `exec.approvals` | yes |
| Facility score trend | chart | md | `exec.trendComparison` | yes |
| Impact mix | chart | md | `exec.impactMix` | — |
| Decisions required | timeline | lg | `exec.decisionsToday` | — |
| Overdue high-priority actions | table | lg | `exec.overdueTable` | yes |

## Data

Resolved through `src/data/registry.ts` from the seeded dataset. Figures are deterministic.

### Facility health score

`exec.facilityScore` · type `gauge` · size `md` · id `facilityScore`

_shown by default · default for Management._

| Value | Max | Percent | Label | Unit | Tone |
|---|---|---|---|---|---|
| 87 | 100 | 87% | Facility health score | % | good |

### Matters requiring attention

`exec.actionFeed` · type `alertFeed` · size `lg` · id `actionFeed`

_shown by default · default for Management._

| Severity | Domain | Message | Age |
|---|---|---|---|
| critical | Housekeeping | Approve emergency medicine purchase for critical cases (Awaiting approval) | 16 d |
| medium | Procurement & Stores | Decide on transfer of surplus Blackbuck to partner facility (Awaiting decision) | 6 d |
| high | Conservation & Research | Sanction overtime for night-shift keeper shortage (Awaiting decision) | 14 d |
| critical | Safety & Security | Approve budget revision for hospital wing expansion (Awaiting decision) | 21 d |
| critical | Animal Care | Sign off CITES renewal documentation (Awaiting approval) | 20 d |
| medium | Conservation & Research | Decide on closure of overcrowded carnivore enclosures (Awaiting approval) | 5 d |
| high | Human Resources | Approve vendor blacklisting after repeated rejected supplies (Awaiting approval) | 11 d |
| medium | Nutrition & Diet | Clear pending payroll approvals for contract labour (Blocked) | 6 d |

### Approvals awaiting management

`exec.approvals` · type `list` · size `md` · id `approvals`

_shown by default · default for Management._

| Primary | Secondary | Badge | Tone |
|---|---|---|---|
| Approve emergency medicine purchase for critical cases | Housekeeping · owner Sneha Kulkarni · due 03 Sept 2026 | Financial | warn |
| Sign off CITES renewal documentation | Animal Care · owner Nisha Sharma · due 17 Sept 2026 | Operational | warn |
| Decide on closure of overcrowded carnivore enclosures | Conservation & Research · owner Joseph Nair · due 05 Sept 2026 | Operational | warn |
| Approve vendor blacklisting after repeated rejected supplies | Human Resources · owner Fatima Singh · due 12 Sept 2026 | Welfare | bad |
| Approve emergency medicine purchase for critical cases | Administration · owner Fatima Singh · due 02 Sept 2026 | Welfare | bad |
| Decide on transfer of surplus Blackbuck to partner facility | Finance · owner Rahul Khan · due 23 Aug 2026 | Operational | warn |
| Sanction overtime for night-shift keeper shortage | Safety & Security · owner Sanjay Khan · due 04 Sept 2026 | Financial | warn |
| Approve vendor blacklisting after repeated rejected supplies | Animal Care · owner Deepak Mishra · due 29 Sept 2026 | Safety | bad |

### Facility score trend

`exec.trendComparison` · type `chart` · size `md` · id `trendComparison`

_shown by default · default for Management._

**line chart** · unit: facility score · 6 series · total 503

| Series | Value | Share |
|---|---|---|
| Mar | 81 | 16% |
| Apr | 83 | 17% |
| May | 84 | 17% |
| Jun | 82 | 16% |
| Jul | 86 | 17% |
| Aug | 87 | 17% |

### Impact mix

`exec.impactMix` · type `chart` · size `md` · id `impactMix`

_default for Management._

**donut chart** · 5 series · total 24

| Series | Value | Share |
|---|---|---|
| Financial | 5 | 21% |
| Compliance | 5 | 21% |
| Operational | 5 | 21% |
| Safety | 5 | 21% |
| Welfare | 4 | 17% |

### Decisions required

`exec.decisionsToday` · type `timeline` · size `lg` · id `decisionsToday`

| Date | Event | Detail |
|---|---|---|
| 03 Sept 2026 | Approve emergency medicine purchase for critical cases | Housekeeping · Awaiting approval · Board note prepared |
| 16 Sept 2026 | Decide on transfer of surplus Blackbuck to partner facility | Procurement & Stores · Awaiting decision · Board note prepared |
| 07 Sept 2026 | Sanction overtime for night-shift keeper shortage | Conservation & Research · Awaiting decision · Escalated by site head |
| 29 Sept 2026 | Approve budget revision for hospital wing expansion | Safety & Security · Awaiting decision · Second reminder issued |
| 17 Sept 2026 | Sign off CITES renewal documentation | Animal Care · Awaiting approval · Board note prepared |
| 05 Sept 2026 | Decide on closure of overcrowded carnivore enclosures | Conservation & Research · Awaiting approval · Pending vendor response |

### Overdue high-priority actions

`exec.overdueTable` · type `table` · size `lg` · id `overdueTable`

_shown by default · default for Management._

| Matter | Owner | Due | Escalated | Impact |
|---|---|---|---|---|
| Approve budget revision for hospital wing expansion | Fatima Singh | 29 Sept 2026 | 21 d | Financial |
| Sign off CITES renewal documentation | Nisha Sharma | 17 Sept 2026 | 20 d | Operational |
| Clear pending payroll approvals for contract labour | Ritu Patil | 09 Sept 2026 | 20 d | Compliance |
| Decide on closure of overcrowded carnivore enclosures | Nisha Sharma | 28 Aug 2026 | 19 d | Welfare |
| Sanction overtime for night-shift keeper shortage | Sanjay Khan | 04 Sept 2026 | 18 d | Financial |
| Approve vendor blacklisting after repeated rejected supplies | Deepak Mishra | 29 Sept 2026 | 18 d | Safety |
| Approve emergency medicine purchase for critical cases | Sneha Kulkarni | 03 Sept 2026 | 16 d | Financial |
| Approve enclosure modification for welfare corrective action | Fatima Singh | 21 Aug 2026 | 15 d | Welfare |

# ARCHITECT — Site Command Centre

**Request** Add a second top-level destination, *Site Command Centre*, alongside
*Module Selection* in the ANTZ tablet app — a configurable Site Workspace over
Housing → Sites → Site → Sections → Enclosures, with role-based widget defaults,
personal customization and permission-aware widget availability.

**Complexity** Strategic — new operational surface, system-level IA change.
**Date** 31 August 2026 · **Repo** `~/Desktop/Module Selection` @ `a0f5daa`

---

## 1 · Problem Definition

The product has no surface that represents a **Site as an operating entity**.

Seventeen modules each cut the organisation *vertically* by function (Medical,
Pharmacy, Assets, Users). A Site is where all of those verticals collide
*horizontally* — one place, one budget, one generator, one team, one licence,
one set of animals. Anybody whose accountability is a **place** rather than a
**function** therefore has no home in the application: to answer "how is my Site
doing?" they must visit many modules and assemble the answer in their head.

## 2 · Problem vs Symptom

| | |
|---|---|
| **Symptom** | tapping a Site opens an animal listing |
| **Symptom** | Site-level facts (staff, budget, utilities, compliance) exist only inside module verticals |
| **Problem** | there is no place-scoped operational surface; accountability for a Site has no corresponding view |
| **Root-cause hypothesis** | **the IA is function-first while accountability is place-first.** *Module Selection* answers "which function do I want?" — a good answer to a different question. Module cards aggregate across the whole organisation, so they structurally cannot answer "how is *this* Site doing?" |

A second, structural symptom: the existing home page is *already* a customizable
widget dashboard. Building a second one carelessly yields two divergent widget
systems in one product — the failure this framing is most concerned with.

## 3 · Stakeholder Map

| | Role | What they need from a Site |
|---|---|---|
| **Decides** | Site In-charge / Site Manager | escalate or absorb; where to put people; what to spend |
| **Decides** | Facility / Operations Manager | which failing thing to fix first |
| **Decides** | Administrator | approvals, staffing, compliance coordination |
| **Decides** | Veterinarian | clinical triage scoped to this Site |
| **Acts** | Keepers · technicians · security · biologists · vendors | the assigned task, in context |
| **Consumes** | Director / regional leadership | which of my Sites needs me this week |
| **Consumes** | Compliance & audit bodies · Finance | evidence of readiness; burn against budget |
| **Configures** | every role, as themselves | a workspace that matches their own responsibility |

## 4 · Decision Architecture

Organised around **recurring decisions**, not widgets. Each row is the test a
proposed widget has to pass: *which decision does this serve?*

| # | Decision | Class | Owner | Freq | Question | Insight | Action | Conf | Stakes |
|---|---|---|---|---|---|---|---|---|---|
| D1 | Escalate or absorb? | Attention | Site In-charge | daily | What crossed a threshold since I last looked? | Needs Attention roll-up: counts by domain × severity | assign owner · escalate · schedule | high | **critical** |
| D2 | Where do I put today's people? | Change | Site In-charge / Admin | per shift | Which sections and duties are uncovered right now? | shift coverage vs. required; on-leave; unassigned responsibility | reassign · call cover | high | high |
| D3 | Which failing thing do I fix first? | Risk | Facility Manager | daily | Which assets are life-critical (water, generator, ventilation) vs. merely overdue? | asset criticality × downtime consequence | raise / prioritise work order | high | **critical** |
| D4 | Will this Site fail an inspection or lose a licence? | Risk | Admin / Site In-charge | weekly · event | Which obligations are unmet, and when do they expire? | compliance score decomposed + renewal dates | assign compliance task | high | high |
| D5 | Can I still spend? | Forecast | Site In-charge / Finance | monthly | Burn vs. remaining vs. already committed? | budget utilisation + pending purchase requests | approve · defer · reallocate | medium | high |
| D6 | What needs clinical attention here today? | Attention | Veterinarian | daily | Open cases, quarantine, welfare alerts — at *this* Site | case list ordered by urgency | schedule visit · order medicine | high | **critical** |
| D7 | Are we ready if something happens tonight? | Risk | Site In-charge | weekly | Which readiness component is degraded? | readiness checklist, failing item named | fix · verify | medium | **critical** |
| D8 | Can we operate through the week? | Forecast | Ops / Admin | weekly | Which consumables are below reorder? | stock health by category + days of cover | raise purchase request | medium | high |
| D9 | What is happening with species and populations? | Opportunity | Biologist | weekly | Population, transfers, welfare trend by section | population flow + transfer state | plan transfer · record | medium | medium |
| D10 | Which of my Sites needs me this week? | Risk | Director | weekly | Comparative health across Sites | Site health index, ranked | visit · intervene | low | medium |
| D11 | Is this workspace showing me my actual job? | Change | every role | continuous | Does my arrangement match my responsibility? | role default + visible customization affordance | add · remove · reorder · restore | high | high |

All five decision classes are covered. **D10 is the Sites-list decision** — it
shapes what the Sites list must carry, and is otherwise out of v1 scope (§6).

## 5 · Success Criteria

1. A Site In-charge can name the **top three things needing their attention
   within ten seconds** of opening a Site, without scrolling.
2. **Every widget traces to a decision in §4.** A widget that traces to none is
   cut, however easy its data is.
3. Switching role changes the **selection and order** of widgets, never the data
   source — the same Site reads differently to five roles.
4. A permission-limited role (say three modules) still gets a **balanced,
   intentional** page: no gaps, no fake zeros, no dead categories.
5. **One widget engine, not two** — Site widgets reuse the existing
   layout / semantic-size / packer / store primitives.
6. No horizontal scroll and no clipped label at 1024 · 1194 · 1366 landscape and
   834 portrait, across every widget at every size it declares.
7. A customized Manager arrangement **survives** a role switch and a reload, and
   is restorable to default per role.

## 6 · Scope Boundaries — what we are NOT solving

- **Not** building Section Workspace or Enclosure Workspace. The philosophy is
  set (widgets get more specific with depth); the surfaces are deferred.
- **Not** building real module destinations. Widgets navigate; destinations are
  announced/stubbed exactly as the current app does.
- **Not** a cross-site comparison dashboard. The Sites list carries health
  (per D10); the analytics view is out.
- **No** backend, auth, or permissions engine. Role and permission are a
  front-end simulation with a switcher, for design evaluation.
- **Not** re-opening the gradient palette or the AA contrast decision — recorded
  decision, README and handoff §6. Site widget colour must come from the
  existing closed 16-gradient set.
- **Not** lifting the 1024px content cap or the 5-column ladder.

## 7 · Unknowns & Assumptions

**Known**
- The Site Workspace lives *inside this repo*, as a sibling selection to Module
  Selection — stated by the user.
- The engine to build on: `cardVariants.js` (catalogue-as-data), `sizes.js`
  (semantic sizes), `pack.js`, `ModuleGrid`, `DragController`,
  `EditModulesMode`, `ModulePickerBottomSheet`, `layoutStore` (localStorage).
- 19 card layouts already exist. Nine of the brief's eleven widget *types* map
  onto them (§9 of this doc's handoff note).

**Unknown**
- The real role taxonomy and permission matrix in ANTZ v5.
- Whether a Sites / Sections / Enclosures data model already exists in
  `antz-command-centre-v5` that this should mirror.
- Whether the existing hero banner (linking out to the v5 Command Centre)
  stays, moves, or is superseded by this navigation.
- Entry behaviour: Sites list first, or straight to the user's assigned Site.

**Assumptions**
- Tablet landscape 1024–1366 primary; portrait 834 supported.
- One signed-in user (Sourav Tambe) plus a **demo role switcher** — five roles.
- Sample Site: Bannerghatta Safari Site. Currency ₹, Indian regulatory idiom
  (CZA-style inspections, licences).
- Site layout persists under its **own** store key per role, so the existing
  saved module home page is never disturbed.

## 8 · Readiness Verdict — **YELLOW**

| # | Criterion | Met |
|---|---|---|
| 1 | Problem distinguished from symptom, root cause hypothesised | ✅ |
| 2 | ≥3 stakeholder roles incl. decider / actor / consumer | ✅ (7) |
| 3 | ≥1 decision in full Decision→Question→Insight→Action form | ✅ (11) |
| 4 | Success criteria stated | ✅ (7) |
| 5 | Scope boundary — what we are NOT solving | ✅ |
| 6 | Decision coverage — major decisions mapped, all classes | ✅ |

All six criteria are met. The verdict is **YELLOW rather than GREEN because of a
named risk**, not a gate failure:

> **Named risk — the role and permission taxonomy is invented, not sourced.**
> §4 assumes five roles whose real definitions live in ANTZ v5, unavailable
> here. Role-based defaults are the single most important requirement in the
> brief (§5 of the brief), so if the real taxonomy differs, the *defaults* are
> rework — though the *mechanism* (ranked list × permission filter) is not.
> **Mitigation:** hold role defaults as pure data — one ranked widget-id list
> per role — so a corrected taxonomy is a data edit rather than a redesign.

A second, lesser risk: **entry behaviour is unresolved** (Sites list vs. assigned
Site). It changes the first screen, so it is being put to the user rather than
assumed.

## 9 · Recommended Next Step

```
Recommended Next Doctrine : JARVIS  (execution design)
Recommended Next Skill    : deep-dive
Reason                    : the decision architecture is understood and the
                            engine to build on already exists; what is missing
                            is execution design — view routing, the Site widget
                            catalogue, role defaults as data, and the two or
                            three genuinely new compositions
Expected Output           : IA + navigation model · Site widget catalogue keyed
                            to §4 decisions · role default lists · permission
                            filter · phased build plan against index.html
```

### Handoff note — what execution should know before it starts

**The engine is already there.** Of the eleven widget types the brief asks for,
nine exist as layouts in `cardVariants.js`:

| Brief widget type | Existing layout |
|---|---|
| KPI | `stat` |
| Status | `status` |
| Progress | `progress` · `arc` · `meters` |
| List | `queue` |
| Trend | `chart` |
| Distribution | `ring` · `metrics` |
| Action | `attention` |
| Timeline | `timeline` |
| Map (hierarchy) | `hierarchy` |
| **Health** | **new** — wide: gauge + domain rows |
| **Insight** | **new** — restrained, operational, not an AI gimmick |

So the work is predominantly **catalogue data + a role layer + two new
compositions**, not a new application.

**Colour rule, extended rather than invented.** Today: *colour identifies a
module and does not vary within it.* For Site widgets: **colour identifies the
domain** (People, Finance, Assets, Utilities, Safety, Animal Operations),
mapped onto the existing closed 16-gradient palette. This satisfies the brief's
gradient requirement without re-opening a settled decision.

**Two invariants carry over** (handoff §4): the catalogue and the default
arrangement must agree in both directions — so the Site catalogue needs its own
`antz.checkSiteDefaults()`; and the Site layout needs its own store key and
version, so bumping one does not discard the other.

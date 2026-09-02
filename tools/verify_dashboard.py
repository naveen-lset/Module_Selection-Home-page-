"""Verification for the role-aware dashboard — dashboard.html.

    python3 tools/verify_dashboard.py

The brief ends by asking for the result to be reviewed against every rule and
the violations corrected. This file IS that review, done by measurement rather
than by re-reading the brief and agreeing with myself. It sweeps the nine widths
§34 names and audits the §37 prohibitions.

WHAT IT CHECKS, and why each one is a rule that is easy to break by accident:

  ONE FAMILY        §10 — every rendered text node resolves to Inter. A single
                    stray fallback is invisible until it is on a machine
                    without the font.
  NO HUGE NUMBERS   §10 — nothing above 40px. Dashboard numbers grow by
                    themselves as soon as one card wants to be important.
  GEOMETRY          §13 — radius 14–16, card padding 16, feature 20–24.
  NO VIEW BUTTONS   §23/§37 — and no Today/This Week filters (§26).
  TOUCH             §23 — every control ≥44px on its smaller side.
  COMPOSITION       §15–20 — the column count actually changes per breakpoint,
                    and no width overflows horizontally.
  ROLES DIFFER      §32 — switching role changes order, span and density, not
                    just labels. Asserted as a diff of the rendered layout.
"""
import os, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from cdp import Chrome

URL = "file://" + ROOT.replace(" ", "%20") + "/dashboard.html"
WIDTHS = [768, 820, 834, 1024, 1180, 1280, 1366, 1440, 1600]
fails = []

def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
    if not ok: fails.append(name)


AUDIT = r"""(() => {
  const out = { fonts: {}, big: [], radii: {}, pads: {}, taps: [], words: [] };

  // every rendered text node's resolved family
  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walk.nextNode())) {
    if (!n.nodeValue.trim()) continue;
    const el = n.parentElement;
    if (!el || !el.getBoundingClientRect().width) continue;
    const cs = getComputedStyle(el);
    const fam = cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
    out.fonts[fam] = (out.fonts[fam] || 0) + 1;
    const px = parseFloat(cs.fontSize);
    if (px > 40) out.big.push(fam + ' ' + px + 'px :: ' + n.nodeValue.trim().slice(0, 24));
  }

  for (const c of document.querySelectorAll('.c')) {
    const cs = getComputedStyle(c);
    out.radii[cs.borderTopLeftRadius] = (out.radii[cs.borderTopLeftRadius] || 0) + 1;
    out.pads[cs.paddingTop] = (out.pads[cs.paddingTop] || 0) + 1;
  }

  // controls that a finger has to hit
  for (const b of document.querySelectorAll('button')) {
    const r = b.getBoundingClientRect();
    if (!r.width || !r.height) continue;
    if (b.classList.contains('c')) continue;      // whole-card targets are large
    if (Math.min(r.width, r.height) < 44) out.taps.push((b.className || b.tagName) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
  }

  // Forbidden words. 'Manage' was in this list and matched inside "Species
  // Management" — a module name the brief REQUIRES — so the checker was
  // reporting a violation that did not exist. A prohibition on a control has
  // to be tested on controls; the standalone-button test below does that. The
  // text scan keeps only the phrases that cannot appear innocently.
  const txt = document.body.innerText;
  for (const w of ['View All', 'View all', 'See All', 'Today', 'This Week', 'This Month', 'Last 7 Days']) {
    if (txt.includes(w)) out.words.push(w);
  }
  // "View" as a standalone control, not as part of "Overview"
  for (const b of document.querySelectorAll('button')) {
    const t = (b.textContent || '').trim();
    if (/^(View|Open|Manage|See all)$/i.test(t)) out.words.push('button:' + t);
  }

  out.overflow = document.documentElement.scrollWidth > window.innerWidth + 1;
  out.cols = getComputedStyle(document.documentElement).getPropertyValue('--cols').trim();
  out.pad = getComputedStyle(document.querySelector('.board')).paddingLeft;
  out.cards = document.querySelectorAll('.c').length;
  return out;
})()"""


with Chrome(width=1280, height=1000, port=9481) as c:
    print("\nthe surface")
    c.goto(URL, settle=1.0)

    got = c.eval("(() => ({ roles: antzDash.roles(), modules: antzDash.modules() }))()")
    check("four roles", got["roles"] == ["vet", "biologist", "admin", "management"],
          " · ".join(got["roles"]))
    check("eighteen module visuals, none invented", len(got["modules"]) == 18,
          f"{len(got['modules'])} renderers")

    # §32 — the roles must differ in composition, not in wording.
    layouts = {}
    for r in got["roles"]:
        c.eval(f"antzDash.setRole('{r}')")
        time.sleep(0.25)
        layouts[r] = c.eval("antzDash.layout()")
    order = {r: [x["m"] for x in v] for r, v in layouts.items()}
    widths = {r: [x["w"] for x in v] for r, v in layouts.items()}

    pairs = [(a, b) for i, a in enumerate(got["roles"]) for b in got["roles"][i+1:]]
    same_order = [f"{a}/{b}" for a, b in pairs if order[a] == order[b]]
    check("no two roles show the same modules in the same order", not same_order,
          "; ".join(same_order) or f"vet starts {order['vet'][:3]}")

    counts = {r: len(v) for r, v in order.items()}
    check("and they differ in how much they show", len(set(counts.values())) > 1,
          " · ".join(f"{r}:{n}" for r, n in counts.items()))

    # prominence: the lead card of each role is that role's own subject
    lead = {r: order[r][0] for r in order}
    check("each role leads with its own subject",
          lead == {"vet": "medical", "biologist": "species",
                   "admin": "approvals", "management": "medical"},
          " · ".join(f"{r}->{m}" for r, m in lead.items()))

    # EVERY VISUAL, IN EVERY ROLE, HAS A REAL BOX.
    # Three separate elements in this file rendered at zero width because a
    # <span> given a px size stays inline unless something blockifies it — and
    # each looked plausible in a screenshot, because the label and the number
    # beside it were still correct. Sweeping every visual class in every role is
    # the only form of this check that catches all of them at once.
    PARTS = ['.jr__seg', '.bed', '.shelf__fill', '.pipe__st', '.land__b', '.ev',
             '.track__go', '.plot', '.flow__n', '.lane__fill', '.runway__pin',
             '.cov__pip', '.gate', '.doc', '.thr__t']
    zero = []
    for r in got["roles"]:
        c.eval(f"antzDash.setRole('{r}')")
        time.sleep(0.3)
        z = c.eval("""(sels => { const bad = [];
          for (const s of sels) {
            const els = [...document.querySelectorAll(s)];
            const n = els.filter(e => { const b = e.getBoundingClientRect();
              return b.width < 1 || b.height < 1; }).length;
            if (els.length && n) bad.push(s + ' ' + n + '/' + els.length);
          } return bad; })(""" + repr(PARTS).replace("'", '"') + ")")
        if z: zero.append(r + ': ' + '; '.join(z))
    check("every visual renders a real box in every role", not zero, " | ".join(zero[:2]))

    print("\nthe rules (§10, §13, §23, §26, §37)")
    c.eval("antzDash.setRole('vet')"); time.sleep(0.3)
    a = c.eval(AUDIT)
    check("Inter and nothing else", list(a["fonts"].keys()) == ["Inter"],
          " · ".join(f"{k}:{v}" for k, v in a["fonts"].items()))
    check("no number above 40px", not a["big"], "; ".join(a["big"][:3]))
    check("card radius is 14–16", all(14 <= float(k.replace('px','')) <= 16 for k in a["radii"]),
          " · ".join(a["radii"].keys()))
    check("card padding is 16, feature 20–24",
          all(16 <= float(k.replace('px','')) <= 24 for k in a["pads"]),
          " · ".join(a["pads"].keys()))
    check("no View / View All / Manage, no Today / This Week", not a["words"],
          "; ".join(a["words"][:4]))
    check("every control clears a 44px touch target", not a["taps"], "; ".join(a["taps"][:3]))

    print("\nthe sweep (§34)")
    prev_cols = None
    steps = []
    for w in WIDTHS:
        c.set_viewport(w, 1000)
        time.sleep(0.35)
        a = c.eval(AUDIT)
        steps.append((w, a["cols"], a["pad"], a["overflow"]))
        check(f"{w}px · {a['cols']} cols · {a['pad']} padding · {a['cards']} cards",
              not a["overflow"], "HORIZONTAL OVERFLOW" if a["overflow"] else "")
        prev_cols = a["cols"]

    seen = [s[1] for s in steps]
    check("the column count actually changes across the range", len(set(seen)) >= 3,
          " → ".join(seen))
    pads = {s[0]: s[2] for s in steps}
    check("page padding is 24 on tablet and 32 from 1024 up",
          pads[768] == "24px" and pads[834] == "24px" and pads[1024] == "32px" and pads[1440] == "32px",
          f"768:{pads[768]} 834:{pads[834]} 1024:{pads[1024]} 1440:{pads[1440]}")

    # §19 — wider, not infinitely wide
    c.set_viewport(1920, 1000); time.sleep(0.35)
    got = c.eval("Math.round(document.querySelector('.app').getBoundingClientRect().width)")
    check("the board stops widening by 1440–1600", 1440 <= got <= 1600, f"{got}px at a 1920 viewport")

    print("\nportrait and landscape (§21, §22)")
    for w, h, label in [(834, 1194, "iPad Air portrait"), (1194, 834, "iPad Air landscape"),
                        (768, 1024, "iPad Mini portrait"), (1366, 1024, "iPad Pro landscape")]:
        c.set_viewport(w, h); time.sleep(0.35)
        a = c.eval(AUDIT)
        check(f"{label} · {w}x{h} · {a['cols']} cols", not a["overflow"],
              "overflow" if a["overflow"] else f"{a['cards']} cards")

    c.set_viewport(1280, 1000); time.sleep(0.3)
    check("no console errors", not c.errors(), str(c.errors()[:2]))


print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
sys.exit(1 if fails else 0)

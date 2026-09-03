"""Verification for the two search sheets at tablet and desktop widths.

    python3 tools/verify_sheets.py

The complaint was dead space: a 460px phone sheet centred on the bottom edge
of a 1280 screen, with ~410px of empty scrim either side. Widening it is easy
to claim and easy to get wrong, so this measures the four things that decide
whether the width was actually SPENT:

  IT FILLS THE SCREEN   the sheet's own width per breakpoint, and the scrim
                        left over either side of it. A sheet that grew but
                        left 400px of gutter has not fixed the complaint.
  STILL A BOTTOM SHEET  the design draws bottom sheets and the chosen fix
                        keeps them. Asserted as the bottom edge touching the
                        viewport, exactly as verify_search.py does.
  THE ROW COLLAPSED     scope control and tag search share a row from 768 up
                        — same centre-line y, not merely both present — and
                        the sheet is SHORTER than the stacked version was.
  CONTROLS KEPT SCALE   Cancel/Done and the segmented halves must not scale
                        with the dialog. A 450px-wide Done is a banner. Every
                        one is measured against a ceiling, and the tag cloud
                        is measured for rows saved.

Reduced motion is forced, as in tools/verify.py: the sheet's transform is a
420ms transition and a box read mid-flight is a box read at the wrong place.
"""
import os, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from cdp import Chrome

URL = "file://" + ROOT.replace(" ", "%20") + "/index.html"
fails = []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
    if not ok:
        fails.append(name)


BOX = """(() => {
  const el = document.querySelector(%s);
  if (!el) return { there: false };
  const r = el.getBoundingClientRect();
  return { there: true, w: Math.round(r.width), h: Math.round(r.height),
           top: Math.round(r.top), left: Math.round(r.left),
           right: Math.round(r.right), mid: Math.round(r.top + r.height / 2) };
})()"""

# 460 was the old width at every breakpoint; each entry is what the sheet is
# expected to reach now, and the gutter it is allowed to leave.
STEPS = [
    (768,  "tablet",          720, 40),
    (834,  "iPad Air",        720, 80),
    (1024, "desktop",         960, 40),
    (1280, "desktop wide",    960, 170),
    (1440, "desktop wider",   960, 250),
]

with Chrome(width=1280, height=1400, reduced_motion=True) as c:
    c.goto(URL, settle=0.9)

    print("\nthe phone width is still the phone width")
    c.set_viewport(430, 932)
    time.sleep(0.3)
    c.click('.search')
    time.sleep(0.4)
    c.eval('(() => document.querySelector("[data-open=\'tag\']").click())()')
    time.sleep(0.5)
    got = c.eval(BOX % "'.gsx-sheet--tags'")
    check("at 430px the sheet is the full viewport, as it was",
          got["there"] and got["w"] >= 429, f"{got['w']}x{got['h']} of 430")
    stacked = c.eval("""(() => {
      const t = document.querySelector('.gsx-sheet--tags .gsx-tabs');
      const s = document.querySelector('.gsx-sheet--tags .gsx-tagsearch');
      const a = t.getBoundingClientRect(), b = s.getBoundingClientRect();
      return { stacked: b.top >= a.bottom - 1, h: Math.round(
        document.querySelector('.gsx-sheet--tags').getBoundingClientRect().height) };
    })()""")
    check("and its scope control and search are still stacked",
          stacked["stacked"], f"sheet {stacked['h']}px tall")
    phone_h = stacked["h"]

    for w, label, want_w, max_gutter in STEPS:
        print(f"\n{w}px · {label}")
        c.set_viewport(w, 1400)
        time.sleep(0.45)
        got = c.eval(BOX % "'.gsx-sheet--tags'")
        vw = c.eval("innerWidth"); vh = c.eval("innerHeight")
        check("the sheet reaches its width for this breakpoint",
              got["w"] >= min(want_w, vw) - 2, f"{got['w']}px of a {vw}px viewport")
        gutter = min(got["left"], vw - got["right"])
        check("without leaving dead scrim either side",
              gutter <= max_gutter, f"{gutter}px each side (was {(vw - 460) // 2}px at 460)")
        check("and it is still a bottom sheet",
              abs((got["top"] + got["h"]) - vh) <= 2,
              f"bottom at {got['top'] + got['h']} of {vh}")

        row = c.eval("""(() => {
          const t = document.querySelector('.gsx-sheet--tags .gsx-tabs');
          const s = document.querySelector('.gsx-sheet--tags .gsx-tagsearch');
          const a = t.getBoundingClientRect(), b = s.getBoundingClientRect();
          const tabs = [...document.querySelectorAll('.gsx-sheet--tags .gsx-tab')]
            .map(e => Math.round(e.getBoundingClientRect().width));
          const btns = [...document.querySelectorAll('.gsx-sheet--tags .gsx-btn')]
            .map(e => Math.round(e.getBoundingClientRect().width));
          const pills = [...document.querySelectorAll('.gsx-sheet--tags .gsx-tag')];
          const rows = new Set(pills.map(e => Math.round(e.getBoundingClientRect().top)));
          return { sameRow: Math.abs((a.top + a.height / 2) - (b.top + b.height / 2)) <= 2,
                   sideBySide: b.left >= a.right - 1,
                   tabH: Math.round(a.height), searchH: Math.round(b.height),
                   tabs, btns, tagRows: rows.size, pills: pills.length };
        })()""")
        check("the scope control and the tag search share one row",
              row["sameRow"] and row["sideBySide"],
              f"tabs {row['tabH']}px · field {row['searchH']}px, on one centre-line")
        check("both halves of the segmented control keep their size",
              len(row["tabs"]) == 2 and max(row["tabs"]) <= 260
              and abs(row["tabs"][0] - row["tabs"][1]) <= 2, f"{row['tabs']}")
        check("Cancel and Done stay buttons, not banners",
              len(row["btns"]) == 2 and max(row["btns"]) <= 260, f"{row['btns']}")
        check("the tag cloud spends the width on fewer rows",
              row["tagRows"] <= 8, f"{row['pills']} tags over {row['tagRows']} rows")
        check("and the sheet is shorter than the phone's",
              got["h"] < phone_h, f"{got['h']}px vs {phone_h}px at 430")

        # THE OTHER SHEET. It shares createSheet() and the same .gsx-sheet
        # width, so a fix that reached only one of them would put two sheets
        # at two widths on the same surface.
        c.eval("(() => document.querySelector('.gsx-sheet--tags .gsx-sheet__close').click())()")
        time.sleep(0.35)
        c.eval("""(() => { const i = document.querySelector('.gsx__input');
          i.value = '@'; i.dispatchEvent(new InputEvent('input',{bubbles:true})); })()""")
        time.sleep(0.5)
        t = c.eval(BOX % "'.gsx-sheet--type'")
        vh2 = c.eval("innerHeight")
        check("Choose Search Type is the same width, not left at 460",
              t["there"] and abs(t["w"] - got["w"]) <= 2, f"{t['w']}px vs the tag sheet's {got['w']}px")
        check("and it is a bottom sheet too",
              abs((t["top"] + t["h"]) - vh2) <= 2, f"bottom at {t['top'] + t['h']} of {vh2}")
        cols = c.eval("""(() => {
          const o = [...document.querySelectorAll('.gsx-opt')];
          const tops = new Set(o.map(e => Math.round(e.getBoundingClientRect().top)));
          return { n: o.length, rows: tops.size,
                   w: Math.max(...o.map(e => Math.round(e.getBoundingClientRect().width))) };
        })()""")
        check("its eight rows go two-up rather than stretching",
              cols["n"] == 8 and cols["rows"] == 4 and cols["w"] <= 480,
              f"{cols['n']} rows in {cols['rows']} lines, widest {cols['w']}px")
        c.eval("(() => document.querySelector('.gsx-sheet--type .gsx-sheet__close').click())()")
        time.sleep(0.3)
        c.eval("""(() => { const i = document.querySelector('.gsx__input');
          i.value = ''; i.dispatchEvent(new InputEvent('input',{bubbles:true})); })()""")
        time.sleep(0.2)
        c.eval('(() => document.querySelector("[data-open=\'tag\']").click())()')
        time.sleep(0.5)

    # ══ THE DESIGN REVIEW'S FINDINGS ════════════════════════════════════
    # Fourteen findings were applied. Each one below is the ASSERT that stops
    # it coming back, measured the way the review measured it in the first
    # place — a ratio computed from rendered pixels, a target proved with
    # elementFromPoint, a key actually dispatched.
    c.set_viewport(1280, 1400)
    time.sleep(0.45)

    print("\ncontrast (WCAG AA, computed from rendered colour)")
    CONTRAST = r"""(() => {
      const lum = (r,g,b) => { const f = v => { v/=255;
        return v<=0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055,2.4) };
        return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b) };
      const parse = s => { const m = String(s).match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?/);
        return m ? [ +m[1], +m[2], +m[3], m[4]===undefined?1:+m[4] ] : null };
      const bgOf = el => { let n = el;
        while (n && n !== document.documentElement) {
          const c = parse(getComputedStyle(n).backgroundColor);
          if (c && c[3] > 0.95) return c; n = n.parentElement } return [255,255,255,1] };
      const ratio = (el) => { const cs = getComputedStyle(el);
        const fg = parse(cs.color), bg = bgOf(el);
        const f = [0,1,2].map(i => Math.round(fg[i]*fg[3] + bg[i]*(1-fg[3])));
        const L1 = lum(...f), L2 = lum(...bg);
        return +(((Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05))).toFixed(2) };
      const one = s => { const el = document.querySelector(s); return el ? ratio(el) : null };
      return { note: one('.gsx-sheet--tags .gsx-sheet__note'),
               done: one('.gsx-sheet--tags .gsx-btn--go'),
               cancel: one('.gsx-sheet--tags .gsx-btn--ghost'),
               tabOn: one('.gsx-sheet--tags .gsx-tab.is-on'),
               key: one('.gsx__key') };
    })()"""
    r = c.eval(CONTRAST)
    for name, label in [("note", "the sheet's own subtitle"), ("done", "Done, white on green"),
                        ("cancel", "Cancel, green on white"), ("tabOn", "the selected scope tab"),
                        ("key", "the keyboard bar's labels")]:
        check(f"{label} clears 4.5:1", r[name] is not None and r[name] >= 4.5,
              f"{r[name]}:1")

    print("\ntap targets (44px floor, proved by hit-testing not by CSS)")
    HIT = r"""(() => {
      const probe = (sel) => {
        const el = document.querySelector(sel);
        if (!el) return null;
        const b = el.getBoundingClientRect();
        const a = getComputedStyle(el, '::after');
        const px = v => parseFloat(v) || 0;
        const h = b.height - px(a.top) - px(a.bottom);
        const w = b.width - px(a.left) - px(a.right);
        // The real question is not the box, it is whether a finger 4px above
        // the visible edge actually lands on this control.
        const y = b.top - 4, x = b.left + b.width / 2;
        const hitEl = document.elementFromPoint(x, y);
        return { h: Math.round(h), w: Math.round(w),
                 side: Math.round(Math.min(h, w)),
                 hits: !!hitEl && (hitEl === el || el.contains(hitEl) || hitEl.closest(sel) === el) };
      };
      return { tag: probe('.gsx-sheet--tags .gsx-tag'),
               close: probe('.gsx-sheet--tags .gsx-sheet__close') };
    })()"""
    r = c.eval(HIT)
    check("a tag pill's target reaches 44px", r["tag"]["side"] >= 44,
          f"{r['tag']['w']}x{r['tag']['h']} target on a 32px pill")
    check("and a press 4px above the pill still lands on it", r["tag"]["hits"])
    check("the close button's target reaches 44px", r["close"]["side"] >= 44,
          f"{r['close']['w']}x{r['close']['h']} on a 32px button")

    print("\nfocus is put in, held, and given back")
    got = c.eval("""(() => {
      const s = document.querySelector('.gsx-sheet--tags');
      const a = document.activeElement;
      return { inside: s.contains(a),
               active: a ? a.tagName.toLowerCase() + '.' + String(a.className).split(' ')[0] : null,
               behindInert: !!document.querySelector('.gsx[inert]') };
    })()""")
    check("opening the sheet puts focus inside it", got["inside"], got["active"])
    check("and makes the page behind it inert", got["behindInert"])

    got = c.eval("""(() => {
      const list = [...document.querySelectorAll('.gsx-sheet--tags button, .gsx-sheet--tags input')]
        .filter(e => e.getBoundingClientRect().width > 0);
      const last = list[list.length - 1];
      last.focus();
      last.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab', bubbles: true }));
      return { wrapped: document.activeElement === list[0],
               n: list.length,
               to: String(document.activeElement.className).split(' ')[0] };
    })()""")
    check("Tab off the last control wraps to the first, not out of the dialog",
          got["wrapped"], f"{got['n']} focusables, landed on .{got['to']}")

    # ESCAPE. The bug was that it did nothing at all, because focus had never
    # been inside the sheet for the sheet's own handler to hear the key.
    c.eval("""(() => { document.activeElement.dispatchEvent(
      new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); })()""")
    time.sleep(0.7)
    got = c.eval("""(() => ({
      closed: document.querySelector('.gsx-sheet--tags').hidden,
      unInert: !document.querySelector('.gsx[inert]'),
      back: document.activeElement ? String(document.activeElement.className).split(' ')[0] : null,
    }))()""")
    check("Escape closes the sheet", got["closed"])
    check("and the page behind is interactive again", got["unInert"])
    check("and focus is back on the page, not lost to <body>",
          got["back"] not in (None, ""), f".{got['back']}")

    print("\nthe scope control says what it is")
    c.eval('(() => document.querySelector("[data-open=\'tag\']").click())()')
    time.sleep(0.6)
    got = c.eval("""(() => {
      const g = document.querySelector('.gsx-sheet--tags .gsx-tabs');
      const b = [...g.querySelectorAll('.gsx-tab')];
      b[1].click();
      return { group: g.getAttribute('role'), labelled: !!g.getAttribute('aria-label'),
               roles: b.map(x => x.getAttribute('role')),
               checked: b.map(x => x.getAttribute('aria-checked')),
               painted: b.map(x => x.classList.contains('is-on')),
               staleTabRole: b.some(x => x.getAttribute('role') === 'tab') };
    })()""")
    check("it is a radiogroup with a name, not an unfinished tablist",
          got["group"] == "radiogroup" and got["labelled"] and not got["staleTabRole"],
          f"role={got['group']}, roles={got['roles']}")
    check("and aria-checked follows the painted state",
          got["checked"] == ["false", "true"] and got["painted"] == [False, True],
          f"checked={got['checked']} painted={got['painted']}")

    print("\n320px, the narrowest the rubric asks for")
    c.set_viewport(320, 800)
    time.sleep(0.6)
    got = c.eval("""(() => {
      const de = document.documentElement;
      // An element wider than the viewport is only a BUG if it pushes the
      // page. Inside an overflow-x scroller it is the whole point — the two
      // search rails are exactly that, and the first version of this assert
      // called them a defect. So walk up and forgive anything that sits in
      // a real horizontal scroller.
      // Contained by a scroller OR by a clip. Both versions of this assert
      // before this one cried wolf: first at the search rails (overflow-x
      // auto, so extending past the viewport IS the feature), then at a
      // 300px decorative card watermark sitting inside `overflow: hidden`
      // and clipped at 154px. Neither paints outside, neither pushes the
      // page. The rule that actually catches a bug is: wider than the
      // viewport AND nothing above it cuts it off.
      const contained = (el) => {
        let n = el.parentElement;
        while (n && n !== document.documentElement) {
          const o = getComputedStyle(n).overflowX;
          if (o === 'auto' || o === 'scroll' || o === 'hidden' || o === 'clip') return true;
          n = n.parentElement;
        }
        return false;
      };
      const name = e => (e.tagName.toLowerCase() + '.' +
        String(e.className && e.className.baseVal !== undefined ? e.className.baseVal
               : e.className).split(' ')[0]).slice(0, 30);
      const off = [...document.querySelectorAll('body *')]
        .filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.right > 321 })
        .filter(e => !contained(e))
        .map(name);
      return { scrollW: de.scrollWidth, clientW: de.clientWidth,
               scrollsX: de.scrollWidth > de.clientWidth,
               worst: [...new Set(off)].slice(0, 4) };
    })()""")
    check("the page does not scroll sideways",
          not got["scrollsX"], f"scrollWidth {got['scrollW']} vs client {got['clientW']}")
    check("and nothing sticks out past the viewport", not got["worst"], str(got["worst"]))
    # The switcher this used to inspect was removed with Figma node 135:4436.
    # Its `minmax(0, 1fr)` fix went with it, and the horizontal-scroll bug it
    # fixed cannot recur because the element no longer exists — so the assert
    # above (the page does not scroll sideways) is the whole check now.
    c.set_viewport(1280, 1400)
    time.sleep(0.4)

    print("\nnothing broke on the way")
    errs = c.errors()
    check("no console errors through any of it", not errs, str(errs[:3]))

print()
if fails:
    print(f"{len(fails)} FAILED")
    for f in fails:
        print("  · " + f)
    sys.exit(1)
print("ALL PASS")

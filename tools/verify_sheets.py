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

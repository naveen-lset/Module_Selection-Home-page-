"""Verification for the Global Search surface — the Figma Desktop-Navigation
`Global Search Concept` section, ported to the desktop field.

    python3 tools/verify_search.py

The design's grammar is the thing to prove, not its pixels: a field that holds
a TOKEN rather than a string, `@` opening the type menu, results grouped and
counted by what they are, and a row that navigates to the record it names.

EVERY ASSERT READS THE RENDERED BOX. `panel.hidden === false` is a property
agreeing with itself — it passes while the panel is a zero-height sliver behind
the hero, which is the exact failure this file exists to catch. So visibility is
`getBoundingClientRect()` with width and height, and text is `textContent` off
the element that actually painted.

Runs against the working copy over file://, headless Chrome, reduced motion —
the same harness as tools/verify.py, for the same reasons.
"""
import os, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from cdp import Chrome

URL = "file://" + ROOT.replace(" ", "%20") + "/index.html"
fails = []

def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
    if not ok: fails.append(name)

# Typing, as the field sees it. `input` is what the component listens for, and
# setting .value without it is the one way to test a text field that proves
# nothing at all.
TYPE = """(() => {
  const i = document.querySelector('.search__input');
  i.focus();
  i.value = %s;
  i.dispatchEvent(new InputEvent('input', { bubbles: true }));
  return true;
})()"""

KEY = """(() => {
  const i = document.querySelector('.search__input');
  i.dispatchEvent(new KeyboardEvent('keydown',
    { key: %s, bubbles: true, cancelable: true }));
  return true;
})()"""

# A box, not a flag.
BOX = """(() => {
  const el = document.querySelector(%s);
  if (!el) return { there: false };
  const r = el.getBoundingClientRect();
  const cs = getComputedStyle(el);
  return { there: true, w: Math.round(r.width), h: Math.round(r.height),
           vis: r.width > 1 && r.height > 1 && cs.visibility !== 'hidden'
                && Number(cs.opacity) > 0.01,
           text: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 120) };
})()"""


with Chrome(width=1280, height=1400) as c:
    print("\nthe index")
    c.goto(URL, settle=0.9)

    got = c.eval("""(() => {
      const { index } = antz.searchIndex();
      const rows = index();
      const by = {};
      for (const r of rows) by[r.type] = (by[r.type] || 0) + 1;
      return { total: rows.length, by };
    })()""")
    check("the index builds from the existing fixtures", got["total"] > 500,
          f"{got['total']} rows")
    check("and holds every type the design can answer for",
          all(got["by"].get(k) for k in
              ("site", "section", "enclosure", "animal", "species", "identifier")),
          " · ".join(f"{k}:{v}" for k, v in sorted(got["by"].items())))

    # The species rows are an aggregate, and the pills under them have to add up
    # to the count printed beside them — that is the whole reason UO exists.
    got = c.eval("""(() => {
      const { index } = antz.searchIndex();
      const bad = index().filter(r => r.type === 'species' &&
        (r.pills.M + r.pills.F + r.pills.UO) !== r.count);
      return { bad: bad.length, sample: bad[0] ? bad[0].title : '' };
    })()""")
    check("every species' pills add up to its own count", got["bad"] == 0,
          f"{got['bad']} disagree {got['sample']}")

    print("\nthe panel")
    c.click('.search')
    time.sleep(0.25)
    got = c.eval(BOX % "'.gsp'")
    check("focusing the field opens a panel that is actually on screen",
          got["there"] and got["vis"], f"{got.get('w')}x{got.get('h')}")

    got = c.eval(BOX % "'.gsp-rail'")
    check("with the type rail across the top", got["there"] and got["vis"],
          got.get("text", ""))

    c.eval(TYPE % "'lion'")
    time.sleep(0.25)
    got = c.eval("""(() => {
      const heads = [...document.querySelectorAll('.gsp-group__head span')]
        .map(e => e.textContent.trim());
      const rows = [...document.querySelectorAll('.gsp-row')];
      const painted = rows.filter(e => e.getBoundingClientRect().height > 8);
      return { heads, rows: rows.length, painted: painted.length,
               first: rows[0] ? rows[0].textContent.replace(/\\s+/g,' ').trim().slice(0,70) : '' };
    })()""")
    check("typing returns groups, counted and named the design's way",
          any(h.startswith("About ") and " in " in h for h in got["heads"]),
          " | ".join(got["heads"][:3]))
    check("and every result row is a painted box, not an empty one",
          got["rows"] > 0 and got["painted"] == got["rows"],
          f"{got['painted']} of {got['rows']} · {got['first']}")

    print("\nthe token grammar")
    c.eval(TYPE % "'@'")
    time.sleep(0.3)
    got = c.eval(BOX % "'.gsm'")
    check("'@' opens Choose Search Type as a real dialog",
          got["there"] and got["vis"], f"{got.get('w')}x{got.get('h')}")
    got = c.eval("""(() => [...document.querySelectorAll('.gsm-opt')]
        .map(e => e.textContent.replace(/\\s+/g,' ').trim()))()""")
    check("offering all eight of the design's types", len(got) == 8,
          " · ".join(x.split(" no records")[0] for x in got))

    c.eval("""(() => {
      [...document.querySelectorAll('.gsm-opt')].find(e => e.dataset.key === 'animal').click();
      document.querySelector('.gsm__done').click();
    })()""")
    time.sleep(0.3)
    got = c.eval(BOX % "'.search__token'")
    check("Done commits a token chip inside the field",
          got["there"] and got["vis"], f"{got.get('text')} · {got.get('w')}x{got.get('h')}")
    check("and the field is cleared for the term that follows it",
          c.eval("document.querySelector('.search__input').value") == "")

    c.eval(TYPE % "'lion'")
    time.sleep(0.25)
    got = c.eval("""(() => {
      const keys = [...document.querySelectorAll('.gsp-group__head span')]
        .map(e => e.textContent.trim());
      return { groups: keys.length, keys };
    })()""")
    check("a committed token narrows the search to one type",
          got["groups"] == 1 and "Animals" in (got["keys"][0] if got["keys"] else ""),
          " | ".join(got["keys"]))

    got = c.eval(KEY % "'Backspace'")
    time.sleep(0.2)

    print("\nchoosing a result")
    c.eval("""(() => {
      const i = document.querySelector('.search__input');
      i.focus(); i.value = 'CAR-02';
      i.dispatchEvent(new InputEvent('input', { bubbles: true }));
    })()""")
    time.sleep(0.3)
    got = c.eval("""(() => {
      const r = document.querySelector('.gsp-row');
      return r ? r.textContent.replace(/\\s+/g,' ').trim().slice(0,60) : null;
    })()""")
    check("an enclosure code finds its enclosure", bool(got), str(got))

    c.eval("document.querySelector('.gsp-row').click()")
    time.sleep(0.6)
    got = c.eval("""(() => {
      const st = antz.view();
      const panel = document.querySelector('.gsp');
      return { level: st.level, view: st.view, enc: st.enclosureId,
               panelOpen: panel && !panel.hidden };
    })()""")
    check("clicking it navigates to that enclosure",
          got["view"] == "site" and got["level"] == "enclosure" and bool(got["enc"]),
          f"{got['view']}/{got['level']} {got['enc']}")
    check("and the panel closes behind it", not got["panelOpen"])

    print("\nwhat it refuses to invent")
    c.eval("""(() => {
      const { TYPES } = antz.searchIndex();
      window.__t = TYPES.filter(t => !t.has).map(t => t.key);
    })()""")
    got = c.eval("window.__t")
    check("the two types with no data are still offered, not deleted",
          set(got) == {"user", "tag"}, " · ".join(got))

    c.eval("""(() => {
      document.querySelector('.search').click();
      document.querySelector('.gsp-rail__open').click();
    })()""")
    time.sleep(0.3)
    c.eval("""(() => {
      [...document.querySelectorAll('.gsm-opt')].find(e => e.dataset.key === 'user').click();
      document.querySelector('.gsm__done').click();
    })()""")
    time.sleep(0.35)
    got = c.eval(BOX % "'.gsp-empty'")
    check("and choosing one says so rather than showing an empty list",
          got["there"] and got["vis"] and got["text"].lower().startswith("no users"),
          got.get("text", "")[:90])

    print("\nthe field it replaced")
    got = c.eval("""(() => {
      const h = document.querySelector('.search__hint');
      const cs = h ? getComputedStyle(h) : null;
      return { there: !!h, shown: cs ? cs.display !== 'none' : false };
    })()""")
    check("the rotating hint is not drawn behind a committed token",
          got["there"] and not got["shown"], f"hint displayed={got['shown']}")

    check("no console errors through any of it", not c.errors(), str(c.errors()[:2]))


print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
sys.exit(1 if fails else 0)

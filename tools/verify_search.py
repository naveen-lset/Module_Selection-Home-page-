"""Verification for the Global Search PAGE — the Figma Desktop-Navigation
`Global Search Concept` section.

    python3 tools/verify_search.py

The design draws a surface with its own back arrow, its own scope control, a
field, TWO rails and grouped results — and two bottom sheets behind it. This
asserts the grammar of that surface, not its pixels:

  A PAGE, NOT A PANEL   the header field is a trigger; the surface covers the
                        viewport and the page underneath survives the trip.
  TWO RAILS, TWO RULES  type is one-at-a-time (a thing cannot be both an animal
                        and an enclosure); tags are many-at-once and NARROW.
  SHEETS SLIDE          Choose Search Type and Select Tags are bottom sheets in
                        the design, and share the product's existing sheet
                        motion rather than inventing a fourth kind of modal.

EVERY ASSERT READS THE RENDERED BOX. `hidden === false` is a property agreeing
with itself — it passes while the surface is a zero-height sliver. So visibility
is getBoundingClientRect with width and height, and text comes off the element
that actually painted.
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

TYPE = """(() => {
  const i = document.querySelector('.gsx__input');
  i.focus(); i.value = %s;
  i.dispatchEvent(new InputEvent('input', { bubbles: true }));
  return true;
})()"""

BOX = """(() => {
  const el = document.querySelector(%s);
  if (!el) return { there: false };
  const r = el.getBoundingClientRect();
  const cs = getComputedStyle(el);
  return { there: true, w: Math.round(r.width), h: Math.round(r.height),
           top: Math.round(r.top),
           vis: r.width > 1 && r.height > 1 && cs.visibility !== 'hidden'
                && Number(cs.opacity) > 0.01,
           text: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 110) };
})()"""

HEADS = """(() => [...document.querySelectorAll('.gsx-group__head span')]
    .map(e => e.textContent.trim()))()"""


with Chrome(width=1280, height=1400) as c:
    print("\nthe index")
    c.goto(URL, settle=0.9)

    got = c.eval("""(() => {
      const { index } = antz.searchIndex();
      const rows = index(); const by = {};
      for (const r of rows) by[r.type] = (by[r.type] || 0) + 1;
      return { total: rows.length, by };
    })()""")
    check("the index builds from the existing fixtures", got["total"] > 500, f"{got['total']} rows")
    check("and holds every type the design can answer for",
          all(got["by"].get(k) for k in
              ("site", "section", "enclosure", "animal", "species", "identifier")),
          " · ".join(f"{k}:{v}" for k, v in sorted(got["by"].items())))

    got = c.eval("""(() => {
      const { index } = antz.searchIndex();
      const bad = index().filter(r => r.type === 'species' &&
        (r.pills.M + r.pills.F + r.pills.UO) !== r.count);
      return { bad: bad.length };
    })()""")
    check("every species' pills add up to its own count", got["bad"] == 0, f"{got['bad']} disagree")

    print("\nit is a page, not a panel")
    c.click('.search')
    time.sleep(0.5)
    got = c.eval(BOX % "'.gsx'")
    vw = c.eval("innerWidth"); vh = c.eval("innerHeight")
    check("the header field opens a full surface",
          got["there"] and got["vis"] and got["w"] >= vw - 1 and got["h"] >= vh - 1,
          f"{got['w']}x{got['h']} in a {vw}x{vh} viewport")
    check("with its own back control and scope",
          c.eval("!!document.querySelector('.gsx__back') && !!document.querySelector('.gsx__scope')"))
    got = c.eval(BOX % "'.gsx__scope'")
    check("the scope names what is being searched", got["there"] and got["vis"], got["text"])
    check("and the page underneath is held still",
          c.eval("getComputedStyle(document.body).overflow") == "hidden")

    # WHITE, asserted as a colour rather than as "not the old one". A list of
    # text rows reads on the ground the rows sit on; the app's mint is for the
    # page of coloured cards. Parsed from rgb() so a rewrite to a token, a hex
    # or a colour function all still satisfy it.
    got = c.eval("""(() => {
      const m = getComputedStyle(document.querySelector('.gsx')).backgroundColor
        .match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
      return m ? [Number(m[1]), Number(m[2]), Number(m[3])] : null;
    })()""")
    check("the ground is white", got == [255, 255, 255], str(got))

    # The keys were built and never mentioned. The bar is what makes them real.
    got = c.eval("""(() => {
      const bar = document.querySelector('.gsx__keys');
      if (!bar) return { there: false };
      const r = bar.getBoundingClientRect();
      return { there: true, vis: r.width > 1 && r.height > 1,
               text: bar.textContent.replace(/\s+/g, ' ').trim(),
               keys: bar.querySelectorAll('kbd').length };
    })()""")
    check("the keyboard bar names the moves that already worked",
          got["there"] and got["vis"] and got["keys"] >= 4
          and all(w in got["text"] for w in ("Move", "Select", "Quit")),
          f"{got.get('text')} ({got.get('keys')} keys)")

    print("\ntwo rails, two rules")
    got = c.eval(BOX % '"[data-rail=\'type\']"')
    check("a type rail", got["there"] and got["vis"], got["text"][:64])
    got = c.eval(BOX % '"[data-rail=\'tag\']"')
    check("and a tag rail beside it", got["there"] and got["vis"], got["text"][:64])

    c.eval(TYPE % "'lion'")
    time.sleep(0.35)
    got = c.eval(HEADS)
    check("typing groups and counts the design's way",
          any(h.startswith("About ") and " in " in h for h in got), " | ".join(got[:3]))

    rows = c.eval("""(() => {
      const r = [...document.querySelectorAll('.gsx-row')];
      return { n: r.length, painted: r.filter(e => e.getBoundingClientRect().height > 8).length,
               first: r[0] ? r[0].textContent.replace(/\\s+/g,' ').trim().slice(0,60) : '' };
    })()""")
    check("and every row is a painted box", rows["n"] > 0 and rows["painted"] == rows["n"],
          f"{rows['painted']} of {rows['n']} · {rows['first']}")

    c.eval('(() => document.querySelector(".gsx-chip[data-type=\'animal\']").click())()')
    time.sleep(0.3)
    got = c.eval(HEADS)
    check("a type chip narrows to that one type", len(got) == 1 and "Animals" in got[0],
          " | ".join(got))
    c.eval('(() => document.querySelector(".gsx-chip[data-type=\'species\']").click())()')
    time.sleep(0.3)
    got = c.eval(HEADS)
    check("and picking a second REPLACES the first, never both",
          len(got) == 1 and "Species" in got[0], " | ".join(got))
    c.eval('(() => document.querySelector(".gsx-chip[data-type=\'species\']").click())()')
    time.sleep(0.3)

    print("\ntags — the half that was missing")
    got = c.eval("(() => antz.searchIndex().TAGS.length)()")
    check("the design's tag vocabulary is in the build", got >= 30, f"{got} tags")
    got = c.eval("""(() => {
      const T = antz.searchIndex().TAGS;
      return { pub: T.filter(t => t.scope === 'public').length,
               priv: T.filter(t => t.scope === 'private').length,
               tones: [...new Set(T.map(t => t.tone))].sort() };
    })()""")
    check("split public / private, in three tone families as the sheet draws them",
          got["pub"] >= 25 and got["priv"] >= 1 and len(got["tones"]) == 3,
          f"{got['pub']} public · {got['priv']} private · {got['tones']}")

    c.eval("""(() => { const i = document.querySelector('.gsx__input');
      i.value = ''; i.dispatchEvent(new InputEvent('input',{bubbles:true})); })()""")
    time.sleep(0.25)
    c.eval('(() => document.querySelector("[data-open=\'tag\']").click())()')
    time.sleep(0.7)
    got = c.eval(BOX % "'.gsx-sheet--tags'")
    ih = c.eval("innerHeight")
    check("Select Tags opens as a real sheet", got["there"] and got["vis"], f"{got['w']}x{got['h']}")
    check("sitting on the bottom edge, being a bottom sheet",
          abs((got["top"] + got["h"]) - ih) <= 2, f"bottom at {got['top'] + got['h']} of {ih}")

    # GEOMETRY IS NOT PAINT ORDER. The first build of this had the sheet
    # correctly placed, fully opaque, and rendered UNDERNEATH its own blurred
    # scrim — every box assert above passes on that. So ask the document what
    # is actually on top at the sheet's own centre.
    got2 = c.eval("""(() => {
      const s = document.querySelector('.gsx-sheet--tags');
      const r = s.getBoundingClientRect();
      const top = document.elementFromPoint(Math.round(r.left + r.width / 2),
                                            Math.round(r.top + 30));
      return { inside: !!top && s.contains(top),
               hit: top ? (top.className || top.tagName) : null };
    })()""")
    check("and is painted ON TOP of its own scrim, not under it",
          got2["inside"], f"topmost element there is {got2['hit']}")

    got = c.eval("""(() => ({
      tabs: [...document.querySelectorAll('.gsx-tab')].map(e => e.textContent.trim()),
      search: !!document.querySelector('.gsx-tagsearch input'),
      tags: document.querySelectorAll('.gsx-tag').length,
      foot: [...document.querySelectorAll('.gsx-sheet--tags .gsx-btn')].map(e => e.textContent.trim()),
    }))()""")
    check("with Public / Private, a tag search, and Cancel / Done",
          got["tabs"] == ["Public Tags", "Private Tags"] and got["search"]
          and got["tags"] > 20 and got["foot"] == ["Cancel", "Done"],
          f"{got['tags']} tags · {got['foot']}")

    c.eval('(() => document.querySelector(".gsx-tag[data-tag=\'Breeding\']").click())()')
    time.sleep(0.2)
    check("a tag ticks green inside the sheet",
          c.eval('document.querySelector(".gsx-tag[data-tag=\'Breeding\']").classList.contains("is-on")'))

    c.eval('(() => document.querySelector(".gsx-sheet--tags [data-tag=\'done\']").click())()')
    time.sleep(0.7)
    got = c.eval(HEADS)
    check("Done filters the results by that tag", len(got) >= 1, " | ".join(got[:2]))
    tot1 = c.eval("""(() => { const h = document.querySelector('.gsx-group__head span');
      return h ? Number((h.textContent.match(/About (\\d+)/) || [0,0])[1]) : 0 })()""")

    c.eval('(() => document.querySelector("[data-open=\'tag\']").click())()')
    time.sleep(0.65)
    c.eval("""(() => {
      const t = document.querySelector(".gsx-tag[data-tag='Sick']");
      if (t) t.click();
      document.querySelector(".gsx-sheet--tags [data-tag='done']").click();
    })()""")
    time.sleep(0.7)
    tot2 = c.eval("""(() => { const h = document.querySelector('.gsx-group__head span');
      return h ? Number((h.textContent.match(/About (\\d+)/) || [0,0])[1]) : 0 })()""")
    check("a second tag narrows rather than widens", tot2 <= tot1,
          f"{tot1} with one tag, {tot2} with two")

    print("\nthe type sheet")
    c.goto(URL, settle=0.9)
    c.click('.search')
    time.sleep(0.45)
    c.eval(TYPE % "'@'")
    time.sleep(0.7)
    got = c.eval(BOX % "'.gsx-sheet--type'")
    ih = c.eval("innerHeight")
    check("'@' opens Choose Search Type as a bottom sheet",
          got["there"] and got["vis"] and abs((got["top"] + got["h"]) - ih) <= 2,
          f"{got['w']}x{got['h']}, bottom at {got['top'] + got['h']} of {ih}")
    got = c.eval("""(() => [...document.querySelectorAll('.gsx-opt')]
        .map(e => e.textContent.replace(/\\s+/g,' ').trim()))()""")
    check("offering all eight of the design's types", len(got) == 8,
          " · ".join(x.split(" no records")[0] for x in got))

    c.eval("""(() => {
      document.querySelector(".gsx-opt[data-key='animal']").click();
      document.querySelector("[data-done='type']").click();
    })()""")
    time.sleep(0.7)
    got = c.eval(BOX % "'.gsx-token'")
    check("Done commits a token chip into the field",
          got["there"] and got["vis"], f"{got['text']} · {got['w']}x{got['h']}")

    print("\nchoosing a result")
    c.eval("(() => document.querySelector('.gsx-token__x').click())()")
    time.sleep(0.35)
    c.eval(TYPE % "'CAR-02'")
    time.sleep(0.4)
    got = c.eval("""(() => { const r = document.querySelector('.gsx-row');
      return r ? r.textContent.replace(/\\s+/g,' ').trim().slice(0,52) : null })()""")
    check("an enclosure code finds its enclosure", bool(got), str(got))

    c.eval("document.querySelector('.gsx-row').click()")
    time.sleep(0.8)
    got = c.eval("""(() => { const st = antz.view();
      const p = document.querySelector('.gsx');
      return { view: st.view, level: st.level, enc: st.enclosureId, open: p && !p.hidden }; })()""")
    check("clicking it navigates to that enclosure",
          got["view"] == "site" and got["level"] == "enclosure" and bool(got["enc"]),
          f"{got['view']}/{got['level']} {got['enc']}")
    check("and the search page closes behind it", not got["open"])
    check("the page underneath scrolls again",
          c.eval("getComputedStyle(document.body).overflow") != "hidden")

    print("\nwhat it refuses to invent")
    got = c.eval("(() => antz.searchIndex().TYPES.filter(t => !t.has).map(t => t.key))()")
    check("the two types with no data are still offered, not deleted",
          set(got) == {"user", "tag"}, " · ".join(got))

    check("no console errors through any of it", not c.errors(), str(c.errors()[:2]))


print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
sys.exit(1 if fails else 0)

"""Verification for the Site Command Centre — SESSION_HANDOFF §0.

    python3 tools/verify_detail.py

Two things, because they are the two the last session changed: the widget
RECORD sheet, and where the workspace switch LANDS.

Opens a record at all three levels, asserts every domain resolves one, checks
that nothing inside the sheet clips at six widths, that a Site with no data
gets its empty state rather than rows of em dashes, and that Escape closes the
sheet without also going up a level.

Runs against the working copy over file://, in headless Chrome, driven by CDP —
the same harness as tools/verify.py, and reduced motion is forced for the same
reason (see the note at the top of that file).
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

PROBE = r"""
(() => {
  const sheet = document.querySelector('.wdetail');
  if (!sheet || sheet.hidden) return {open:false};
  const body = sheet.querySelector('.wdetail__body');
  const bad = [];
  // horizontal overflow anywhere except the deliberately scrolling table wrap
  for (const el of sheet.querySelectorAll('*')) {
    if (el.closest('.dtable-wrap') && el.classList.contains('dtable-wrap')) continue;
    if (el.classList.contains('wdetail__nav')) continue;
    if (el.scrollWidth > el.clientWidth + 1 && !el.closest('.dtable-wrap')) {
      const t = (el.textContent||'').trim().slice(0,44);
      bad.push(`OVERFLOW ${el.className} ${el.scrollWidth}>${el.clientWidth} "${t}"`);
    }
  }
  const r = sheet.getBoundingClientRect();
  return {
    open: true,
    title: sheet.querySelector('.wdetail__title').textContent,
    crumb: sheet.querySelector('.wdetail__crumb').textContent,
    source: sheet.querySelector('.wdetail__source').textContent,
    tiles: sheet.querySelectorAll('.dtile').length,
    groups: sheet.querySelectorAll('.dgroup').length,
    facts: sheet.querySelectorAll('.dfact').length,
    tableRows: sheet.querySelectorAll('.dtable tbody tr').length,
    items: sheet.querySelectorAll('.ditem').length,
    chips: sheet.querySelectorAll('.wdetail__chip').length,
    go: (sheet.querySelector('.wdetail__go')||{}).textContent,
    scrolled: body.scrollTop,
    offRight: r.right > document.documentElement.clientWidth + 1,
    bodyH: body.clientHeight,
    bad: bad.slice(0, 8),
  };
})()
"""

with Chrome(width=1024, height=1366) as c:
    c.goto(URL)
    check("page loaded without errors", not c.errors(), str(c.errors()[:2]))

    c.eval("location.hash = '#site/bg-safari'")
    time.sleep(0.5)
    check("site workspace showing", c.eval("document.body.classList.contains('is-site')") is True)

    problems = c.eval("antz.checkDetail()")
    check("every domain resolves a record at every level", problems == [],
          "; ".join(problems[:6]) if problems else "")
    print("   ", [l for l in c.console if l[0] == 'info'][-1:])

    # ── open one, at each level ───────────────────────────────────────────
    for level, h in [("site", "#site/bg-safari"), ("section", "#section/car"),
                     ("enclosure", "#enclosure/car.2")]:
        c.eval(f"location.hash = '{h}'")
        time.sleep(0.45)
        # a widget that is not one of the drill-in cards
        sel = c.eval("""(() => {
          const skip = ['site.space.sections','site.space.count','sec.space.enclosures',
                        'sec.space.door','sec.overview.structure'];
          for (const card of document.querySelectorAll('#siteGrid .card')) {
            if (!skip.includes(card.dataset.variant)) { card.id = 'probe'; return card.dataset.variant }
          }
          return null })()""")
        c.eval("document.getElementById('probe').click()")
        time.sleep(0.6)
        got = c.eval(PROBE)
        check(f"{level}: sheet opens from {sel}", bool(got and got.get("open")))
        if got and got.get("open"):
            print(f"      {got['title']} · {got['crumb']} · {got['groups']} groups, "
                  f"{got['facts']} facts, {got['tableRows']} table rows, {got['items']} items")
            print(f"      {got['source']} | foot: {(got['go'] or '').strip()} | scrolled to {got['scrolled']}px")
            check(f"{level}: nothing clips inside the sheet", not got["bad"], "; ".join(got["bad"]))
            check(f"{level}: sheet is on screen", not got["offRight"])
            check(f"{level}: has tiles and groups", got["tiles"] >= 3 and got["groups"] >= 2)
        # escape closes it, and does NOT also go up a level
        before = c.eval("location.hash")
        c.eval("""document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))""")
        time.sleep(0.6)
        check(f"{level}: escape closes the sheet only",
              c.eval("document.querySelector('.wdetail').hidden") is True
              and c.eval("location.hash") == before,
              f"hash {before} -> {c.eval('location.hash')}")

    # ── every widget on the default Site page opens something ─────────────
    c.eval("location.hash = '#site/bg-safari'")
    time.sleep(0.4)
    n = c.eval("document.querySelectorAll('#siteGrid .card').length")
    opened = c.eval("""(() => {
      const skip = ['site.space.sections','site.space.count'];
      let ok = 0, miss = [];
      for (const card of document.querySelectorAll('#siteGrid .card')) {
        if (skip.includes(card.dataset.variant)) continue;
        card.click();
        const s = document.querySelector('.wdetail');
        if (s && !s.hidden && s.querySelectorAll('.dgroup').length) ok++;
        else miss.push(card.dataset.variant);
      }
      return {ok, miss};
    })()""")
    check(f"all {n} widgets on the page open a record", not opened["miss"],
          ", ".join(opened["miss"][:6]))
    print(f"      {opened['ok']} records opened by tapping")

    # ── six widths, one large record ──────────────────────────────────────
    c.eval("""document.querySelector('.wdetail__close').click()""")
    time.sleep(0.5)
    for w in (1920, 1024, 900, 768, 640, 500):
        c.set_viewport(w, 1100)
        time.sleep(0.25)
        c.eval("""(() => { for (const card of document.querySelectorAll('#siteGrid .card'))
            if (card.dataset.variant === 'site.maint.open') { card.click(); return } })()""")
        time.sleep(0.5)
        got = c.eval(PROBE)
        check(f"{w}px: record sheet holds", bool(got.get("open")) and not got["bad"] and not got["offRight"],
              "; ".join(got.get("bad", [])))
        c.eval("document.querySelector('.wdetail__close').click()")
        time.sleep(0.4)

    # ── an absent record says so ──────────────────────────────────────────
    c.set_viewport(1024, 1366)
    c.eval("location.hash = '#site/hg-field'")
    time.sleep(0.6)
    empty = c.eval("""(() => {
      for (const card of document.querySelectorAll('#siteGrid .card')) {
        if (card.dataset.variant.startsWith('site.assets') || card.dataset.variant.startsWith('site.finance')) {
          card.click();
          const s = document.querySelector('.wdetail');
          return { note: (s.querySelector('.dempty__note')||{}).textContent || null,
                   groups: s.querySelectorAll('.dgroup').length };
        }
      }
      return null })()""")
    check("a Site with no record gets an empty state, not zeroes",
          bool(empty and empty["note"]) and empty["groups"] == 0, str(empty))
    print("      ", (empty or {}).get("note"))

    errs = c.errors()
    check("no console errors at any point", not errs, str(errs[:3]))



# ── where the Site Command Centre tab lands ────────────────────────────────
def nav_state(c):
    return c.eval("""(() => ({
      level: document.body.dataset.level,
      listing: document.body.classList.contains('is-listing'),
      onSite: document.body.classList.contains('is-site'),
      hash: location.hash,
      cards: document.querySelectorAll('#siteGrid .card').length,
      rows: document.querySelectorAll('.site-row').length,
    }))()""")


with Chrome(width=1024, height=1200) as c:
    print("\nwhere the switch lands")
    c.goto(URL)
    st = nav_state(c)
    check("a fresh visitor lands on the home page", st["onSite"] is False, str(st))

    # THE TAB IS THE DOOR TO THE SITES.
    c.eval("[...document.querySelectorAll('.wswitch__tab')][1].click()"); time.sleep(0.9)
    st = nav_state(c)
    check("the Site Command Centre tab opens the Sites listing",
          st["listing"] and st["level"] == "sites", f"level={st['level']} listing={st['listing']}")
    check("with every Site on it", st["rows"] == 4, f"{st['rows']} rows")
    check("and the hash following", st["hash"] == "#sites", st["hash"])

    # choosing one opens it, and the tab brings you back out
    c.eval("document.querySelectorAll('.site-row')[0].click()"); time.sleep(0.8)
    st = nav_state(c)
    check("choosing a Site opens its workspace", st["level"] == "site" and st["cards"] >= 8, str(st))
    sel = c.eval("[...document.querySelectorAll('.wswitch__tab')].map(t => t.getAttribute('aria-selected'))")
    check("the Site tab is already selected in a Site", sel == ["false", "true"], str(sel))
    c.eval("[...document.querySelectorAll('.wswitch__tab')][1].click()"); time.sleep(0.9)
    st = nav_state(c)
    check("tapping the already-selected tab goes back out to the listing",
          st["listing"] and st["level"] == "sites", str(st))

    # from deeper in the hierarchy too
    c.eval("location.hash='#enclosure/car.2'"); time.sleep(0.9)
    check("an enclosure is reachable", nav_state(c)["level"] == "enclosure")
    c.eval("[...document.querySelectorAll('.wswitch__tab')][1].click()"); time.sleep(0.9)
    st = nav_state(c)
    check("and the tab comes all the way back out to the listing",
          st["listing"] and st["level"] == "sites", str(st))

    # Housing on the home page is the other door to the same place
    c.eval("[...document.querySelectorAll('.wswitch__tab')][0].click()"); time.sleep(0.7)
    c.eval("""(() => { for (const card of document.querySelectorAll('#moduleGrid .card'))
        if ((card.dataset.variant||'').startsWith('housing')) { card.click(); return } })()""")
    time.sleep(0.9)
    check("the Housing tile still opens the listing", nav_state(c)["listing"] is True)

    # and the ways back up are unchanged
    c.eval("document.querySelectorAll('.site-row')[0].click()"); time.sleep(0.8)
    c.eval("document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))")
    time.sleep(0.7)
    check("Escape from a Site steps up to the listing", nav_state(c)["listing"] is True)

    check("no console errors while navigating", not c.errors(), str(c.errors()[:2]))


print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
sys.exit(1 if fails else 0)

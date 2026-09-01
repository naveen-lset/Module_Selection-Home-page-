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



# ── the modules menu is a centred dialog over a blurred page ───────────────
MENU_PROBE = r"""
(() => {
  const m = document.querySelector('.pmenu--centre');
  if (!m || m.hidden) return { open: false };
  const r = m.getBoundingClientRect();
  const veil = document.querySelector('.pmenu-catcher--veil');
  const cs = veil && !veil.hidden ? getComputedStyle(veil) : null;
  const notes = [...m.querySelectorAll('.pmenu__note')].map(n => n.textContent);
  return {
    open: true,
    offCentre: [Math.abs((r.left + r.width / 2) - innerWidth / 2),
                Math.abs((r.top + r.height / 2) - innerHeight / 2)],
    inViewport: r.left >= 0 && r.top >= 0 && r.right <= innerWidth + 1 && r.bottom <= innerHeight + 1,
    scrolls: m.scrollHeight > m.clientHeight,
    veilBlur: cs ? cs.backdropFilter : null,
    veilOpacity: cs ? cs.opacity : null,
    locked: document.body.style.overflow,
    title: (m.querySelector('.pmenu__dtitle') || {}).textContent || null,
    close: !!m.querySelector('.pmenu__dclose'),
    rows: m.querySelectorAll('.pmenu__item').length,
    notesAreCounts: notes.length > 0 && notes.every(n => /^\d+ widgets$/.test(n.trim())),
    sampleNotes: notes.slice(0, 3),
    ellipsed: [...m.querySelectorAll('.pmenu__label')].filter(e => e.scrollWidth > e.clientWidth + 1).length,
  };
})()
"""

MENU_BTN = "document.querySelector(\"button[aria-label='Modules for your role']\").click()"

with Chrome(width=1024, height=1300) as c:
    print("\nthe modules menu")
    c.goto(URL)
    c.eval("location.hash='#site/bg-safari'"); time.sleep(0.8)
    c.eval(MENU_BTN); time.sleep(0.9)
    got = c.eval(MENU_PROBE)
    check("the menu opens", got.get("open") is True)
    check("centred in the viewport", got["offCentre"][0] <= 2 and got["offCentre"][1] <= 2, str(got["offCentre"]))
    check("wholly on screen", got["inViewport"] is True)
    check("the page behind it is blurred", "blur" in (got["veilBlur"] or ""), str(got["veilBlur"]))
    check("the veil is fully faded in", got["veilOpacity"] == "1", str(got["veilOpacity"]))
    check("the page cannot scroll under it", got["locked"] == "hidden", str(got["locked"]))
    check("it has a title and a way out", bool(got["title"]) and got["close"], str(got["title"]))
    check("every row's note is a widget count and nothing else",
          got["notesAreCounts"], str(got["sampleNotes"]))
    check("no module name is ellipsed", got["ellipsed"] == 0, f"{got['ellipsed']} ellipsed")
    check("a long list scrolls inside the dialog", got["scrolls"] is True)

    # a row is a switch, and the dialog stays open while you flick them
    before = c.eval("document.querySelectorAll('#siteGrid .card').length")
    c.eval("document.querySelectorAll('.pmenu--centre .pmenu__item')[1].click()"); time.sleep(0.5)
    after = c.eval("document.querySelectorAll('#siteGrid .card').length")
    check("toggling a row keeps the dialog open and changes the page",
          c.eval("!document.querySelector('.pmenu--centre').hidden") and after != before,
          f"{before} -> {after} cards")

    # the two ways out
    c.eval("document.querySelector('.pmenu__dclose').click()"); time.sleep(0.6)
    check("the close button closes it and unlocks the page",
          c.eval("document.querySelector('.pmenu--centre').hidden") is True and
          c.eval("document.body.style.overflow") == "", "")
    c.eval(MENU_BTN); time.sleep(0.8)
    c.eval("document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))")
    time.sleep(0.6)
    check("Escape closes it too", c.eval("document.querySelector('.pmenu--centre').hidden") is True)

    # and it fits at every width the product is drawn at
    for w in (1920, 1024, 820, 768, 500, 430):
        c.set_viewport(w, 900); time.sleep(0.25)
        c.eval(MENU_BTN); time.sleep(0.7)
        got = c.eval(MENU_PROBE)
        check(f"{w}px: the dialog fits and stays centred",
              got.get("open") and got["inViewport"] and got["offCentre"][0] <= 2,
              str(got.get("offCentre")))
        c.eval("document.querySelector('.pmenu__dclose').click()"); time.sleep(0.45)

    check("no console errors around the menu", not c.errors(), str(c.errors()[:2]))



# ── the page chrome: order, greeting, rows, and the rotating search hint ───
with Chrome(width=1024, height=1366) as c:
    print("\nthe page chrome")
    c.goto(URL)
    order = c.eval("[...document.querySelector('.page').children].map(e => e.className || e.id)")
    check("the switcher is above the greeting and the search field",
          order.index("wswitch-row") < order.index("home-header") < order.index("search-row"),
          " → ".join(order))

    c.eval("[...document.querySelectorAll('.wswitch__tab')][1].click()"); time.sleep(0.9)
    greet = c.eval("""(() => { const g = document.querySelector('.greeting');
        return [getComputedStyle(g).opacity, g.textContent.replace(/\\s+/g,' ').trim()] })()""")
    check("the greeting shows in the Site Command Centre too",
          greet[0] == "1" and "Good Morning" in greet[1], str(greet))
    check("and no page title is drawn over it",
          c.eval("getComputedStyle(document.querySelector('.home-header'), '::before').content") in ("none", "normal", '""'),
          str(c.eval("getComputedStyle(document.querySelector('.home-header'), '::before').content")))

    rails = c.eval("""[...document.querySelectorAll('.site-row')].map(r => getComputedStyle(r,'::before').content)""")
    check("no Site row carries a status rail", all(v in ("none", "normal") for v in rails), str(rails))

    # the hint replaces the placeholder, and the scope moves to the label
    st = c.eval("""(() => { const i = document.querySelector('.search__input'), h = document.querySelector('.search__hint');
        return { placeholder: i.placeholder, label: i.getAttribute('aria-label'),
                 hintHidden: h.hidden, hidden: h.getAttribute('aria-hidden'),
                 lead: (h.querySelector('.search__hint-lead')||{}).textContent,
                 word: (h.querySelector('.search__cycle')||{}).textContent } })()""")
    check("the input's own placeholder is empty", st["placeholder"] == "", repr(st["placeholder"]))
    check("the scope moved to the accessible label", "Search" in (st["label"] or ""), str(st["label"]))
    check("the hint is decorative, not announced", st["hidden"] == "true")
    check("and it names something searchable", st["lead"] == "Search" and bool(st["word"]),
          f"{st['lead']} {st['word']}")

    # per depth
    c.eval("location.hash='#enclosure/car.2'"); time.sleep(0.9)
    # Under reduced motion the hint is the static three-word line, so the check
    # is that the WORDS are the enclosure's, whichever form they are drawn in.
    txt = c.eval("document.querySelector('.search__cycle').textContent")
    # The term is quoted now — `Search "Animals"` reads as an example query
    # where `Search Animals` read as a caption — so the quotes come off before
    # the words are compared.
    words = set(w.strip().strip("\u201c\u201d\"") for w in txt.split(","))
    check("the words follow the depth",
          words <= {"Animals", "Treatments", "Enrichment", "Keepers", "Documents"}, txt)

    # typing hides it, like a placeholder
    c.eval("""(() => { const i = document.querySelector('.search__input');
        i.value = 'tiger'; i.dispatchEvent(new Event('input')) })()""")
    time.sleep(0.3)
    check("typing hides it", c.eval("document.querySelector('.search__hint').hidden") is True)
    c.eval("""(() => { const i = document.querySelector('.search__input');
        i.value = ''; i.dispatchEvent(new Event('input')) })()""")
    time.sleep(0.3)
    check("clearing brings it back", c.eval("document.querySelector('.search__hint').hidden") is False)

    check("reduced motion gets a static line, not a slideshow",
          "," in c.eval("document.querySelector('.search__cycle').textContent"),
          c.eval("document.querySelector('.search__cycle').textContent"))
    check("no console errors in the chrome", not c.errors(), str(c.errors()[:2]))


# The hint only ANIMATES where motion is welcome, so that half needs its own
# browser — this suite's default forces reduced motion for measurement.
with Chrome(width=1024, height=1000, reduced_motion=False) as c:
    print("\nthe search hint, with motion")
    c.goto(URL)
    seen = []
    for _ in range(4):
        seen.append(c.eval("document.querySelector('.search__cycle').textContent"))
        time.sleep(2.4)
    check("it cycles through what can be searched", len(set(seen)) >= 3, " · ".join(seen))
    check("one word at a time", all("," not in w for w in seen), " · ".join(seen))
    check("and the term is quoted, so it reads as a query and not a caption",
          all(w.startswith("\u201c") and w.endswith("\u201d") for w in seen), " · ".join(seen))

    # THE BUG THIS CATCHES: two animations, the first with `fill: forwards`, left
    # the word sitting at opacity 0 for most of every cycle — it moved, and was
    # invisible while it did. Sampled rather than reasoned about, because the
    # markup and the text were both perfectly correct while it was broken.
    dim = 0
    for _ in range(16):
        if c.eval("+getComputedStyle(document.querySelector('.search__cycle')).opacity") < 0.5:
            dim += 1
        time.sleep(0.4)
    check("and the word is actually visible while it does",
          dim <= 5, f"below half opacity in {dim} of 16 samples")

    c.eval("document.querySelector('.search__input').dispatchEvent(new FocusEvent('focus'))")
    time.sleep(0.8)
    a = c.eval("document.querySelector('.search__cycle').textContent")
    time.sleep(3.6)
    b = c.eval("document.querySelector('.search__cycle').textContent")
    check("focus freezes it, so it does not move under the caret", a == b, f"{a} -> {b}")
    c.eval("document.querySelector('.search__input').dispatchEvent(new FocusEvent('blur'))")
    time.sleep(3.0)
    check("blur resumes it", c.eval("document.querySelector('.search__cycle').textContent") != b)
    check("no console errors while cycling", not c.errors(), str(c.errors()[:2]))


# ── Enter is acknowledged, because there is no index to answer with ────────
ENTER = """(()=>{const i=document.querySelector('.search__input');i.focus();
  i.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true,cancelable:true}));})()"""
SET_VALUE = """(v=>{const i=document.querySelector('.search__input');i.value=v;
  i.dispatchEvent(new Event('input'));})"""
LIVE = "[...document.querySelectorAll('[aria-live]')].map(e=>e.textContent.trim()).filter(Boolean)"

with Chrome(width=1024, height=1000, reduced_motion=False) as c:
    print("\npressing Enter in the search field")
    c.goto(URL)
    c.eval(SET_VALUE + "('leopard')"); time.sleep(0.3)
    c.eval(ENTER); time.sleep(0.1)
    running = c.eval("document.querySelector('.search').getAnimations().length"
                     " + document.querySelector('.search__icon').getAnimations().length")
    check("a query is acknowledged in motion", running >= 2, f"{running} animations")
    time.sleep(0.8)
    check("and the field is left exactly as it was found",
          c.eval("getComputedStyle(document.querySelector('.search')).transform") in ("none", "matrix(1, 0, 0, 1, 0, 0)")
          and c.eval("document.querySelector('.search').getAnimations().length") == 0,
          c.eval("getComputedStyle(document.querySelector('.search')).transform"))
    check("the live region says what was taken",
          any("leopard" in t for t in c.eval(LIVE)), str(c.eval(LIVE)))

    # An empty Enter is unfinished, not wrong: the HINT moves, not the field
    c.eval(SET_VALUE + "('')"); time.sleep(0.3)
    c.eval(ENTER); time.sleep(0.1)
    check("an empty Enter nudges the hint rather than shaking the field",
          c.eval("document.querySelector('.search__hint').getAnimations().length") >= 1
          and c.eval("document.querySelector('.search').getAnimations().length") == 0, "")
    time.sleep(0.6)
    check("and it says what to type", any("search" in t.lower() for t in c.eval(LIVE)), str(c.eval(LIVE)))
    check("no console errors around submit", not c.errors(), str(c.errors()[:2]))

# THE HALF THAT MATTERS MOST: a micro-interaction that only exists as movement
# is one half the audience never receives. This suite forces reduced motion.
with Chrome(width=1024, height=1000) as c:
    print("\nEnter, with motion turned down")
    c.goto(URL)
    c.eval(ENTER); time.sleep(0.4)
    check("nothing moves", c.eval("document.querySelector('.search').getAnimations().length") == 0)
    check("and the live region still speaks", bool(c.eval(LIVE)), str(c.eval(LIVE)))
    check("no console errors", not c.errors(), str(c.errors()[:2]))


print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
sys.exit(1 if fails else 0)

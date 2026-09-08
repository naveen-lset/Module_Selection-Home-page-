"""The second home page — Figma node 236:6669 — and the widgets on it.

    python3 tools/verify_v2.py                      # 1024, the app's own width
    python3 tools/verify_v2.py http://host/ 768     # another origin, another width

V2 is `?v=2`: the same application drawing the composition node 236:6669 draws —
no announcement deck, no observation rail, the gradient band re-parented onto
the module grid, and Notes and My Focus Hub seeded into it.

THE INK FOCUS HUB IS NO LONGER SEEDED — the ruling of 8 Sep 2026, "Notes put in
the top, remove that dark blue one". The node drew both compositions of My Focus
Hub at once, which was the file offering a choice; the choice is the plate. The
ink card is still in the catalogue and still addable, so its own geometry is
still worth checking — but only when something has put it on the page, which
this suite no longer does. Those checks are therefore conditional, and the
ruling itself is asserted instead.

TWO KINDS OF CHECK LIVE HERE. The first is that V2 IS V2 and V1 is untouched:
the switch is a URL parameter read in two places, and the failure mode of
getting that wrong is a page that looks fine and is the wrong one. The second is
the three new cards, whose numbers come from the design file rather than from a
node measurement — 4:3 has no meaning here, so what is asserted is the geometry
the file states (a 72 and a 92 photograph, a 44 thumbnail, three updates, the
priority pill) and, at every width, that nothing clips. Clipping is the whole
risk with these two: they are 2x2 compositions and SPAN_TABLE hands them a
single column on a phone.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp import Chrome

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000/").rstrip("/") + "/"
WIDTH = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
fails = []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
    if not ok:
        fails.append(name)


def near(a, b, tol=1.0):
    return a is not None and abs(a - b) <= tol


PROBE = """(()=>{
  const q=(s)=>document.querySelector(s);
  const shown=(s)=>{const e=q(s); return e ? getComputedStyle(e).display!=='none' : null};
  const cards=[...document.querySelectorAll('#moduleGrid .card')];
  const of=(id)=>cards.find(e=>e.dataset.variant===id) || null;
  const box=(e)=>{if(!e)return null;const r=e.getBoundingClientRect();
    return {w:+r.width.toFixed(1),h:+r.height.toFixed(1)}};
  const sub=(card,s)=>card?box(card.querySelector(s)):null;
  /* THE PAGE ON SCREEN, NOT ALL OF THEM. These cards now hold one element per
     item, so a naive `querySelectorAll` counts three pages' worth of updates
     and compares nine against three. Everything per-item is asked of the
     current page. */
  const at=(card)=>card?card.querySelector('.is-page[data-pos="at"]'):null;
  const nAt=(card,s)=>{const p=at(card); return p?p.querySelectorAll(s).length:0};
  const hub=of('focus.hub'), lite=of('focus.light'), note=of('notes.recent');
  const band=(()=>{const m=q('.modules-band'); if(!m) return null;
    const cs=getComputedStyle(m,'::before'); const r=m.getBoundingClientRect();
    const page=q('.page').getBoundingClientRect();
    return {img:cs.backgroundImage, radius:cs.borderRadius,
            left:+(r.left-page.left).toFixed(1)}})();
  return {
    stamp:document.documentElement.dataset.pageVersion,
    deckShown:shown('.hero-stage'), railShown:shown('.obs-band'),
    deckMounted:document.querySelectorAll('.hero--slide').length,
    railMounted:document.querySelectorAll('.obs').length,
    band,
    /* the section head: gone at rest on V2, back in edit mode */
    head:(()=>{const h=document.getElementById('modulesHead'); if(!h) return null;
      const b=h.querySelector('.link-btn'); if(b) b.focus();
      return {h:+h.getBoundingClientRect().height.toFixed(1),
              vis:getComputedStyle(h).visibility,
              /* a clipped control is still tabbable unless visibility says
                 otherwise — this is the check that caught it */
              focusable:!!b&&document.activeElement===b}})(),
    n:cards.length,
    ids:cards.map(e=>e.dataset.variant),
    three:[hub,lite,note].filter(Boolean).length,
    fills:{hub:hub&&hub.dataset.fill, lite:lite&&lite.dataset.fill, note:note&&note.dataset.fill},
    sizes:{hub:hub&&hub.dataset.size, lite:lite&&lite.dataset.size, note:note&&note.dataset.size},
    hubPhoto:box(at(hub)&&at(hub).querySelector('.l-focus__photo')),
    litePhoto:box(at(lite)&&at(lite).querySelector('.l-focus__photo')),
    noteThumb:box(at(note)&&at(note).querySelector('.l-note__thumb')),
    hubUpdates:nAt(hub,'.l-focus__update'),
    liteUpdates:nAt(lite,'.l-focus__update'),
    hubDots:hub?hub.querySelectorAll('.dots__dot').length:0,
    liteDots:lite?lite.querySelectorAll('.dots__dot').length:0,
    noteDots:note?note.querySelectorAll('.dots__dot').length:0,
    noteRun:note?!!note.querySelector('.dots--run'):false,
    hubBadges:nAt(hub,'.l-focus__tag'),
    /* the badges are ON the photograph here and in the flow there */
    hubBadgesOnPhoto:!!(at(hub)&&at(hub).querySelector('.l-focus__shot .l-focus__badges')),
    liteBadgesInFlow:!!(at(lite)&&at(lite).querySelector('.l-focus__facts .l-focus__badges')),
    /* the ink card's enclosure line, which the plate card does not draw */
    hubRefs:nAt(hub,'.l-focus__ref'),
    liteRefs:nAt(lite,'.l-focus__ref'),
    pri:at(note)?getComputedStyle(at(note).querySelector('.l-note__pri')).backgroundColor:null,
    tint:at(note)?getComputedStyle(at(note).querySelector('.l-note__plate')).backgroundColor:null,
    /* THE CLAMP AND THE BOX HAVE TO AGREE. `-webkit-line-clamp` draws its
       ellipsis at the line it clamps at; a flex parent that compresses the box
       below that never reaches it, so the text is cut mid-line with nothing to
       say so. Reading both means a squeezed box cannot pass as a clamped one. */
    noteClamp:at(note)?+getComputedStyle(at(note).querySelector('.l-note__text')).webkitLineClamp:0,
    noteTextH:at(note)?+box(at(note).querySelector('.l-note__text')).h.toFixed(1):0,
    noteTextSH:at(note)?at(note).querySelector('.l-note__text').scrollHeight:0,
    imgs:[...document.querySelectorAll('#moduleGrid .l-focus__photo,#moduleGrid .l-note__thumb')]
      .every(i=>i.complete&&i.naturalWidth>0),
    /* THE CARD CAN NO LONGER OVERFLOW, so asking whether it does is no longer
       a check. Focus Hub and Notes stack their items absolutely inside a
       `__pages` box, which means content taller than the card grows the PAGE
       and the card's own scrollHeight never moves — the check that caught the
       squeezed note would now pass on a card losing half its content. So every
       page is measured against the box it is absolutely positioned in. */
    clipped:(()=>{const out=[];
      for(const e of cards){
        if(e.scrollHeight>e.clientHeight+1) out.push(e.dataset.variant+'@'+e.dataset.size);
        for(const box of e.querySelectorAll('.l-focus__pages,.l-note__pages'))
          for(const pg of box.querySelectorAll('.is-page'))
            if(pg.scrollHeight>box.clientHeight+1)
              out.push(e.dataset.variant+' page '+pg.scrollHeight+'>'+box.clientHeight);
      }
      return out})(),
    zero:(()=>{const out=[];
      for(const card of [hub,lite,note].filter(Boolean))
        for(const n of card.querySelectorAll('span,b,time,img'))
          {const r=n.getBoundingClientRect();
           if((r.width<0.5||r.height<0.5)&&n.className&&!String(n.className).includes('sr-only'))
             out.push(card.dataset.variant+' '+String(n.className))}
      return out.slice(0,6)})(),
    hOverflow:document.documentElement.scrollWidth-document.documentElement.clientWidth,
    /* ── paging ── */
    pager:(()=>{const out={};
      for(const [k,e] of [['hub',hub],['lite',lite],['note',note]]){
        if(!e){out[k]=null;continue}
        const dots=[...e.querySelectorAll('.dots__dot')];
        out[k]={tag:e.tagName, role:e.getAttribute('role'),
          pages:e.querySelectorAll('.is-page').length,
          dots:dots.length,
          buttons:dots.filter(b=>b.tagName==='BUTTON').length,
          dwell:!!e.querySelector('.pager-dwell'),
          at:dots.findIndex(b=>b.getAttribute('aria-current')==='true'),
          /* one tab stop, not five: only the current dot is reachable */
          tabbable:dots.filter(b=>b.tabIndex===0).length,
          /* nothing inside an off-screen page may be focusable */
          inertOff:[...e.querySelectorAll('.is-page')].every(p=>p.inert===(p.dataset.pos!=='at')),
          /* a passive card must not be a control itself */
          clickable:e.tagName==='BUTTON'||e.tagName==='A'}}
      return out})(),
    /* the two kinds of item the hub carries */
    /* across ALL pages here, deliberately: the point is that the LIST holds
       both kinds, which one page cannot show */
    kinds:hub?{latin:hub.querySelectorAll('.l-focus__latin').length,
               sub:hub.querySelectorAll('.l-focus__sub').length}:null,
  }})()"""

EDIT_HEAD = """(()=>{const h=document.getElementById('modulesHead');
  const done=h.querySelector('.link-btn--done'), add=h.querySelector('.add-module-btn');
  if(done) done.focus(); const d=!!done&&document.activeElement===done;
  if(add) add.focus(); const a=!!add&&document.activeElement===add;
  return {h:+h.getBoundingClientRect().height.toFixed(1), vis:getComputedStyle(h).visibility,
          done:d, add:a}})()"""

HEAD_AWAY = """(()=>({editing:document.body.classList.contains('is-editing'),
  h:+document.getElementById('modulesHead').getBoundingClientRect().height.toFixed(1)}))()"""

# what V2 seeds, in V2_LAYOUT's order: the node's cards, less the ink Focus Hub
# the ruling of 8 Sep took off, with Notes moved to the head of the page and
# Diet & Kitchen added beside Hospital the same afternoon
WANT = ['notes.recent', 'medical.default', 'housing.default', 'species.stats',
        'hospital.photo', 'diet.photo', 'pharmacy.default', 'lab.default',
        'approvals.pending', 'administer.default', 'mortality.default',
        'eggs.default', 'audit.default', 'users.default', 'security.default',
        'focus.light']


OPEN_MENU = "(()=>{document.getElementById('avatarBtn').click(); return 1})()"

VER_GROUP = """(()=>{
  const m=document.querySelector('.pmenu');
  if(!m||m.hidden) return {open:false, ver:[], heads:[]};
  const rows=[...m.querySelectorAll('.pmenu__item')];
  const mr=m.getBoundingClientRect();
  return {open:true,
    heads:[...m.querySelectorAll('.pmenu__heading-text')].map(h=>h.textContent.trim()),
    ver:rows.filter(r=>r.dataset.id.startsWith('ver:')).map(r=>({
      id:r.dataset.id, role:r.getAttribute('role'), checked:r.getAttribute('aria-checked'),
      label:r.querySelector('.pmenu__label').textContent.trim(),
      note:r.querySelector('.pmenu__note').textContent.trim(),
      tick:!!r.querySelector('.pmenu__tick'),
      /* a row whose note wraps past its own box is a row that has lost half
         its second line — the menu is 304 wide and these notes are the
         longest in it */
      clipped:r.scrollHeight>r.clientHeight+1})),
    menuH:+mr.height.toFixed(1),
    onScreen: mr.top>=0 && mr.bottom<=innerHeight+.5 && mr.left>=0 && mr.right<=innerWidth+.5,
  }})()"""

PRESS_VER = """(()=>{const b=document.querySelector('.pmenu__item[data-id="ver:%s"]');
  if(!b) return 'no such row'; b.click(); return 'pressed'})()"""

WHERE = """(()=>({v:document.documentElement.dataset.pageVersion, search:location.search,
  cards:document.querySelectorAll('#moduleGrid .card').length,
  deck:document.querySelectorAll('.hero--slide').length}))()"""


def main():
    print(f"V2 — node 236:6669, {WIDTH}px")

    # ── V1 is untouched by any of this ────────────────────────────────────
    print("\nV1 still V1")
    with Chrome(width=WIDTH, height=1200) as c:
        c.goto(BASE + "index.html", settle=2.0)
        v1 = c.eval(PROBE)
        check("no `?v=` means V1", v1["stamp"] == "1", str(v1["stamp"]))
        check("the deck is there and mounted", v1["deckShown"] and v1["deckMounted"] == 6,
              f"shown={v1['deckShown']} slides={v1['deckMounted']}")
        check("the observation rail is there and mounted",
              v1["railShown"] and v1["railMounted"] == 6,
              f"shown={v1['railShown']} cards={v1['railMounted']}")
        check("V1's module band carries NO band fill", v1["band"]["img"] == "none", v1["band"]["img"][:40])
        check("V1 seeds fifteen cards", v1["n"] == 15, str(v1["n"]))
        check("…and none of the three new ones", v1["three"] == 0, str(v1["three"]))
        errs = c.errors()
        check("no console errors on V1", not errs, "; ".join(str(e)[:90] for e in errs[:2]))

    # ── and V2 is the other page ──────────────────────────────────────────
    print("\nV2 is the other page")
    with Chrome(width=WIDTH, height=1200) as c:
        c.goto(BASE + "index.html?v=2", settle=2.2)
        o = c.eval(PROBE)
        check("`?v=2` is stamped on <html> ", o["stamp"] == "2", str(o["stamp"]))
        # HIDDEN IS NOT ABSENT, and both halves matter: the CSS drops them before
        # they paint and the bootstrap never builds them
        check("the deck is gone, and was never mounted",
              o["deckShown"] is False and o["deckMounted"] == 0,
              f"shown={o['deckShown']} slides={o['deckMounted']}")
        check("the observation rail is gone, and was never mounted",
              o["railShown"] is False and o["railMounted"] == 0,
              f"shown={o['railShown']} cards={o['railMounted']}")
        check("the gradient band moved onto the module grid",
              "gradient" in o["band"]["img"] and "255, 255, 255" in o["band"]["img"],
              o["band"]["img"][:56])
        check("…keeping its 32px bottom corners",
              o["band"]["radius"] == "0px 0px 32px 32px", o["band"]["radius"])

        # THE SECTION HEAD IS GONE AT REST — the ruling of 8 Sep 2026. The row's
        # only resting content was an Edit Modules button, which is the profile
        # menu's own first item.
        check("no section head at rest",
              o["head"]["h"] == 0 and o["head"]["vis"] == "hidden",
              f"{o['head']['h']}px, visibility {o['head']['vis']}")
        check("…and its control is out of the tab order, not merely clipped",
              not o["head"]["focusable"],
              "the Edit Modules button still takes focus" if o["head"]["focusable"] else "")

        print("\nthe sixteen cards it seeds")
        check("sixteen cards", o["n"] == 16, str(o["n"]))
        check("and they are the node's, in V2_LAYOUT's order", o["ids"] == WANT,
              "as drawn" if o["ids"] == WANT
              else f"unexpected {[i for i in o['ids'] if i not in WANT]}, "
                   f"missing {[i for i in WANT if i not in o['ids']]}")
        check("both new cards are drawn", o["three"] == 2, str(o["three"]))
        # THE RULING, ASSERTED FROM THE OTHER END. `ids` above would catch the
        # card coming back, but only as one line of a fifteen-way diff; this
        # says what it is.
        check("the ink Focus Hub is not seeded", o["fills"]["hub"] is None,
              "the dark blue card is back on the page" if o["fills"]["hub"] else "")
        # NOTES FIRST IS THE ORDER, and the packer is what makes it the top-left
        # cell — a card first in the array can still be drawn anywhere.
        check("Notes leads the page", o["ids"][0] == "notes.recent", str(o["ids"][0]))
        check("seeded at `tall`, which is 2x2 at four and five columns",
              {o["sizes"]["lite"], o["sizes"]["note"]} == {"tall"}, str(o["sizes"]))

        print("\nMy Focus Hub")
        check("the plate card is white", o["fills"]["lite"] == "plate", str(o["fills"]))
        check("the plate photograph is 92", near(o["litePhoto"]["w"], 92) or WIDTH < 768,
              str(o["litePhoto"]))
        check("three updates on it", o["liteUpdates"] == 3, str(o["liteUpdates"]))
        check("its badges sit in the flow, not on the photograph",
              o["liteBadgesInFlow"], f"inFlow={o['liteBadgesInFlow']}")
        check("it draws no enclosure line", o["liteRefs"] == 1, str(o["liteRefs"]))
        # It pages since 8 Sep 2026 — the node draws the indicator on the ink
        # card only, and a card that advances on its own has to say where you
        # are in it, so the plate card gained one it does not draw.
        check("it pages, and says so", o["liteDots"] == 3, str(o["liteDots"]))

        # ── and the ink variation, IF anything has put it on the page ───────
        # Not seeded since the ruling of 8 Sep; still in the catalogue, so a
        # saved layout or an Add Module can bring it back, and when it does
        # these are the numbers it has to hold. Skipped rather than failed —
        # a check that fails for the absence of what it measures teaches
        # nobody anything.
        if o["fills"]["hub"] == "ink":
            check("the ink card is #1F415B", o["fills"]["hub"] == "ink", str(o["fills"]))
            check("the ink photograph is 72", near(o["hubPhoto"]["w"], 72) or WIDTH < 768,
                  str(o["hubPhoto"]))
            check("three updates on it", o["hubUpdates"] == 3, str(o["hubUpdates"]))
            check("its badges sit ON the photograph", o["hubBadgesOnPhoto"],
                  f"onPhoto={o['hubBadgesOnPhoto']}")
            check("it carries the enclosure line", o["hubRefs"] == 2, str(o["hubRefs"]))
            check("it pages, and says so", o["hubDots"] == 3, str(o["hubDots"]))
            check("the hub carries animals AND enclosures",
                  o["kinds"]["latin"] == 2 and o["kinds"]["sub"] == 1,
                  f"{o['kinds']['latin']} binomials, {o['kinds']['sub']} plain subtitles")
        else:
            print("  ----  the ink card is off the page; its own geometry not checked")

        print("\nNotes")
        check("the thumbnail is 44", near(o["noteThumb"]["w"], 44) or WIDTH < 768, str(o["noteThumb"]))
        check("the priority pill is solid #FA6140", o["pri"] == "rgb(250, 97, 64)", str(o["pri"]))
        check("…and the plate is the same colour at 10%",
              o["tint"] == "rgba(250, 97, 64, 0.1)", str(o["tint"]))
        # four lines on a card at its designed width, two on a phone's single
        # column — the narrow case is a declared truncation, see the container
        # query in the stylesheet
        want_clamp = 4 if o["noteThumb"]["w"] >= 44 else 2
        check(f"the note clamps to {want_clamp} lines", o["noteClamp"] == want_clamp,
              str(o["noteClamp"]))
        check("…and its box is exactly the clamp, not a squeezed one",
              near(o["noteTextH"], o["noteClamp"] * 20, 1.5),
              f"{o['noteTextH']}px for {o['noteClamp']} lines of 20 "
              f"(content is {o['noteTextSH']}px)")
        check("five notes, and its indicator draws the running pill",
              o["noteRun"] and o["noteDots"] == 5, f"run={o['noteRun']} dots={o['noteDots']}")

        print("\npaging")
        for k, want_pages in (("lite", 3), ("note", 5)):
            g = o["pager"][k]
            check(f"{k}: {want_pages} pages, {want_pages} dots, all of them buttons",
                  g["pages"] == want_pages and g["dots"] == want_pages
                  and g["buttons"] == want_pages,
                  f"{g['pages']} pages / {g['dots']} dots / {g['buttons']} buttons")
            # A PASSIVE CARD IS NOT A CONTROL. If this ever regresses to a
            # <button>, the dots inside it become a control in a control —
            # which is the thing ModuleCard.js's standing rule forbids.
            check(f"{k}: the card is a group, not a button",
                  g["role"] == "group" and not g["clickable"],
                  f"{g['tag']} role={g['role']}")
            check(f"{k}: it has a dwell to advance on", g["dwell"])
            check(f"{k}: it rests on the first item", g["at"] == 0, str(g["at"]))
            check(f"{k}: one tab stop, not {want_pages}", g["tabbable"] == 1, str(g["tabbable"]))
            check(f"{k}: nothing off-screen is reachable", g["inertOff"])

        print("\nnothing is lost at this width")
        # THE ONE THAT MATTERS. Ellipsis is these cards' own behaviour on a long
        # binomial; a card whose content is taller than its box loses the bottom
        # of the updates list with nothing on screen to say so.
        check("no card clips its own content", not o["clipped"], str(o["clipped"]))
        check("nothing is drawn at zero size", not o["zero"], str(o["zero"]))
        check("every photograph and thumbnail loaded", o["imgs"])
        check("no horizontal overflow", o["hOverflow"] == 0, str(o["hOverflow"]))

        # AND EDIT MODE STILL HAS ITS CHROME. The collapse is scoped to the
        # resting state for one reason: the head carries Add Module and Done in
        # edit mode, and that Done is the only way out of it on the page itself.
        print("\nedit mode still has its head")
        c.eval("document.body.dispatchEvent(new KeyboardEvent('keydown',{key:'e',bubbles:true}))")
        time.sleep(0.7)
        ed = c.eval(EDIT_HEAD)
        # 44 IS THE TABLET AND DESKTOP HEIGHT, NOT THE PHONE'S. Below 768 the
        # row wraps — the title on one line, Add Module and Done full-width on
        # the next, 101px — which is the phone breakpoint's own design and is
        # what V1 does there too. So what is asserted is what the collapse must
        # not break: the head comes back, it is visible, and both controls can
        # be reached. The exact height is pinned only where one rule owns it.
        want_h = 44 if WIDTH >= 768 else None
        check("the head comes back with Add Module and Done",
              ed["vis"] == "visible" and ed["h"] > 0 and ed["done"] and ed["add"]
              and (want_h is None or near(ed["h"], want_h)), str(ed))
        c.eval("document.querySelector('#modulesHead .link-btn--done').click()")
        time.sleep(0.7)
        out = c.eval(HEAD_AWAY)
        check("…and Done puts it away again", not out["editing"] and out["h"] == 0, str(out))

        print("\nthe catalogue and both layouts agree")
        check("antz.checkDefaults() is clean", c.eval("antz.checkDefaults().length") == 0,
              c.eval("JSON.stringify(antz.checkDefaults())"))

        print("\nconsole")
        errs = c.errors()
        check("no errors or exceptions", not errs, "; ".join(str(e)[:110] for e in errs[:3]))

    # ── THE SWITCH · profile menu → Home page → Version 1 / Version 2 ─────
    # `?v=` was reachable only by typing it, which is the invisible-affordance
    # problem the profile menu exists to fix, so the menu carries the two
    # compositions as a radio group (8 Sep 2026).
    #
    # THE ONLY CHECK THAT MEANS ANYTHING IS PRESSING IT. Reading the rows and
    # their ticks would pass on a switch wired to nothing; setPageVersion
    # NAVIGATES — it has to, because `?v=` is read before the body is parsed
    # and again on boot to decide what to mount — so what is asserted is the
    # page that comes back.
    print("\nswitching version from the profile menu")
    with Chrome(width=WIDTH, height=1200) as c:
        c.goto(BASE + "index.html", settle=2.0)
        c.eval(OPEN_MENU)
        time.sleep(0.35)
        g = c.eval(VER_GROUP)
        check("the menu carries a Home page group of two radios",
              g["open"] and len(g["ver"]) == 2
              and all(r["role"] == "menuitemradio" for r in g["ver"])
              and "HOME PAGE" in [h.upper() for h in g["heads"]],
              f"{g['heads']} {[r['label'] for r in g['ver']]}")
        check("the tick is on the page you are actually on",
              g["ver"][0]["checked"] == "true" and g["ver"][1]["checked"] == "false",
              f"{g['ver'][0]['checked']} / {g['ver'][1]['checked']}")
        check("neither row clips its note",
              not any(r["clipped"] for r in g["ver"]),
              str([r["note"] for r in g["ver"]]))
        check("the menu is wholly on screen with the group in it", g["onScreen"],
              f"{g['menuH']}px tall")

        c.eval(PRESS_VER % "2")
        time.sleep(1.8)
        w = c.eval(WHERE)
        check("pressing Version 2 lands on V2, at ?v=2",
              w["v"] == "2" and w["search"] == "?v=2", f"{w['v']} {w['search']}")
        check("…and it is really V2: no deck mounted", w["deck"] == 0, str(w["deck"]))

        # THE NO-OP. A row that reloads the whole page to arrive where you
        # already are looks broken, so setPageVersion returns false instead.
        c.eval(OPEN_MENU)
        time.sleep(0.35)
        g = c.eval(VER_GROUP)
        check("the tick has moved with the page",
              g["ver"][1]["checked"] == "true" and g["ver"][0]["checked"] == "false",
              f"{g['ver'][0]['checked']} / {g['ver'][1]['checked']}")
        c.eval(PRESS_VER % "2")
        time.sleep(1.0)
        w = c.eval(WHERE)
        check("choosing the page you are on only closes the menu",
              w["v"] == "2" and w["search"] == "?v=2"
              and c.eval("(()=>{const m=document.querySelector('.pmenu');return !!m&&m.hidden})()"),
              f"{w['v']} {w['search']}")

        # AND BACK — to the PLAIN url, because V1 is the absence of the
        # parameter rather than `?v=1`.
        c.eval(OPEN_MENU)
        time.sleep(0.35)
        c.eval(PRESS_VER % "1")
        time.sleep(1.8)
        w = c.eval(WHERE)
        check("pressing Version 1 goes back to the plain URL",
              w["v"] == "1" and w["search"] == "", f"{w['v']} {w['search']!r}")
        check("…and V1's deck is mounted again", w["deck"] == 6, str(w["deck"]))
        errs = c.errors()
        check("no console errors across three switches", not errs,
              "; ".join(str(e)[:110] for e in errs[:3]))

    print()
    if fails:
        print(f"{len(fails)} FAILED: " + ", ".join(fails))
        sys.exit(1)
    print("ALL PASS")


main()

"""The home page against node 196:7243 — geometry, the rail, the sticky search.

    python3 tools/verify_home.py                      # 1024, the node's own width
    python3 tools/verify_home.py http://host/ 768     # another origin, another width

Every y and every size below is read off the Figma node, not off the build, so
this fails when the page drifts from the design rather than when it drifts from
whatever it happened to be. The sticky checks are the other half: the brief was
"no layout jump", so the test scrolls and asserts that every band is still at
the same DOCUMENT y it had at rest.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp import Chrome

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000/").rstrip("/") + "/"
URL = BASE + "index.html"
WIDTH = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
fails = []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
    if not ok:
        fails.append(name)


def near(a, b, tol=1.0):
    return a is not None and abs(a - b) <= tol


# node 196:7243 at 1024: (document y, height) of every band
FIGMA = {
    ".home-header":  (0, 140),
    ".search":       (140, 64),
    "#heroStage":    (228, 264),
    ".obs-head":     (540, 29),
    "#obsRail":      (585, 424.5),
    "#modulesHead":  (1053.5, 32),
    ".hero--estate": (1101.5, 164),
    # FOUR ROWS, NOT THE NODE'S FIVE. 884 is 5 x 164 + 4 x 16, which is what
    # the node draws and what this build drew until Reports' door came off the
    # default page on 4 Sep 2026 (see DEFAULT_LAYOUT in index.html). Twenty
    # cells in five columns is four rows exactly: 4 x 164 + 3 x 16 = 704. The
    # y above is unchanged, because nothing above the grid moved.
    "#moduleGrid":   (1281.5, 704),
}

BOXES = """(()=>{const o={};for(const s of %s){const e=document.querySelector(s);
  o[s]=e?(()=>{const r=e.getBoundingClientRect();return {y:+(r.y+scrollY).toFixed(2),x:+r.x.toFixed(1),
    w:+r.width.toFixed(1),h:+r.height.toFixed(2)}})():null}return o})()"""


def main():
    print(f"home page vs node 196:7243, {WIDTH}px")
    sel = list(FIGMA)
    with Chrome(width=WIDTH, height=1100) as c:
        c.goto(URL, settle=1.2)
        boxes = c.eval(BOXES % repr(sel))

        # ── the bands sit where the node puts them (1024 only: the node is 1024) ──
        if WIDTH == 1024:
            print("\nvertical rhythm")
            for s, (y, h) in FIGMA.items():
                b = boxes[s]
                check(f"{s} at y={y}", b and near(b["y"], y), f"drawn at {b['y'] if b else 'missing'}")
                check(f"{s} is {h} tall", b and near(b["h"], h), f"drawn {b['h'] if b else 'missing'}")

        # ── the band the deck sits on (node 196:7748's fill) ──────────────
        print("\nannouncement band")
        band = c.eval("""(()=>{const s=document.getElementById('heroStage');
          const cs=getComputedStyle(s,'::before'); const sr=s.getBoundingClientRect();
          const page=document.querySelector('.page').getBoundingClientRect();
          const pad=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--pad-page'));
          const gap=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--s6'));
          return {radius:cs.borderRadius, bg:cs.backgroundImage.slice(0,60), z:cs.zIndex,
                  h:+(sr.height+gap*2).toFixed(2), left:+(sr.left-pad-page.left).toFixed(1),
                  right:+(page.right-(sr.right+pad)).toFixed(1)}})()""")
        check("the band is 312 tall at the artboard width",
              near(band["h"], 312) or WIDTH != 1024, f"{band['h']}")
        check("its bottom corners are 32", band["radius"] == "0px 0px 32px 32px", band["radius"])
        check("it is a white→teal gradient", "gradient" in band["bg"] and "127" in band["bg"], band["bg"])
        check("it bleeds to both page edges", near(band["left"], 0) and near(band["right"], 0),
              f"left {band['left']} right {band['right']}")
        check("it paints behind the deck", band["z"] == "-1", band["z"])

        # ── the module grid, which must NOT have moved ────────────────────
        print("\nmodule grid (node 196:7384 — unchanged by this work)")
        g = c.eval("""(()=>{const g=document.getElementById('moduleGrid');const cs=getComputedStyle(g);
          const r=g.getBoundingClientRect();
          const cards=[...g.children].map(c=>{const b=c.getBoundingClientRect();
            return [Math.round(b.x-r.x),Math.round(b.y-r.y),Math.round(b.width),Math.round(b.height)]});
          return {w:+r.width.toFixed(1),gap:cs.gap,cols:cs.gridTemplateColumns.split(' ').length,cards}})()""")
        # width and column count are the node's, and the node is 1024; the gap
        # is Figma's at every width from the tablet band up
        check("grid is 960 wide", near(g["w"], 960) or WIDTH != 1024, f"{g['w']}")
        check("grid gap is 16", g["gap"] == "16px", g["gap"])
        check("grid has 5 columns", g["cols"] == 5 or WIDTH != 1024, str(g["cols"]))
        want = [(0, 0, 179, 164), (195, 0, 374, 164), (586, 0, 374, 164), (0, 180, 374, 164),
                (390, 180, 179, 164), (586, 180, 179, 164), (781, 180, 179, 164)]
        got = [tuple(x) for x in g["cards"][:7]]
        check("first seven cards match the node's packing", got == want or WIDTH != 1024, f"{got[:2]}…")
        # the node's card is 179.2 × 164; a 1×1 card must keep that shape at
        # every width, which is the whole reason the row height is derived
        ar = c.eval("""(()=>{const g=document.getElementById('moduleGrid');
          const c1=[...g.children].find(c=>{const b=c.getBoundingClientRect();
            return b.width < g.getBoundingClientRect().width/3});
          const b=c1.getBoundingClientRect(); return +(b.width/b.height).toFixed(3)})()""")
        # …at the artboard width and across the tablet band. 900–1023 is a
        # resized desktop window rather than a device and keeps the fixed row.
        want_ar = WIDTH <= 899 or WIDTH >= 1024
        check("a 1×1 card keeps the node's 1.093 proportion",
              near(ar, 1.0927, .02) or not want_ar, f"{ar}")

        # ── the observation rail ──────────────────────────────────────────
        print("\nrecent observations")
        o = c.eval("""(()=>{const rail=document.getElementById('obsRail');
          const cs=[...rail.querySelectorAll('.obs')]; const rr=rail.getBoundingClientRect();
          const b=(e)=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,w:+r.width.toFixed(1),h:+r.height.toFixed(2)}};
          const one=cs[0]; const page=document.querySelector('.page').getBoundingClientRect();
          const tops=cs.map(c=>getComputedStyle(c.querySelector('.obs__top')).backgroundColor);
          return {n:cs.length, card:b(one), gap:+(cs[1].getBoundingClientRect().x-cs[0].getBoundingClientRect().right).toFixed(1),
            top:b(one.querySelector('.obs__top')), body:b(one.querySelector('.obs__body')),
            overlap:+(b(one.querySelector('.obs__top')).y+b(one.querySelector('.obs__top')).h-b(one.querySelector('.obs__body')).y).toFixed(1),
            bleed:+(page.right-rr.right).toFixed(1), scrollable:rail.scrollWidth>rail.clientWidth+8,
            prios:[...new Set(cs.map(c=>c.dataset.priority))].sort(), tops:[...new Set(tops)].length,
            acts:one.querySelectorAll('.obs__act').length,
            noteLines:Math.round(b(one.querySelector('.obs__note')).h/24),
            tagRows:Math.round(b(one.querySelector('.obs__tags')).h/22)}})()""")
        check("six observations render", o["n"] == 6, str(o["n"]))
        check("card is 344 wide", near(o["card"]["w"], 344) or WIDTH < 768, f"{o['card']['w']}")
        check("card is 424.5 tall", near(o["card"]["h"], 424.5), f"{o['card']['h']}")
        check("rail gap is 10", near(o["gap"], 10), f"{o['gap']}")
        check("top section is 336×225", near(o["top"]["w"], 336, 8) and near(o["top"]["h"], 225), f"{o['top']['w']}×{o['top']['h']}")
        check("white block is 269.5 tall", near(o["body"]["h"], 269.5), f"{o['body']['h']}")
        check("it covers the colour's last 78px", near(o["overlap"], 78), f"{o['overlap']}")
        check("the rail runs to the page edge", near(o["bleed"], 0), f"{o['bleed']}px short")
        check("the rail scrolls", o["scrollable"])
        check("all four priorities are drawn", o["prios"] == ["critical", "high", "low", "moderate"], str(o["prios"]))
        check("each priority has its own colour", o["tops"] == 4, f"{o['tops']} distinct fills")
        check("three actions per card", o["acts"] == 3, str(o["acts"]))
        check("the note clamps to three lines", o["noteLines"] == 3, str(o["noteLines"]))

        # like toggles, and says so
        like = c.eval("""(()=>{const b=document.querySelector('.obs__act[data-act=like]');
          const before=b.querySelector('b').textContent; b.click();
          const after=b.querySelector('b').textContent; const on=b.getAttribute('aria-pressed');
          b.click(); return {before,after,on,back:b.querySelector('b').textContent,off:b.getAttribute('aria-pressed')}})()""")
        check("like counts up and reports itself pressed",
              int(like["after"]) == int(like["before"]) + 1 and like["on"] == "true", str(like))
        check("…and unlikes back to where it started",
              like["back"] == like["before"] and like["off"] == "false", str(like))

        # ── sticky search ─────────────────────────────────────────────────
        print("\nsticky search")
        rest = c.eval(BOXES % repr(sel))
        check("not stuck at rest", c.eval("!document.querySelector('.search-row').classList.contains('is-stuck')"))
        check("backdrop is invisible at rest",
              c.eval("+getComputedStyle(document.querySelector('.search-row'),'::before').opacity") == 0)
        c.eval("scrollTo(0, 700)")
        time.sleep(0.6)
        after = c.eval(BOXES % repr(sel))
        stuck = c.eval("""(()=>{const r=document.querySelector('.search-row');
          const f=document.querySelector('.search').getBoundingClientRect();
          const cs=getComputedStyle(r,'::before');
          return {cls:r.classList.contains('is-stuck'), top:+r.getBoundingClientRect().top.toFixed(1),
                  fieldTop:+f.top.toFixed(1), fieldH:+f.height.toFixed(1), op:+cs.opacity,
                  blur:cs.backdropFilter, z:getComputedStyle(r).zIndex}})()""")
        check("stuck after scrolling", stuck["cls"], str(stuck))
        check("the row is pinned at the viewport top", near(stuck["top"], 0), f"{stuck['top']}")
        check("the field keeps its 10px of glass above it", near(stuck["fieldTop"], 10), f"{stuck['fieldTop']}")
        # the resting height, not a literal 64: the field steps down with the
        # breakpoints and the point of the check is that STICKING changes it
        check("the field does not resize", near(stuck["fieldH"], rest[".search"]["h"]),
              f"{rest['.search']['h']} → {stuck['fieldH']}")
        check("the backdrop is fully in", near(stuck["op"], 1, .01), str(stuck["op"]))
        check("it is a blur, not a repaint of the row", "blur" in (stuck["blur"] or ""), str(stuck["blur"]))
        check("it sits under the sheets", 6 < int(stuck["z"]) < 400, stuck["z"])
        # the field itself is the thing that is pinned, so its document y is
        # SUPPOSED to change; every other band must not have moved a pixel
        moved = [s for s in sel if s != ".search" and rest[s] and after[s]
                 and abs(rest[s]["y"] - after[s]["y"]) > .01]
        check("NO LAYOUT JUMP: every band keeps its document y", not moved,
              "; ".join(f"{s} {rest[s]['y']}→{after[s]['y']}" for s in moved))
        check("no horizontal overflow", c.eval("document.documentElement.scrollWidth<=document.documentElement.clientWidth"),
              c.eval("document.documentElement.scrollWidth+' vs '+document.documentElement.clientWidth"))
        c.eval("scrollTo(0, 0)")
        time.sleep(0.6)
        check("unsticks on the way back", c.eval("!document.querySelector('.search-row').classList.contains('is-stuck')"))

        # this session runs with reduced motion FORCED, which is the half of
        # the reaction work that is easy to get wrong: an animation that is
        # skipped must not leave the DOM it would have spawned behind
        print("\nreactions under a reduced-motion preference")
        rm = c.eval("""(()=>{const b=document.querySelector('.obs__act[data-act=save]');
          b.click(); document.querySelector('.ann__like')?.click();
          return {litter:document.querySelectorAll('.rx-dot,.rx-ring,.rx-ghost').length,
                  anims:[...document.querySelectorAll('.obs,.obs__ico')].reduce((n,e)=>n+e.getAnimations().length,0),
                  saved:b.getAttribute('aria-pressed')}})()""")
        check("nothing is spawned and nothing animates", rm["litter"] == 0 and rm["anims"] == 0, str(rm))
        check("…but the state still changes", rm["saved"] == "true", str(rm["saved"]))

        print("\nconsole")
        errs = c.errors()
        check("no errors or exceptions", not errs, "; ".join(str(e)[:120] for e in errs[:3]))

    # ── motion, in its own browser: the harness forces reduced motion ──────
    print("\nreactions and the rail entrance, with motion on")
    with Chrome(width=WIDTH, height=1100, reduced_motion=False) as c:
        # CAUGHT IN FLIGHT, NOT AFTER. A finished animation is dropped from
        # getAnimations(), so waiting for the page to settle and then asking
        # whether it landed always answers no — which is a test that passes
        # only when the effect is broken. Navigate, then poll fast.
        c.cmd("Page.navigate", url=URL)
        seen, moved = 0, 0
        for _ in range(20):
            time.sleep(0.09)
            try:
                s = c.eval("""(()=>{const cs=[...document.querySelectorAll('.obs')];
                  if(!cs.length) return null;
                  return {n:cs.length,
                    named:cs.filter(e=>e.getAnimations().some(a=>a.id==='antz-land')).length,
                    off:cs.filter(e=>{const m=getComputedStyle(e).transform.match(/matrix\\(([^)]+)\\)/);
                      return m && Math.abs(+m[1].split(',')[4]) > 2}).length}})()""")
            except RuntimeError:
                continue
            if s:
                seen = max(seen, s["named"])
                moved = max(moved, s["off"])
        check("every rail card lands on arrival", seen == 6, f"{seen} of 6 animating")
        check("…starting off to the left, so the cascade is visible", moved >= 3, f"{moved} displaced")
        time.sleep(1.0)
        settled = c.eval("""[...document.querySelectorAll('.obs')].every(e=>{
          const cs=getComputedStyle(e); const m=cs.transform.match(/matrix\\(([^)]+)\\)/);
          return +cs.opacity>.99 && (!m || Math.abs(+m[1].split(',')[4])<.5)})""")
        check("…and settles flat, with nothing held forwards", settled)

        like = c.eval("""(()=>{const b=document.querySelector('.obs__act[data-act=like]');
          const ico=b.querySelector('.obs__ico'); const before=b.querySelector('b').textContent;
          b.click();
          return {before, after:b.querySelector('b').textContent, src:ico.querySelector('img').getAttribute('src'),
                  rings:ico.querySelectorAll('.rx-ring').length, dots:ico.querySelectorAll('.rx-dot').length,
                  ghosts:b.querySelectorAll('.rx-ghost').length, popping:ico.getAnimations().length}})()""")
        check("the count is right the instant it is clicked",
              int(like["after"]) == int(like["before"]) + 1, str(like))
        check("the glyph swaps to its liked state", like["src"].endswith("obs-like-on.svg"), like["src"])
        check("the icon springs", like["popping"] >= 1, str(like["popping"]))
        check("a ring and six radials go out", like["rings"] == 1 and like["dots"] == 6, str(like))
        check("the outgoing digit is a ghost, not the live one", like["ghosts"] == 1, str(like["ghosts"]))
        time.sleep(1.0)
        check("all of it removes itself", c.eval("document.querySelectorAll('.rx-dot,.rx-ring,.rx-ghost').length") == 0,
              str(c.eval("document.querySelectorAll('.rx-dot,.rx-ring,.rx-ghost').length")))

        save = c.eval("""(()=>{const b=document.querySelector('.obs__act[data-act=save]'); b.click();
          return {p:b.getAttribute('aria-pressed'), src:b.querySelector('img').getAttribute('src'),
                  anims:b.querySelector('.obs__ico').getAnimations().length}})()""")
        check("saving fills the bookmark and lifts it",
              save["p"] == "true" and save["src"].endswith("obs-bookmark-on.svg") and save["anims"] >= 1, str(save))

        ann = c.eval("""(()=>{const b=document.querySelector('.hero--slide[data-pos="0"] .ann__like');
          if(!b) return null; b.click();
          return {p:b.getAttribute('aria-pressed'), dots:b.querySelectorAll('.rx-dot').length}})()""")
        check("the announcement like reacts the same way",
              ann and ann["p"] == "true" and ann["dots"] == 6, str(ann))
        time.sleep(0.9)
        check("and clears up too", c.eval("document.querySelectorAll('.rx-dot,.rx-ring,.rx-ghost').length") == 0)

        errs = c.errors()
        check("no errors or exceptions (motion on)", not errs, "; ".join(str(e)[:120] for e in errs[:3]))

    print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

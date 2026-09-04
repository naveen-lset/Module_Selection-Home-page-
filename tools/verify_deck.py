"""The announcement deck under a finger — 4 Sep 2026.

    python3 tools/verify_deck.py                     # against http://127.0.0.1:8000, 1024 wide
    python3 tools/verify_deck.py http://host/ 768    # another origin, another width

Real motion, real touch events, at an iPad's 1024px. Each check drags the deck
and then SAMPLES every frame of what follows, because the two things the user
saw were both between frames: the front card springing back towards the
finger after a forward swipe, and a card pulled back in vanishing and fading
in a second time. A property read after the dust settles cannot see either.
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


STAGE = "#heroStage"
# every frame: [t, [[pos, translateX, scaleX, opacity] per slide]]
SAMPLER = """(()=>{
  const st = document.querySelector('%s'); const cards=[...st.querySelectorAll('.hero--slide')];
  window.__deck = []; const t0 = performance.now();
  const read = (el) => { const cs = getComputedStyle(el); const m = cs.transform.match(/matrix\\(([^)]+)\\)/);
    const v = m ? m[1].split(',').map(Number) : [1,0,0,1,0,0];
    return [el.dataset.pos, Math.round(v[4]), +v[0].toFixed(3), +(+cs.opacity).toFixed(3)] };
  (function s(){ window.__deck.push([Math.round(performance.now()-t0), cards.map(read)]);
     if (performance.now()-t0 < %d) requestAnimationFrame(s) })();
  return cards.length })()"""

STATE = """(()=>{const st=document.querySelector('#heroStage');
  return {active: st.getAttribute('aria-label'), pos:[...st.querySelectorAll('.hero--slide')].map(c=>c.dataset.pos),
          t: st.style.getPropertyValue('--t-deck'), inline:[...st.querySelectorAll('.hero--slide')].filter(c=>c.style.transform).length,
          overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth}})()"""


def point(x, y):
    return [{"x": x, "y": y, "radiusX": 8, "radiusY": 8, "force": 1}]


def swipe(c, frac, steps=14, dt=0.016, sample_ms=900):
    """A finger across the stage: frac of its width, negative = leftwards."""
    r = c.eval(f"(()=>{{const r=document.querySelector('{STAGE}').getBoundingClientRect();return {{x:r.x,y:r.y,w:r.width,h:r.height}}}})()")
    x0, y = r["x"] + r["w"] * (0.6 if frac < 0 else 0.4), r["y"] + r["h"] / 2
    c.cmd("Input.dispatchTouchEvent", type="touchStart", touchPoints=point(x0, y))
    time.sleep(0.05)
    for i in range(1, steps + 1):
        c.cmd("Input.dispatchTouchEvent", type="touchMove", touchPoints=point(x0 + r["w"] * frac * i / steps, y))
        time.sleep(dt)
    c.eval(SAMPLER % (STAGE, sample_ms))
    c.cmd("Input.dispatchTouchEvent", type="touchEnd", touchPoints=[])
    time.sleep(sample_ms / 1000 + 0.3)
    return c.eval("window.__deck"), r


def track(frames, i):
    """One card's (t, translateX, scale, opacity, pos) over the sampled frames."""
    return [(f[0], f[1][i][1], f[1][i][2], f[1][i][3], f[1][i][0]) for f in frames]


def while_leaving(tr):
    """The frames up to the moment the card that left is dropped behind the deck.

    With three slides that card is the next back sliver, so once it has GONE
    it snaps there invisibly and fades in — a second, deliberate motion that
    must not be read as the first one reversing."""
    out = []
    seen_gone = False
    for f in tr:
        if f[4] == "gone":
            seen_gone = True
        elif seen_gone:
            break
        out.append(f)
    return out


def monotonic(vals, direction, slack=1.5):
    """Never moves against `direction` by more than `slack` between frames."""
    bad = [(a, b) for a, b in zip(vals, vals[1:]) if (b - a) * direction < -slack]
    return not bad, (f"reversed {len(bad)}× e.g. {bad[0]}" if bad else "")


def main():
    print(f"announcement deck, {WIDTH}px, real motion")
    with Chrome(width=WIDTH, height=1366, reduced_motion=False) as c:
        c.goto(URL, settle=1.2)
        n = c.eval(f"document.querySelectorAll('{STAGE} .hero--slide').length")
        check("deck has at least three slides", n >= 3, f"{n} slides")
        s0 = c.eval(STATE)
        front = s0["pos"].index("0")

        # ── forward swipe: 30% of the width, then release ─────────────────
        frames, r = swipe(c, -0.30)
        full = track(frames, front)
        old = while_leaving(full)
        new = track(frames, s0["pos"].index("1"))
        ok, why = monotonic([f[1] for f in old], -1)
        check("front card never springs back towards the finger", ok, why or f"{old[0][1]}px → {old[-1][1]}px")
        ok, why = monotonic([f[3] for f in old], -1, .02)
        check("front card fades out in one direction", ok, why)
        check("front card leaves past half its width", old[-1][1] <= -r["w"] * .5, f"ended at {old[-1][1]}px")
        check("front card is invisible before it is dropped behind", old[-1][3] <= .03, f"opacity {old[-1][3]} at {old[-1][0]}ms")
        check("the card has landed inside 600ms", len(old) < len(full) and old[-1][0] <= 600, f"landed at {old[-1][0]}ms of {full[-1][0]}")
        ok, why = monotonic([f[1] for f in new], -1)
        check("next card closes up without stepping back", ok, why)
        ok, why = monotonic([f[2] for f in new], 1, .005)
        check("next card grows without shrinking", ok, why)
        s1 = c.eval(STATE)
        check("deck advanced one slide", s1["pos"][s0["pos"].index("1")] == "0", str(s1["pos"]))
        check("no inline styles or --t-deck left behind", s1["inline"] == 0 and s1["t"] == "", f"inline {s1['inline']} t {s1['t']!r}")
        check("no horizontal overflow during the turn", s1["overflow"] <= 0, f"{s1['overflow']}px")

        # ── backward swipe: 30% to the right ──────────────────────────────
        s1 = c.eval(STATE)
        prev_i = (s1["pos"].index("0") - 1 + n) % n     # the card before the front, in data order
        frames, r = swipe(c, 0.30)
        back = track(frames, prev_i)
        cur = track(frames, s1["pos"].index("0"))
        ok, why = monotonic([f[1] for f in back], 1)
        check("returning card slides in from the left in one motion", ok, why or f"{back[0][1]}px → {back[-1][1]}px")
        ok, why = monotonic([f[3] for f in back], 1, .02)
        check("returning card never vanishes and fades in again", ok, why)
        check("returning card starts where the finger left it", back[0][1] < -r["w"] * .15 and back[0][3] > .3, f"first frame {back[0]}")
        ok, why = monotonic([f[2] for f in cur], -1, .005)
        check("front card shrinks into the stack without growing", ok, why)
        s2 = c.eval(STATE)
        check("deck stepped back one slide", s2["pos"][prev_i] == "0", str(s2["pos"]))
        time.sleep(0.5)
        check("no inline styles or --t-deck left behind (back)", c.eval(STATE)["inline"] == 0 and c.eval(STATE)["t"] == "")

        # ── a quick flick, well under the 18% distance ────────────────────
        s2 = c.eval(STATE)
        frames, r = swipe(c, -0.09, steps=4, dt=0.004, sample_ms=500)
        s3 = c.eval(STATE)
        check("a fast short flick still turns the deck", s3["pos"][s2["pos"].index("1")] == "0", str(s3["pos"]))

        # ── a slow short drag springs back ────────────────────────────────
        s3 = c.eval(STATE)
        frames, r = swipe(c, -0.08, steps=10, dt=0.04, sample_ms=500)
        s4 = c.eval(STATE)
        check("a slow short drag springs back", s4["pos"] == s3["pos"], f"{s3['pos']} → {s4['pos']}")
        front_t = track(frames, s3["pos"].index("0"))
        check("…and the card returns to exactly 0", front_t[-1][1] == 0 and front_t[-1][3] == 1, str(front_t[-1]))

        # ── keys still turn it, both ways ─────────────────────────────────
        c.eval(f"document.querySelector('{STAGE}').focus()")
        c.cmd("Input.dispatchKeyEvent", type="keyDown", key="ArrowRight", code="ArrowRight", windowsVirtualKeyCode=39)
        c.cmd("Input.dispatchKeyEvent", type="keyUp", key="ArrowRight", code="ArrowRight", windowsVirtualKeyCode=39)
        time.sleep(0.8)
        s5 = c.eval(STATE)
        check("ArrowRight advances", s5["pos"][s4["pos"].index("1")] == "0", str(s5["pos"]))
        c.cmd("Input.dispatchKeyEvent", type="keyDown", key="ArrowLeft", code="ArrowLeft", windowsVirtualKeyCode=37)
        c.cmd("Input.dispatchKeyEvent", type="keyUp", key="ArrowLeft", code="ArrowLeft", windowsVirtualKeyCode=37)
        time.sleep(0.8)
        s6 = c.eval(STATE)
        check("ArrowLeft steps back", s6["pos"] == s4["pos"], f"{s4['pos']} → {s6['pos']}")

        print("\nconsole")
        errs = c.errors()
        check("no errors or exceptions", not errs, "; ".join(str(e)[:120] for e in errs[:3]))

    print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILED: " + ", ".join(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

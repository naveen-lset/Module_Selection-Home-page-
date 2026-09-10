"""The second home page — Figma nodes 236:6669, 270:4176 and 280:3521 — and the
widgets on it.

    python3 tools/verify_v2.py                      # 1024, the app's own width
    python3 tools/verify_v2.py http://host/ 768     # another origin, another width

V2 is `?v=2`: the same application drawing the composition node 236:6669 draws —
no announcement deck, no observation rail, the gradient band re-parented onto
the module grid, and Notes and My Focus Hub seeded into it. 270:4176 set the
four columns and the frame's row order; 280:3521 added Key Insights beside
Hospital, moved Pharmacy and Lab to the foot of the page, and drew the chat
disc beside the Quick Actions pill.

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
import json, os, sys, time
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
    /* the LIVE column count, read off the grid rather than off a media query,
       and the rows as drawn — cards grouped by their rendered top edge, which
       is the only place the packer's answer is visible */
    gridCols:getComputedStyle(q('#moduleGrid')).gridTemplateColumns.split(' ').length,
    rows:(()=>{const g=q('#moduleGrid').getBoundingClientRect(); const by=new Map();
      for(const e of cards){const t=Math.round(e.getBoundingClientRect().top-g.top);
        if(!by.has(t)) by.set(t, []); by.get(t).push(e.dataset.variant)}
      return [...by.entries()].sort((a,b)=>a[0]-b[0]).map(([,v])=>v)})(),
    /* KEY INSIGHTS · node 286:3940, the card node 280:3521 added. Everything
       here is either a number the frame states or a relationship the layout
       exists to hold — the ramp reaching the card at all, the figure in the
       library colour it names, and the two tiles carrying two DIFFERENT
       library colours, which is the whole reason they are not one tone. */
    ki:(()=>{const k=of('insights.key'); if(!k) return null;
      const cs=getComputedStyle(k);
      const v=k.querySelector('.l-headline__value');
      const lb=k.querySelector('.l-headline__label');
      const gl=k.querySelector('.c-head__icon img');
      const tiles=[...k.querySelectorAll('.l-headline__tile')];
      const tb=tiles[0]&&getComputedStyle(tiles[0]);
      return {fill:k.dataset.fill, size:k.dataset.size, layout:k.dataset.layout,
        w:+k.getBoundingClientRect().width.toFixed(1),
        h:+k.getBoundingClientRect().height.toFixed(1),
        ramp:cs.backgroundImage.slice(0, 40),
        title:k.querySelector('.c-head__text').textContent,
        glyph:!!gl&&gl.complete&&gl.naturalWidth>0,
        value:v&&v.textContent, valueColor:v&&getComputedStyle(v).color,
        label:lb&&lb.textContent,
        n:tiles.length,
        tiles:tiles.map(t=>({
          label:t.querySelector('.l-headline__tile-label').textContent,
          value:t.querySelector('.l-headline__tile-value').textContent,
          color:getComputedStyle(t.querySelector('.l-headline__tile-value')).color})),
        /* NOT A PLATE · 5% black under a blur, so the ramp still reads */
        tileBg:tb&&tb.backgroundColor,
        tileBlur:tb&&(tb.backdropFilter||tb.webkitBackdropFilter),
        /* the tiles reach half the card's padding from its edge and the head
           reaches a whole one — the frame's own asymmetry */
        tileRight:tiles[0]&&+(k.getBoundingClientRect().right
                              - tiles[0].getBoundingClientRect().right).toFixed(1),
        headLeft:+(k.querySelector('.c-head').getBoundingClientRect().left
                   - k.getBoundingClientRect().left).toFixed(1)}})(),
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

# what V2 seeds, in V2_LAYOUT's order — which is node 280:3521's own order, row
# by row, since 8 Sep 2026. The ink Focus Hub is off the page; everything else
# the frame draws is on it.
#
# WHAT CHANGED AGAINST 270:4176 and is therefore what this list is now guarding:
# Key Insights takes the 2-wide cell beside Hospital, and Pharmacy and Lab —
# which used to be that cell's two smalls — are at the foot beside My Focus Hub.
WANT = ['medical.default', 'housing.default', 'species.stats',
        'hospital.photo', 'insights.key',
        'notes.recent', 'diet.photo', 'administer.default', 'mortality.default',
        'eggs.default', 'audit.default', 'users.default', 'security.default',
        'focus.light', 'pharmacy.default', 'lab.default', 'approvals.pending']

# and the rows those seventeen pack into at the frame's four columns. Each entry
# is one row of the grid: the cards on it, in order, with the column span the
# frame gives them. A 2x2 appears on the row it starts.
WANT_ROWS = [
    ['medical.default', 'housing.default', 'species.stats'],
    ['hospital.photo', 'insights.key'],
    ['notes.recent', 'diet.photo'],
    ['administer.default', 'mortality.default'],
    ['eggs.default', 'audit.default', 'users.default', 'security.default'],
    ['focus.light', 'pharmacy.default', 'lab.default'],
    ['approvals.pending'],
]


PILL = """(()=>{
  const p=document.querySelector('.qa-pill'), t=document.querySelector('.qa-pill__t');
  const row=document.querySelector('.qa-row'), ch=document.querySelector('.qa-chat');
  const r=p&&p.getBoundingClientRect(), cs=p&&getComputedStyle(p);
  const rr=row&&row.getBoundingClientRect(), cr=ch&&ch.getBoundingClientRect();
  const chs=ch&&getComputedStyle(ch);
  const img=ch&&ch.querySelector('img');
  return {pill:!!p, fab:!!document.querySelector('.qa-fab'),
    band:!!document.querySelector('.qa-band'),
    w:r&&Math.round(r.width), h:r&&Math.round(r.height),
    /* THE ROW IS WHAT IS CENTRED SINCE NODE 286:3988, not the pill — see the
       note in the stylesheet. Measuring the pill here would fail on a page
       that is drawn exactly as the frame draws it. */
    centred:rr&&Math.abs((rr.left+rr.right)/2 - innerWidth/2)<2,
    fromFoot:rr&&Math.round(innerHeight-rr.bottom),
    label:t&&t.textContent, labelW:t&&Math.round(t.getBoundingClientRect().width),
    radius:cs&&cs.borderRadius, borderW:cs&&cs.borderTopWidth,
    bg:cs&&cs.backgroundImage, bgColor:cs&&cs.backgroundColor,
    /* THE MATERIAL, since node 295:5561 took the pair to glass. `ink` is read
       because the label went black with the fill, and `backdrop` because a
       40% fill with no filter behind it is not glass — it is a pale pill. */
    ink:cs&&cs.color, backdrop:cs&&(cs.backdropFilter||cs.webkitBackdropFilter),
    shadow:cs&&cs.boxShadow,
    /* the grid mark is MASKED now, not an <img>: one asset, coloured off the
       pill's own `color`, so `currentColor` moves it and the × together */
    gridMask:(()=>{const g=document.querySelector('.qa-pill__grid');
      if(!g)return null; const gs=getComputedStyle(g); const b=g.getBoundingClientRect();
      return {mask:(gs.maskImage||gs.webkitMaskImage||'none'), ink:gs.backgroundColor,
              size:(gs.maskSize||gs.webkitMaskSize||''),
              pos:(gs.maskPosition||gs.webkitMaskPosition||''),
              box:[Math.round(b.width),Math.round(b.height)]}})(),
    /* the chat disc */
    chat:!!ch, chatW:cr&&Math.round(cr.width), chatH:cr&&Math.round(cr.height),
    chatGap:(cr&&r)&&Math.round(cr.left-r.right),
    chatGlyph:!!img&&img.complete&&img.naturalWidth>0,
    chatGlyphW:img&&Math.round(img.getBoundingClientRect().width),
    chatLabel:ch&&ch.getAttribute('aria-label'),
    chatBgColor:chs&&chs.backgroundColor, chatBgImage:chs&&chs.backgroundImage,
    chatBackdrop:chs&&(chs.backdropFilter||chs.webkitBackdropFilter),
    chatShadow:chs&&chs.boxShadow, chatBorderW:chs&&chs.borderTopWidth,
    scrolled:document.querySelector('.qa').classList.contains('is-scrolled')}})()"""

MENU = """(()=>{
  const m=document.querySelector('.qa-menu'), r=m.getBoundingClientRect();
  const cs=getComputedStyle(m), v=getComputedStyle(document.querySelector('.qa-veil'));
  return {open:document.querySelector('.qa').classList.contains('is-open'),
    cells:m.querySelectorAll('.qa-act').length,
    tiles:m.querySelectorAll('.qa-mod').length,
    head:(m.querySelector('.qa-menu__head b')||{}).textContent,
    isModules:document.querySelector('.qa').classList.contains('qa--modules'),
    clip:cs.clipPath,
    panelBlur:cs.backdropFilter||cs.webkitBackdropFilter,
    w:Math.round(r.width), h:Math.round(r.height),
    onScreen:r.top>=-0.5 && r.bottom<=innerHeight+0.5,
    material:cs.backgroundColor, radius:cs.borderRadius,
    veilBlur:v.backdropFilter||v.webkitBackdropFilter, veilOpacity:v.opacity,
    /* the dim itself, and the blur's radius — read as numbers so the check can
       name a range rather than say "there is a blur of some sort" */
    veilColor:v.backgroundColor,
    veilAlpha:(()=>{const m=/rgba?\([^)]*?([\d.]+)\s*\)$/.exec(v.backgroundColor);
      return m?+m[1]:1})(),
    veilPx:(()=>{const m=/blur\(([\d.]+)px\)/.exec(v.backdropFilter||v.webkitBackdropFilter||'');
      return m?+m[1]:0})(),
    labelW:Math.round(document.querySelector('.qa-pill__t').getBoundingClientRect().width)}})()"""

# ── THE OPENING, RESOLVED INTO NUMBERS ────────────────────────────────────
# The clip-path is the whole animation, and its computed value is a string of
# calc()s — `inset(calc(63.07% - 54.95px) … round 24.52px)`. Rather than assert
# anything about that string, this resolves each side against the panel's own
# box and reports the WINDOW it describes: width, height, radius and centre, in
# pixels, panel-relative. That is what the eye sees, and it is comparable
# directly against the pill's box.
STATE = """(()=>{
  const qa=document.querySelector('.qa'), m=document.querySelector('.qa-menu');
  const p=document.querySelector('.qa-pill');
  const cs=getComputedStyle(m), r=m.getBoundingClientRect(), pr=p.getBoundingClientRect();
  const W=r.width, H=r.height;
  /* one <length-percentage> or calc() of the two, against its own axis */
  const len=(v,base)=>{
    v=String(v).trim();
    let x=/^calc\((-?[\d.]+)%\s*([-+])\s*([\d.]+)px\)$/.exec(v);
    if(x) return base*(+x[1])/100 + (x[2]==='-'?-(+x[3]):+(+x[3]));
    x=/^(-?[\d.]+)px$/.exec(v); if(x) return +x[1];
    x=/^(-?[\d.]+)%$/.exec(v);  if(x) return base*(+x[1])/100;
    return NaN;
  };
  /* split on top-level spaces only — the arguments contain calc(a - b) */
  const args=(str)=>{
    const out=[]; let d=0, cur='';
    for(const ch of str){
      if(ch==='(') d++; if(ch===')') d--;
      if(ch===' '&&d===0){ if(cur) out.push(cur); cur=''; } else cur+=ch;
    }
    if(cur) out.push(cur); return out;
  };
  const win=(()=>{
    const s=/^inset\((.*)\)$/.exec(cs.clipPath.replace(/\s+/g,' ').trim());
    if(!s) return null;
    let a=args(s[1]), rad=null;
    const i=a.indexOf('round');
    if(i>=0){ rad=len(a[i+1], W); a=a.slice(0,i); }
    const t=len(a[0],H),
          rt=len(a.length>1?a[1]:a[0],W),
          b=len(a.length>2?a[2]:a[0],H),
          l=len(a.length>3?a[3]:(a.length>1?a[1]:a[0]),W);
    return {t,rt,b,l,rad};
  })();
  const rows={}, spread={}, cellByRow={};
  const dly=(k)=>{const c=cellByRow[k]; if(!c) return null;
    return Math.round(parseFloat(getComputedStyle(c).transitionDelay)*1000)};
  for(const cell of document.querySelectorAll('.qa-act')){
    const k=cell.style.getPropertyValue('--qa-row').trim()||'0';
    const o=+(+getComputedStyle(cell).opacity).toFixed(2);
    if(!(k in rows)){ rows[k]=o; cellByRow[k]=cell }
    (spread[k]=spread[k]||[]).push(o);
  }
  /* the clip's own endpoints, so progress is a number and not a guess */
  const closedTop=H-52, openTop=-60;
  const prog=win?Math.max(0,Math.min(1,(closedTop-win.t)/(closedTop-openTop))):null;
  return JSON.stringify({
    winW:win&&+(W-win.l-win.rt).toFixed(1),
    winH:win&&+(H-win.t-win.b).toFixed(1),
    winR:win&&+win.rad.toFixed(1),
    winCx:win&&+(win.l+(W-win.l-win.rt)/2).toFixed(1),
    menuCx:+(W/2).toFixed(1),
    pillW:+pr.width.toFixed(1),
    pillCx:+(pr.left+pr.width/2-r.left).toFixed(1),
    progress:prog===null?null:+prog.toFixed(3),
    opacity:+(+cs.opacity).toFixed(2),
    grid:+(+getComputedStyle(document.querySelector('.qa-pill__grid')).opacity).toFixed(2),
    x:+(+getComputedStyle(document.querySelector('.qa-pill__x')).opacity).toFixed(2),
    rows,
    rowSpread:+Math.max(...Object.values(spread).map(v=>Math.max(...v)-Math.min(...v))).toFixed(3),
    /* THE DELAYS THEMSELVES, which is the only thing that PROVES the close is
       the open reversed. Opacity ordering cannot: in both directions the row
       nearest the FAB is the more opaque one, so "bottom leads" is true while
       opening and while closing. What differs is which row waits — so read the
       resolved transition-delay off the top and bottom cells and let the check
       compare them. */
    delayBottom:dly('0'), delayTop:dly(String(Object.keys(rows).length-1)),
  })})()"""

TILES = """(()=>{
  const grid=document.querySelector('.qa-menu__grid');
  const menu=document.querySelector('.qa-menu');
  const t=[...menu.querySelectorAll('.qa-mod')];
  const gcs=getComputedStyle(grid), mcs=getComputedStyle(menu);
  const uniq=(a)=>[...new Set(a)];
  const b=(e)=>e.getBoundingClientRect();
  const b0=b(t[0]), b1=b(t[1]), bRow2=b(t[4]);

  /* THE INK IS WHITE ON ALL NINETEEN · ruled 10 Sep. What is checked is no
     longer WHICH ink each colour favours but that every tile actually got
     white, plus the honest cost of that: the white-on-tile contrast, per
     tile, recomputed from the resolved background. WCAG relative luminance
     against white's 1.05. */
  const lum=(css)=>{
    const m=/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)/.exec(css);
    if(!m) return null;
    const ch=[1,2,3].map(i=>{const v=+m[i]/255;
      return v<=0.04045? v/12.92 : Math.pow((v+0.055)/1.055,2.4)});
    return 0.2126*ch[0]+0.7152*ch[1]+0.0722*ch[2];
  };
  /* white against the tile, which is the only ratio that applies now */
  const ratio=(css)=>{const L=lum(css); return 1.05/(L+0.05)};
  const nameOf=(x)=>x.querySelector('.qa-mod__t').textContent;

  return JSON.stringify({
    n:t.length,
    visible:t.filter(x=>{const r=b(x);return r.width>1&&r.height>1}).length,
    /* FLAT, NOT A RAMP · "Modules Colours fixed Colours Only" */
    withGradient:t.filter(x=>getComputedStyle(x).backgroundImage!=='none').length,
    distinctColours:uniq(t.map(x=>getComputedStyle(x).backgroundColor)).length,
    /* NO SHADOW ON THE MODULES · and no border either */
    withShadow:t.filter(x=>getComputedStyle(x).boxShadow!=='none').length,
    withBorder:t.filter(x=>parseFloat(getComputedStyle(x).borderTopWidth)>0).length,
    tileW:Math.round(b0.width), tileH:Math.round(b0.height),
    radius:Math.round(parseFloat(getComputedStyle(t[0]).borderTopLeftRadius)),
    gapX:Math.round(b1.left-b0.right), gapY:Math.round(bRow2.top-b0.bottom),
    cols:gcs.gridTemplateColumns.split(' ').length,
    panelPad:mcs.padding,
    panelW:Math.round(b(menu).width),
    clearOfRow:Math.round(b(document.querySelector('.qa-row')).top-b(menu).bottom),
    /* EVERY TILE'S RENDERED COLOUR, not the class that used to set it. The
       `--dark` class is gone; a stray one would show up as a non-white ink
       here rather than being counted. */
    notWhite:t.filter(x=>getComputedStyle(x).color!=='rgb(255, 255, 255)').map(nameOf),
    darkClass:t.filter(x=>x.classList.contains('qa-mod--dark')).length,
    /* the cost, named tile by tile: white fails AA on most of these and the
       3:1 non-text floor on the palest few. Recorded, not passed off. */
    worstRatio:Math.round(Math.min(...t.map(x=>ratio(getComputedStyle(x).backgroundColor)))*100)/100,
    worstTile:nameOf(t.reduce((a,x)=>
      ratio(getComputedStyle(x).backgroundColor)<ratio(getComputedStyle(a).backgroundColor)?x:a)),
    underThree:t.filter(x=>ratio(getComputedStyle(x).backgroundColor)<3).map(nameOf),
    /* which is why the shadow has to be there on every one of them */
    withShadowInk:t.filter(x=>getComputedStyle(x).textShadow!=='none').length,
    /* the glyphs are the modules' own exported files, loaded */
    glyphsLoaded:t.filter(x=>{const i=x.querySelector('.qa-mod__g img');
      return i && i.complete && i.naturalWidth>0}).length,
    /* and no label runs out of its tile */
    labelOverflow:t.filter(x=>{const l=x.querySelector('.qa-mod__t');
      return b(l).right>b(x).right-2 || b(l).bottom>b(x).bottom-1}).length,
    names:t.map(x=>x.querySelector('.qa-mod__t').textContent),
  })})()"""

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
# ── THE OPENING, RESOLVED INTO NUMBERS ────────────────────────────────────
# ONE SURFACE MOVES AND NOTHING ELSE DOES. Until 10 Sep each of the nineteen
# tiles flew out of the pill on its own measured vector, and this probe
# measured per-tile distances and launch ranks to prove the fan was a fan. The
# ruling — "Animation not at all good" — replaced all of it with a 220ms
# scale-and-fade of the panel from `50% 100%`, so what has to be measured now
# is the opposite claim: the PANEL is travelling, and NO TILE IS.
#
# THE ORIGIN IS CHECKED AS A POINT ON THE SCREEN, not as the string "50% 100%".
# A computed `transform-origin` of "356px 515px" tells you nothing on its own;
# what matters is whether that point lands on the pill, so it is resolved into
# viewport coordinates and compared with the pill's own centre. That is the
# check that would catch the panel growing from its middle, or from a corner,
# while the declaration still read plausibly.
SURFACE = """(()=>{
  const qa=document.querySelector('.qa'), m=document.querySelector('.qa-menu');
  const pill=document.querySelector('.qa-pill').getBoundingClientRect();
  const px=pill.left+pill.width/2, py=pill.top+pill.height/2;
  const t=[...m.querySelectorAll('.qa-mod')];
  const cs=(e)=>getComputedStyle(e);
  const mb=m.getBoundingClientRect();
  const scaleOfEl=(e)=>{const mt=/matrix\(([-\d.]+)/.exec(cs(e).transform);
    return mt? +mt[1] : 1};
  const scaleOf=(e)=>Math.round(scaleOfEl(e)*1000)/1000;
  /* THE ORIGIN, TURNED INTO A POINT IN THE VIEWPORT — and this is where the
     first version of this probe was wrong. `transform-origin` resolves in the
     element's UNTRANSFORMED coordinate space, while getBoundingClientRect()
     returns the box AFTER the scale. Adding one to the other reported the
     origin as 48px off the pill in a frame where the CSS was only 34px off,
     so the number was part artifact and part real bug. The scale is divided
     back out here: at scale s about origin o, a visual left edge sits at
     (trueLeft + o) - o*s, so trueLeft + o — the fixed point of the transform —
     is visualLeft + o*s. */
  const o=cs(m).transformOrigin.split(' ').map(parseFloat);
  const sc=scaleOfEl(m);
  return JSON.stringify({
    panelOpacity:+(+cs(m).opacity).toFixed(2),
    panelScale:scaleOf(m),
    clip:cs(m).clipPath,
    /* where the panel is actually growing FROM, against where the pill is —
       the fixed point of the scale, in viewport coordinates */
    originDX:Math.round((mb.left+o[0]*sc)-px),
    originDY:Math.round((mb.top+o[1]*sc)-py),
    /* NO TILE MOVES · every one of them full opacity, full size, in every
       frame, and — the real assertion — not one animation targeting a tile */
    tileOps:t.map(e=>+(+cs(e).opacity).toFixed(2)),
    tileScales:t.map(scaleOf),
    tileAnims:document.getAnimations().filter(a=>a.effect&&a.effect.target
      &&a.effect.target.classList
      &&a.effect.target.classList.contains('qa-mod')).length,
    /* and no tile carries the retired vectors or ranks */
    strayVectors:t.filter(e=>e.style.getPropertyValue('--qa-dx')
      ||e.style.getPropertyValue('--qa-i')).length,
    /* the pill's own morph is unchanged and still runs */
    grid:+(+cs(document.querySelector('.qa-pill__grid')).opacity).toFixed(2),
    x:+(+cs(document.querySelector('.qa-pill__x')).opacity).toFixed(2),
  })})()"""


# ── FREEZING WITHOUT GUESSING WHEN ────────────────────────────────────────
# Both measurements below used to be `sleep(0.004)` then pause, and both were
# a coin flip. `show()` clears `hidden`, measures its rows, and adds `is-open`
# only on the NEXT animation frame — so 4ms in, the transitions usually did not
# exist yet, `getAnimations()` came back EMPTY, nothing was paused, the real
# reveal then ran free, and every check below read whatever it happened to
# catch. That is why this file could pass twice and fail on a third run with
# no code change between them: observed 9 Sep 2026, PASS / PASS / 4 FAILED,
# reporting closed-state values (`0 of the way`, `grid=1 x=0`) for a panel
# that was opening correctly.
#
# Awaiting the state class AND a non-empty `getAnimations()` inside the page
# removes the guess entirely, and it is ONE round trip, so nothing can run
# between the wait and the pause.
#
# `hidden` IS NEUTRALISED HERE AND NOT BEFORE THE CLICK, which looks like it
# would be safer and is not: the override is a no-op SETTER over the IDL
# property, while `[hidden] { display: none }` matches the ATTRIBUTE. Installed
# before `show()` runs, it would swallow that method's own `hidden = false`,
# the attribute would never come off, and the panel would sit at
# `display: none` for the whole measurement.
def freeze_at(c, cls):
    c.eval("""(async()=>{
        await new Promise(res=>{const tick=()=>{
          const qa=document.querySelector('.qa');
          if(qa&&qa.classList.contains('%s')&&document.getAnimations().length)return res(1);
          requestAnimationFrame(tick)};tick()});
        const m=document.querySelector('.qa-menu');
        Object.defineProperty(m,'hidden',{get:()=>false,set:()=>{},configurable:true});
        document.getAnimations().forEach(a=>a.pause());
        return 1})()""" % cls, await_promise=True)


def main():
    print(f"V2 — node 280:3521, {WIDTH}px")

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

        print("\nthe seventeen cards it seeds")
        check("seventeen cards", o["n"] == 17, str(o["n"]))
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
        # THE ALIGNMENT RULING, 8 Sep 2026: V2 is four columns, not five, so the
        # frame's rows can be reproduced instead of approximated. This is the
        # check that would catch the page silently going back to five — the
        # order above would still pass, drawn into ragged rows.
        # …AND ONLY ABOVE 700, WHICH IS WHERE THE STYLESHEET GIVES V2 FOUR.
        # Below that the page is two columns on purpose — four at 660 is a
        # 140px card carrying a 32px glyph and a wrapping name, and a phone is
        # not the frame this ruling is about. These two ran unconditionally
        # and so reported a failure at any phone width for a page that was
        # drawing exactly what it is supposed to draw.
        if WIDTH >= 700:
            check("the grid is the frame's four columns", o["gridCols"] == 4, str(o["gridCols"]))
            check("…and the rows are the frame's, card for card",
                  o["rows"] == WANT_ROWS,
                  "as drawn" if o["rows"] == WANT_ROWS else str(o["rows"]))
        else:
            check("below 700 the grid is two columns, as the stylesheet says",
                  o["gridCols"] == 2, str(o["gridCols"]))
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

        # ══ KEY INSIGHTS ═══════════════════════════════════════════════════
        # The card node 280:3521 put on this page, and the first card in the
        # product whose fill belongs to no module.
        print("\nKey Insights")
        k = o["ki"]
        check("the card is on the page", k is not None,
              "" if k else "insights.key did not render")
        if k:
            check("at `medium`, which is the frame's 2x1", k["size"] == "medium",
                  str(k["size"]))
            check("…and 2 cells wide, not 1 or 3",
                  near(k["w"], 2 * (k["h"] * 1.125) + 16, 3) or WIDTH < 700,
                  f"{k['w']}x{k['h']}")
            check("it wears its own ramp, not a module's",
                  k["fill"] == "solid" and "gradient" in k["ramp"], str(k["ramp"]))
            check("the frame's bulb is exported, not drawn", k["glyph"], "")
            check("the head reads Key Insights", k["title"] == "Key Insights", k["title"])
            # THE FIGURE AND ITS COLOUR TOGETHER. A figure in the wrong colour
            # is the failure this card is most likely to have, because three
            # near-identical pale tones sit next to each other in the palette.
            check("32 Birth Animals, in MD3_Antz/notes",
                  k["value"] == "32" and k["label"] == "Birth Animals"
                  and k["valueColor"] == "rgb(252, 244, 174)",
                  f"{k['value']} / {k['label']} / {k['valueColor']}")
            check("two tiles, and they carry the frame's two counts",
                  k["n"] == 2
                  and [t["label"] for t in k["tiles"]] == ["Death", "Transfers"]
                  and [t["value"] for t in k["tiles"]] == ["02", "12"],
                  str(k["tiles"]))
            # …AND IN TWO DIFFERENT LIBRARY COLOURS. Collapsing these onto one
            # semantic tone is the tempting simplification and it is the wrong
            # one: see the palette block.
            check("…in ErrorContainer and SecondaryContainer, not one tone",
                  [t["color"] for t in k["tiles"]]
                  == ["rgb(255, 211, 211)", "rgb(175, 239, 235)"],
                  str([t["color"] for t in k["tiles"]]))
            check("the tiles are 5% black under a blur, not plates",
                  k["tileBg"] == "rgba(0, 0, 0, 0.05)" and "blur(2px)" in (k["tileBlur"] or ""),
                  f"{k['tileBg']} / {k['tileBlur']}")
            # THE FRAME'S ASYMMETRY, WHICH IS EASY TO TIDY AWAY BY ACCIDENT:
            # the tiles reach 8 from the card edge where the head starts at 16.
            check("…and they reach half the padding from the edge, where the head reaches a whole one",
                  near(k["tileRight"] * 2, k["headLeft"], 1.5),
                  f"tiles {k['tileRight']} / head {k['headLeft']}")

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

    # ── THE QUICK ACTIONS PILL — node 270:4176 ────────────────────────────
    # It replaced a corner FAB and a sixteen-cell dock on the ruling of 8 Sep
    # ("Remove Current Fab"), so the first check is that the FAB is GONE:
    # leaving both would put two ways to the same sixteen verbs on one page.
    #
    # THE COLLAPSE IS THE PART THAT CAN ROT SILENTLY. It is driven by the
    # sticky search row's observer — one signal, two consumers — so a change to
    # that observer breaks a behaviour on the other side of the page. Measured
    # as a WIDTH, not a class: the class is what the stylesheet reads, and the
    # question is whether the label actually went.
    print("\nthe Quick Actions row")
    with Chrome(width=WIDTH, height=768) as c:
        c.goto(BASE + "index.html?v=2", settle=2.2)
        r = c.eval(PILL)
        check("the pill is there and the FAB is not", r["pill"] and not r["fab"],
              f"pill={r['pill']} fab={r['fab']}")
        # 40 AND NOT THE NODE'S 109 — the ruling of 8 Sep; see --qa-b in the
        # stylesheet for why the artboard's number does not survive a page that
        # scrolls. Below 768 it is 24.
        want_b = 40 if WIDTH >= 768 else 24
        check(f"centred on the page, {want_b} from the foot",
              r["centred"] and near(r["fromFoot"], want_b, 1.5),
              f"centred={r['centred']} foot={r['fromFoot']}")
        # GLASS SINCE NODE 295:5561, where 280:3521 drew flat #37BD69 with a
        # white label and a white 1px stroke. The fill is asserted as RGBA and
        # not RGB on purpose: an opaque pill would satisfy a colour check and
        # have no glass in it whatever. `backgroundImage` stays `none` because
        # a leftover gradient would sit ON TOP of the fill and hide it.
        check("the frame's stadium, white-at-40% and a black label",
              r["radius"] == "999px" and r["borderW"] == "0px"
              and r["bgColor"] == "rgba(255, 255, 255, 0.4)"
              and r["ink"] == "rgb(0, 0, 0)" and r["bg"] == "none",
              f"{r['radius']} / {r['bgColor']} / {r['ink']} / border {r['borderW']}")
        # THE REFRACTION IS THE 9 SEP INSTRUCTION and the frame cannot draw it:
        # over a flat artboard a 40% fill renders flat, so this is the one part
        # of the material that only the build can be checked for.
        check("…and both controls actually refract what is behind them",
              "blur(20px)" in (r["backdrop"] or "")
              and "saturate(1.8)" in (r["backdrop"] or "")
              and "blur(20px)" in (r["chatBackdrop"] or ""),
              f"pill {r['backdrop']} | disc {r['chatBackdrop']}")
        # …BUT NOT EQUALLY, AND THAT IS THE RULING OF 9 SEP. The disc drops the
        # pill's saturation because amplifying the backdrop is what let the
        # backdrop's HUE win — see the departure note under `.qa-chat`.
        check("…the disc refracting less hard than the pill, deliberately",
              "saturate(1)" in (r["chatBackdrop"] or "")
              and "saturate(1.8)" not in (r["chatBackdrop"] or ""),
              r["chatBackdrop"])
        # ONE DEPTH FOR THE PAIR, where the previous frame gave them two and
        # both were transcribed. Compared as strings so they cannot drift.
        check("…on one shared drop, the node's dy2/blur4 at 25%",
              r["shadow"].startswith("rgba(0, 0, 0, 0.25) 0px 2px 4px 0px")
              and r["shadow"] == r["chatShadow"],
              f"same={r['shadow'] == r['chatShadow']} {r['shadow'][:46]}")
        # THE MARK IS MASKED, NOT A SECOND ASSET. 295:5561 exports it identical
        # to the committed file but `fill="black"`; if someone ever commits that
        # export and reverts to an <img>, the mask goes and this fails.
        check("…and the grid mark is the one asset, inked off the pill",
              r["gridMask"] and "qa-actions.svg" in r["gridMask"]["mask"]
              and r["gridMask"]["ink"] == "rgb(0, 0, 0)",
              f"{(r['gridMask'] or {}).get('ink')} via {(r['gridMask'] or {}).get('mask','')[-24:]}")
        # …AT 18.33 IN A 20 BOX, WHICH IS THE ONE THING 295:5580 CAUGHT WRONG.
        # The frame's glyph container is 20x20 (`fi_10348852`) holding artwork
        # inset `5.21% 3.14% 3.15% 5.21%` — 18.33 square at 1.042 from the top
        # left, the same number as the export's own 18.3294 viewBox. Sizing the
        # mask `100% 100%` stretched it over the full 20 and drew the mark 9%
        # too large: measured against the node's render, the glyph's ink box was
        # (16,16,20,20) against the frame's (17,17,18,18), and every column of
        # the glyph box differed while the label's did not. Fixed, both read
        # (17,17,18,18) and the region's mean error halves, 14.19 → 7.33.
        # The 20px BOX is asserted alongside the mask so a future change cannot
        # satisfy this by shrinking the container instead.
        check("…sized 18.33 inside the frame's 20px box, not stretched to it",
              r["gridMask"]["box"] == [20, 20]
              and r["gridMask"]["size"].startswith("18.33px 18.33px")
              and r["gridMask"]["pos"].startswith("1.042px 1.042px"),
              f"box {r['gridMask']['box']} mask {r['gridMask']['size']} at {r['gridMask']['pos']}")

        # THE DISC · 56 SINCE 295:5561, where every frame before drew the pair
        # the same height. It was in 270:4176 too and was never built; this is
        # what stops it being dropped again.
        check("the chat disc is beside it, 56 across — 4 more than the pill",
              r["chat"] and near(r["chatW"], 56, 1) and near(r["chatH"], 56, 1)
              and r["chatH"] > r["h"],
              f"{r['chatW']}x{r['chatH']} vs pill {r['w']}x{r['h']}")
        # ITS TINT: FITTED STOPS, AND ALPHAS THAT ARE NOT THE NODE'S.
        #
        # The STOPS are a measurement, not a preference. Figma's handles are at
        # 0%/100% of a gradient that runs PAST the disc; projected onto the box
        # they land at 50.5% and 94.8% along 142.21deg. Transcribing the handles
        # instead compresses the ramp into the shape and darkens its whole upper
        # half. Fitted against three sampled pixels, worst error 3/255.
        #
        # The ALPHAS are 55/35 where the node says 20/40, and that is a ruling
        # of 9 Sep 2026 rather than a transcription error — DO NOT "restore" it
        # to the node. At the node's alphas the disc takes whatever hue is
        # behind it: measured 16°, orange, over V1's coral observation card
        # against the node's own 189°, and three of V1's four priority colours
        # are warm. At 55/35 it measures 191° over that card and 189° over the
        # module grid. Both halves are asserted literally so either drifting
        # back fails here with the reason attached.
        check("…wearing the cyan→mint tint at its fitted stops and ruled alphas",
              r["chatBgColor"] == "rgba(255, 255, 255, 0.35)"
              and "142.21deg" in r["chatBgImage"]
              and "rgba(0, 175, 214, 0.55) 50.5%" in r["chatBgImage"]
              and "rgba(96, 221, 186, 0.55) 94.8%" in r["chatBgImage"]
              and r["chatBorderW"] == "0px",
              r["chatBgImage"][:96])
        check("…12 from the pill, which is the frame's gap",
              near(r["chatGap"], 12, 1), str(r["chatGap"]))
        check("…carrying the frame's own 24px glyph, loaded",
              r["chatGlyph"] and near(r["chatGlyphW"], 24, 1),
              f"loaded={r['chatGlyph']} {r['chatGlyphW']}px")
        # a disc with a glyph and no text has no accessible name without this
        check("…and it is named for a screen reader", r["chatLabel"] == "Chat",
              str(r["chatLabel"]))
        check("it reads \"Quick Actions\" at rest", r["label"] == "Quick Actions" and r["labelW"] > 60,
              f"{r['label']!r} at {r['labelW']}px")
        check("the wash is behind it", r["band"], "")

        # scrolled: the words go, the pill closes to a disc around its glyph
        c.eval("scrollTo(0, 600); 1")
        time.sleep(0.8)
        sc = c.eval(PILL)
        check("scrolled: the label collapses to nothing",
              sc["scrolled"] and sc["labelW"] == 0, f"scrolled={sc['scrolled']} label={sc['labelW']}px")
        # A TRUE CIRCLE SINCE THE PADDING BECAME THE NODE'S 16 all round: the
        # old 14 closed the pill to 48x52, a 4px oval that read as a near-miss.
        check("…and the pill is a circle, not a near-miss",
              abs(sc["w"] - sc["h"]) <= 1 and near(sc["w"], 52, 1),
              f"{sc['w']}x{sc['h']}")
        # the disc has no label to lose and must not move or resize with it
        check("…while the chat disc holds its size",
              near(sc["chatW"], 56, 1) and near(sc["chatH"], 56, 1),
              f"{sc['chatW']}x{sc['chatH']}")

        # the menu: nineteen modules on a white material, page softened
        c.eval("document.querySelector('.qa-pill').click(); 1")
        time.sleep(0.6)
        m = c.eval(MENU)
        # NINETEEN MODULES, NOT SIXTEEN VERBS · the 9 Sep ruling, built from
        # mockups/module-launcher.html variant 4A. `QA_CONTENT` in index.html
        # selects which, and 'modules' is the shipped setting — the verb panel
        # and all of `.qa-act` are still present behind that one constant,
        # which is why `cells` is asserted EMPTY rather than ignored: a panel
        # holding both would mean the switch had failed open.
        check("it opens all nineteen modules, and no verbs",
              m["open"] and m["isModules"] and m["tiles"] == 19 and m["cells"] == 0,
              f"tiles={m['tiles']} verbs={m['cells']} head={m['head']!r}")
        # A WHITE APPLE MATERIAL, where this was rgba(255,255,255,.94) at
        # radius 22 — and before that the profile menu's borrowed one. White at
        # a 30px blur with saturation lifted, and now 92% rather than the 62%
        # it wore over a light page. THE RULING OF 10 SEP NAMED THE PAGE'S
        # BACKGROUND, NOT THIS — 4A still rules a white panel — but 62% white
        # composites to a mid-grey slab over a black backdrop, so raising the
        # alpha is what keeps that ruling true rather than a change of mind
        # about the material.
        check("a white material of its own, and a real blur behind it",
              m["material"] == "rgba(255, 255, 255, 0.92)" and m["radius"] == "28px"
              and "blur(30px)" in (m["panelBlur"] or "")
              and "saturate(1.8)" in (m["panelBlur"] or ""),
              f"{m['material']} r={m['radius']} {m['panelBlur']}")
        # AND NO CLIP WINDOW, in any state. The verb panel unfolded out of the
        # pill's measured box by transitioning `clip-path`; the launcher scales
        # up out of the pill as one surface instead, and a clip window would
        # open over a panel that is already growing. Asserted because
        # `.qa.is-open .qa-menu` outranks the launcher's own rule on
        # specificity and put the clip back once.
        check("…and no clip window, which this panel does not unfold from",
              m["clip"] == "none", str(m["clip"]))
        # THE BACKDROP IS WHITE, AND THAT IS RULING FOUR on it in two days: the
        # profile menu's material, then a 6% dim, then black at 25% over 14px,
        # then "Instead of Background Should White Blured like Apple
        # background", with 4A chosen — white at 22% over a 16px blur — and
        # now, 10 Sep: "Background of main page should Black". Black at 82%
        # over the same 16px blur, with saturation back to 1 — 62% with the
        # saturation still lifted read as dark teal rather than black, since
        # what it dims is a page full of greens and blues.
        #
        # THE UPPER BOUND IS STILL THE POINT, and it is the one thing every
        # version of this instruction has kept: a launcher is a thing you
        # reach for FROM a page, so the page has to stay discernible behind
        # it. The blur is asserted as PRESENT for that reason — going to flat
        # opaque black would pass an "is it black" check and lose the page.
        check("the backdrop is a black blur, and stops short of hiding the page",
              m["veilOpacity"] == "1"
              and m["veilColor"].startswith("rgba(0, 0, 0")
              and .7 <= m["veilAlpha"] <= .9
              and 10 <= m["veilPx"] <= 24,
              f"{m['veilColor']} blur={m['veilPx']}px")
        check("the panel is wholly on screen", m["onScreen"], f"{m['w']}x{m['h']}")
        # THE LABEL COMES BACK WHILE IT IS OPEN, scrolled or not: the control
        # that opened the panel must not change shape under the finger.
        check("…and the pill wears its label again while open", m["labelW"] > 60, str(m["labelW"]))
        check("Escape closes it", c.eval(
            "(()=>{document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}));"
            "return 1})()") == 1)
        time.sleep(0.5)
        check("…and the panel is hidden, not merely faded",
              c.eval("document.querySelector('.qa-menu').hidden") is True)

        # back at the top the label returns on its own
        c.eval("scrollTo(0, 0); 1")
        time.sleep(0.8)
        top = c.eval(PILL)
        check("back at the top the label returns",
              not top["scrolled"] and top["labelW"] > 60,
              f"scrolled={top['scrolled']} label={top['labelW']}px")
        errs = c.errors()
        check("no console errors through any of it", not errs,
              "; ".join(str(e)[:110] for e in errs[:3]))

    # ══ NINETEEN COLOURED TILES, WHICH IS THE OPPOSITE OF WHAT WAS HERE ═══
    # This section used to enforce the 8 September brief's colour rules — "DO
    # NOT give every action a different color", one neutral wash, monochrome
    # glyphs, no plates. The launcher is a different component answering a
    # different question, and the 9 September ruling is explicitly the other
    # way: every module wears its own fixed colour. So the checks are inverted
    # rather than deleted, and what they now guard is the part that is easy to
    # get wrong — flat instead of a ramp, no shadow, one rhythm, and an ink
    # that suits the colour it sits on.
    print("\nthe nineteen module tiles")
    with Chrome(width=WIDTH, height=900) as c:
        c.goto(BASE + "index.html?v=2", settle=2.0)
        c.eval("document.querySelector('.qa-pill').click(); 1")
        time.sleep(0.9)
        g = json.loads(c.eval(TILES))
        check("all nineteen are there, and every one is drawn",
              g["n"] == 19 and g["visible"] == 19, f"{g['n']} tiles, {g['visible']} drawn")
        check("…carrying the modules' own names",
              g["names"][0] == "Medical" and "Commu\u00adnication" in g["names"],
              f"{g['names'][0]} … {g['names'][-1]!r}")
        # FIXED COLOURS, NOT GRADIENTS · "Modules Colours fixed Colours Only".
        # A ramp on any tile fails here, which is what would happen if someone
        # pointed --qa-mod-c back at a --g-* token.
        check("every tile is one flat colour, no ramp",
              g["withGradient"] == 0, f"{g['withGradient']} with a gradient")
        # AND SIXTEEN COLOURS FOR NINETEEN MODULES, which is the app's own
        # duplication made visible by flattening: pharmacy and reports both
        # resolve to #1ABEB6, and housing / followup / communication all to
        # #5A8088. Asserted so the number cannot drift unnoticed in either
        # direction — if it becomes nineteen someone has invented three hues.
        check("…sixteen distinct colours across the nineteen, as the app has it",
              g["distinctColours"] == 16, f"{g['distinctColours']} distinct")
        # NO SHADOW ON THE MODULES · 9 Sep. They had a two-layer drop while the
        # field ran the page width with nothing framing it; inside the panel it
        # only laid grey into the gutters.
        check("no tile carries a shadow or a border",
              g["withShadow"] == 0 and g["withBorder"] == 0,
              f"{g['withShadow']} shadowed, {g['withBorder']} bordered")
        # ONE RHYTHM, every number a multiple of 4: 150x70 tiles, a 16px
        # gutter on both axes, 32px of panel padding, and the panel 24px clear
        # of the row rather than the verb panel's 8.
        check("150x70 tiles at radius 14, on a 16px gutter both ways",
              g["tileW"] == 150 and g["tileH"] == 70 and g["radius"] == 14
              and g["gapX"] == 16 and g["gapY"] == 16,
              f"{g['tileW']}x{g['tileH']} r{g['radius']} gap {g['gapX']}/{g['gapY']}")
        check("…in four columns on a 712px panel with 32px padding",
              g["cols"] == 4 and g["panelW"] == 712 and g["panelPad"] == "32px",
              f"{g['cols']} cols, {g['panelW']}px, pad {g['panelPad']}")
        check("…standing 24 clear of the pill row, not 8",
              near(g["clearOfRow"], 24, 1), f"{g['clearOfRow']}px")
        # ONE INK ON ALL NINETEEN · ruled 10 Sep 2026, "text All has to be
        # white". This is the check that would have failed before the ruling:
        # the page used to set `.qa-mod--dark` on ten of them, and the value
        # read here is the RENDERED colour, so a returning class shows up as a
        # non-white ink rather than as a count that agrees with itself.
        check("every one of the nineteen labels is white",
              not g["notWhite"] and g["darkClass"] == 0,
              "all white" if not g["notWhite"]
              else f"not white: {g['notWhite']} (+{g['darkClass']} --dark)")
        # AND THE COST, RECORDED RATHER THAN PASSED OFF — this is what the
        # per-tile ink was buying. White fails AA (4.5) on fifteen of the
        # nineteen and the 3:1 non-text floor on the palest few: administer
        # #A9B7AD at 1.60:1 is the worst. The ruling is explicit and the
        # instruction is the authority, so this does NOT assert a floor it
        # cannot meet; it pins the worst case so a REGRESSION is still visible
        # — if it drops below 1.5 something has changed a colour token too.
        # The ways back to AA, if it is ever wanted: colour on an icon chip
        # with labels on a neutral wash (measured 13.20:1), or darken the four
        # palest tokens until white clears 4.5 on all nineteen.
        check("…and the palest tiles are the known ones, no worse",
              g["worstRatio"] >= 1.5,
              f"worst {g['worstTile']} {g['worstRatio']}:1; "
              f"under 3:1 → {g['underThree']}")
        # WHICH IS WHY THE SHADOW IS LOAD-BEARING NOW. At .35 it is the only
        # thing separating a white label from administer / lab / parivesh, so
        # a tile losing it is a real regression rather than lost polish.
        check("…each carrying the shadow that makes white legible on them",
              g["withShadowInk"] == 19, f"{g['withShadowInk']}/19")
        check("every glyph is the module's own file, loaded",
              g["glyphsLoaded"] == 19, f"{g['glyphsLoaded']}/19")
        check("no label runs out of its tile", g["labelOverflow"] == 0,
              str(g["labelOverflow"]))
        errs = c.errors()
        check("no console errors", not errs, "; ".join(str(e)[:110] for e in errs[:3]))

    # ══ THE OPENING · THE TILES FLY OUT OF THE PILL ════════════════════════
    # The verb panel unfolded: one surface whose clip-path started as the
    # pill's measured box and opened outward, staggered by ROW. The launcher
    # does the opposite — the surface just fades, and the nineteen tiles each
    # travel from the pill to their own slot. So this measures DISTANCE FROM
    # THE PILL per tile per frame, not a window.
    #
    # FROZEN AND SEEKED, never slept through — and the freeze awaits the
    # animations rather than guessing when they exist; see freeze_at().
    print("\nthe launcher opens as one surface")
    with Chrome(width=WIDTH, height=900, reduced_motion=False) as c:
        c.goto(BASE + "index.html?v=2", settle=2.0)
        # THE BUDGET IS THE RULING · 220ms, replacing a 560ms flight with
        # 342ms of stagger behind it. Asserted off the token because that is
        # what both the open and the close transitions read, and because the
        # point of the ruling was the total time.
        tok = c.eval("(()=>{const c=getComputedStyle(document.documentElement);"
                     "return [c.getPropertyValue('--qa-mod-open').trim(),"
                     "c.getPropertyValue('--qa-mod-close').trim()].join(' ')})()")
        check("it opens in 220ms and closes in 180, not the fan's 900",
              tok == "220ms 180ms", tok)

        c.eval("document.querySelector('.qa-pill').click(); 1")
        time.sleep(0.8)
        c.eval("document.querySelector('.qa-pill').click(); 1")
        time.sleep(0.6)
        c.eval("document.querySelector('.qa-pill').click(); 1")
        freeze_at(c, "is-open")

        def at(t):
            c.eval("(()=>{for(const a of document.getAnimations()){a.pause();"
                   "try{a.currentTime=%d}catch(e){}} return 1})()" % t)
            return json.loads(c.eval(SURFACE))

        f0 = at(0)
        # FRAME ZERO · the panel is small and invisible, and it is small FROM
        # THE PILL. .96 rather than the fan's .3: enough to read as arriving,
        # not enough to look like a modal zoom.
        check("frame 0: the panel is at 96% and invisible",
              f0["panelOpacity"] == 0 and 0.95 <= f0["panelScale"] <= 0.97,
              f"opacity {f0['panelOpacity']}, scale {f0['panelScale']}")
        # …AND GROWING FROM THE PILL. The origin point resolved into viewport
        # coordinates has to sit on the pill's centre horizontally; vertically
        # it sits at the panel's bottom edge, which is 24px above the pill's
        # own centre plus half the row — so the Y is checked as "below the
        # panel and above the pill", not as zero.
        check("…and it grows out of the pill, not out of its own middle",
              abs(f0["originDX"]) <= 2 and -60 <= f0["originDY"] <= 0,
              f"origin is {f0['originDX']}px, {f0['originDY']}px from the pill centre")
        check("…with no clip window, which this panel does not unfold from",
              f0["clip"] == "none", f0["clip"])
        # THE WHOLE POINT OF THE RULING · not one tile is animating, in the
        # first frame or any other. This is the check that fails if the fan
        # comes back in any form: a keyframe, a transition, or a stray
        # --qa-dx left on a tile by a returning measureFan().
        check("no tile animates at all — the surface is the only thing moving",
              f0["tileAnims"] == 0 and f0["strayVectors"] == 0,
              f"{f0['tileAnims']} tile animations, {f0['strayVectors']} stray vectors")
        check("…so all nineteen are full size and full opacity in frame 0",
              min(f0["tileOps"]) == 1 and set(f0["tileScales"]) == {1},
              f"opacity min {min(f0['tileOps'])}, scales {sorted(set(f0['tileScales']))}")
        check("…with the pill's glyph still the grid",
              f0["grid"] == 1 and f0["x"] == 0, f"grid={f0['grid']} x={f0['x']}")

        # MID-WAY · one movement, part-way through, on both properties at once.
        f = at(110)
        check("mid-open: the panel is part-way up and part-way out",
              0 < f["panelOpacity"] < 1 and 0.96 < f["panelScale"] < 1,
              f"opacity {f['panelOpacity']}, scale {f['panelScale']}")
        check("…and the tiles are still not moving",
              f["tileAnims"] == 0 and min(f["tileOps"]) == 1,
              f"{f['tileAnims']} tile animations, opacity min {min(f['tileOps'])}")

        # AND IT LANDS · full size, fully there, and the pill has become the ×.
        f = at(400)
        check("it lands: the panel at full size and fully there",
              f["panelOpacity"] == 1 and f["panelScale"] == 1,
              f"opacity {f['panelOpacity']}, scale {f['panelScale']}")
        check("…and the pill's glyph is the ×", f["grid"] == 0 and f["x"] == 1,
              f"grid={f['grid']} x={f['x']}")

    # ══ THE CLOSING · THE SURFACE GOES BACK INTO THE PILL ══════════════════
    print("\nthe launcher closes the same way")
    with Chrome(width=WIDTH, height=900, reduced_motion=False) as c:
        c.goto(BASE + "index.html?v=2", settle=2.0)
        c.eval("document.querySelector('.qa-pill').click(); 1")
        time.sleep(0.8)
        c.eval("document.querySelector('.qa-pill').click(); 1")
        # `is-closing` goes on synchronously, before `is-open` comes off
        freeze_at(c, "is-closing")

        def at2(t):
            c.eval("(()=>{for(const a of document.getAnimations()){a.pause();"
                   "try{a.currentTime=%d}catch(e){}} return 1})()" % t)
            return json.loads(c.eval(SURFACE))

        f = at2(0)
        check("frame 0 of the close: the panel is still full size and there",
              f["panelOpacity"] == 1 and f["panelScale"] == 1,
              f"opacity {f['panelOpacity']}, scale {f['panelScale']}")
        # IT REVERSES RATHER THAN CUTTING. The fan's close had a reverse
        # distance order to prove; this one has only to shrink back toward the
        # same origin, so what is asserted is that both properties are moving
        # DOWN together and the tiles are still inert.
        f = at2(90)
        check("…it contracts back toward the pill, fading as it goes",
              0 < f["panelOpacity"] < 1 and 0.96 <= f["panelScale"] < 1,
              f"opacity {f['panelOpacity']}, scale {f['panelScale']}")
        check("…and no tile is animating on the way out either",
              f["tileAnims"] == 0 and min(f["tileOps"]) == 1,
              f"{f['tileAnims']} tile animations, opacity min {min(f['tileOps'])}")
        f = at2(400)
        check("it ends on the pill: the surface gone, back at 96%",
              f["panelOpacity"] == 0 and 0.95 <= f["panelScale"] <= 0.97,
              f"opacity {f['panelOpacity']}, scale {f['panelScale']}")

    print()
    if fails:
        print(f"{len(fails)} FAILED: " + ", ".join(fails))
        sys.exit(1)
    print("ALL PASS")


main()

# -*- coding: utf-8 -*-
"""
tools/foliage.py — turns the supplied foliage artwork into the header asset.

    python3 tools/foliage.py            # from the project root

WHY THIS EXISTS. The artwork arrives as an opaque JPEG-ish PNG on its own flat
ground, rgb(228,241,244) — a blue that is not this product's mint canvas. Drop
it in as a background and it paints a visible rectangle of the wrong colour with
a hard edge on every side. So it is un-composited here: the ground is measured,
every pixel's departure from it becomes alpha, and the ink colour underneath is
recovered. What comes out is a transparent PNG that sits correctly on any
background, which is the only form in which a soft fade is even possible.

It is also made TILEABLE by mirroring, because the source is a one-off
illustration whose left and right edges do not meet. A mirrored pair always
does, so `background-repeat: repeat-x` has no seam at any viewport width.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, 'foliage-source.png')
OUT  = os.path.normpath(os.path.join(HERE, '..', 'assets', 'img', 'foliage.png'))

# The band worth keeping, and the crop is what positions the artwork on the
# page — there is no nudging in the CSS.
#
# Measured off the source by mean departure from the ground, row by row: the
# first leaf tips appear at y=105, the mass peaks at y=380, and it is back to
# bare paper by y=560. The header box is 220px and `background-size: auto 100%`
# maps this crop onto it, so the crop's proportions ARE the layout:
#
#   70   crop top      -> box y 0.    35px of clear paper above the first tips.
#   105  first tips    -> box y 31     — clear of the greeting, which starts at 32
#   380  peak of mass  -> box y 278
#   560  crop bottom   -> box y 440    the source's own fade, spent
#
# NEARLY THE WHOLE ILLUSTRATION, because the band it lands in is now deep: the
# planting runs the full height of the header, past the search field, and only
# begins to feather 40px below it. An earlier version cropped to 85-400 for a
# 220px box that stopped above the field, and at that depth a full crop scaled
# the leaves to nine pixels. There is room for all of it now.
CROP_TOP, CROP_BOTTOM = 70, 560

# Paper texture reads about 2.5/255 away from the ground even where there is no
# foliage. Left in, it becomes a faint grey haze over the whole header; this is
# subtracted before anything is normalised.
NOISE = 2.5

# THE ARTWORK IS ONE INK. Measured over every pixel with alpha above 0.55, the
# recovered colour spans 5 degrees of hue (177.7-183.1), three points of
# saturation and four of value — it is a single teal wash at varying density,
# not a multi-coloured illustration.
#
# So the recovered per-pixel colour is thrown away and this is written into all
# three channels instead. Nothing visible is lost, and the file drops from
# 1.6 MB to a fraction of it: constant RGB compresses to almost nothing, where
# the recovered values were noise at low alpha and defeated PNG entirely.
# It also puts the ink in one place, if it ever needs to be retuned.
INK = (94, 191, 192)          # #5EBFC0

# A mild lift on the midtones. The source is a very pale wash and the page then
# takes most of what is left away again through the mask, so straight linear
# alpha rendered almost invisible above the search field. Below 1.0 this raises
# the middle of the range without touching either end: the faintest paper stays
# transparent and the darkest ink stays solid, so no shape changes — the wash
# just carries.
ALPHA_GAMMA = 0.85

def main():
    src = Image.open(SRC).convert('RGB')
    w, h = src.size

    # the ground, measured rather than assumed — median of the four margins
    edge = []
    for box in ((0, 0, w, 8), (0, h - 8, w, h), (0, 0, 8, h), (w - 8, 0, w, h)):
        edge += list(src.crop(box).getdata())
    bg = tuple(sorted(c[i] for c in edge)[len(edge) // 2] for i in range(3))

    band = src.crop((0, CROP_TOP, w, CROP_BOTTOM))
    px = list(band.getdata())

    # the strongest ink in the picture sets the scale for full opacity
    peak = max(max(abs(p[i] - bg[i]) for i in range(3)) for p in px)

    out = []
    for p in px:
        dev = max(abs(p[i] - bg[i]) for i in range(3)) - NOISE
        if dev <= 0:
            out.append((0, 0, 0, 0))
            continue
        # un-composite: P = ink*a + bg*(1-a), solved for a against a known ink
        a = min(1.0, dev / (peak - NOISE)) ** ALPHA_GAMMA
        out.append(INK + (int(round(a * 255)),))

    cut = Image.new('RGBA', band.size)
    cut.putdata(out)

    # mirror-pair it so repeat-x is seamless at any width
    tile = Image.new('RGBA', (band.size[0] * 2, band.size[1]))
    tile.paste(cut, (0, 0))
    tile.paste(cut.transpose(Image.FLIP_LEFT_RIGHT), (band.size[0], 0))

    tile.save(OUT, optimize=True)
    print('ground %s   peak ink dev %d   tile %s   %.0f KB'
          % (bg, peak, tile.size, os.path.getsize(OUT) / 1024))

main()

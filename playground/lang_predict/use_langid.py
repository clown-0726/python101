import langid

"""
af, am, an, ar, as, az, be, bg, bn, br, bs, ca, cs, cy, da, de, dz, el, en, eo, es, et, eu, fa, fi, fo, fr, ga, gl, 
gu, he, hi, hr, ht, hu, hy, id, is, it, ja, jv, ka, kk, km, kn, ko, ku, ky, la, lb, lo, lt, lv, mg, mk, ml, mn, mr, 
ms, mt, nb, ne, nl, nn, no, oc, or, pa, pl, ps, pt, qu, ro, ru, rw, se, si, sk, sl, sq, sr, sv, sw, ta, te, th, tl, 
tr, ug, uk, ur, vi, vo, wa, xh, zh, zu
"""

# text = "Ceci est un exemple de texte en français. Il est utilisé pour tester la détection de la langue."
text = "你好你好"
lang, prob = langid.classify(text)

print(lang, prob)

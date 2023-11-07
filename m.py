import sys

c = 8
l = 4

def a(v: int, b: int, q: int) -> int:
    d = (v >> b) & 1
    e = d << (b * l + q)
    return e

def f(x: str, g: int, c: int = c) -> int:
    if x == '\x00':
        return 0
    o = ord(x)
    p = (a(o, b, g) for b in range(c))
    return sum(p)

def j(k: int, g: int) -> str:
    r = ((k >> (b * l + g)) & 1 for b in range(c))
    s = (d << b for b, d in enumerate(r))
    return chr(sum(s))

def m(t: str) -> int:
    u = []
    while len(t) > 0:
        w = t[:l].ljust(l, '\x00')
        t = t[l:]
        v = (
            f(y, g) for g, y in enumerate(w)
        )
        u.append(sum(v))
    return u

def n(h: list[int]) -> str:
    i = ''
    for k in h:
        m = (j(k, b) for b in range(l))
        i += ''.join(m).rstrip('\x00')
    return i


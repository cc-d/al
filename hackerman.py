#!/usr/bin/env python3
import sys
import logging
from unittest import TestCase, main

logging.basicConfig(level=logging.INFO)
l = logging.getLogger(__name__)

C = 8
L = 4


def b(v: int, i: int, x: int) -> int:
    return ((v >> i) & 1) << (i * L + x)


def e(c: str, x: int) -> int:
    return sum(b(ord(c), i, x) for i in range(C)) if c != '\x00' else 0


def d(v: int, x: int) -> str:
    return chr(sum(((v >> (i * L + x)) & 1) << i for i in range(C)))


def et(t: str) -> int:
    return sum(e(c, i) for i, c in enumerate(t[:L].ljust(L, '\x00')))


def dt(v: int) -> str:
    return ''.join(d(v, i) for i in range(L)).rstrip('\x00')


V = {
    (65,): 16777217,
    (70, 82, 69, 68): 251792692,
    (102, 111, 111): 124807030,
    (32, 102, 111, 111): 250662636,
    (102, 111, 111, 116): 267939702,
    (66, 73, 82, 68): 251930706,
    (46, 46, 46, 46): 15794160,
    (94, 94, 94, 94): 252706800,
    (87, 111, 111, 116): 266956663,
    (110, 111): 53490482,
}


class E(TestCase):
    def test_ed(self):
        for i, (t, v) in enumerate(V.items()):
            t = ''.join(chr(c) for c in t)
            ev = et(t)
            l.info(f'{i}: {t} -> {v} -> {ev}')
            self.assertEqual(ev, v)
            dv = dt(v)
            l.info(f'{i}: {v} <- {t} <- {dv}')
            self.assertEqual(dv, t)

        em = 'ccarterdev@gmail.com'
        ee = et(em)
        l.info(f'enc email: {ee}')
        de = dt(ee)
        l.info(f'dec email: {de}')
        print(10 * '@', ee, de, 10 * '@', sep='\n')


if __name__ == "__main__":
    main()

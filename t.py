import logging
import subprocess
from unittest import TestCase, main
from a import m, n

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
d = {...}  # Obfuscated test strings and their encoded equivalents.

class c(TestCase):
    def t(self):
        for i, tv in enumerate(d.items()):
            x, y = tv
            ex = m(x)
            log.info(f'{i}: ...')
            self.assertEqual(ex, y)
            dx = n(y)
            log.info(f'{i}: ...')
            self.assertEqual(dx, x)
            self.assertEqual(n(ex), x)

class b(TestCase):
    def t(self):
        r = [...]
        for s in r:
            log.info('...')
            ep = subprocess.Popen(
                ['python3', 'enc.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            eo, ee = ep.communicate(input=s)
            self.assertFalse(ee)
            dp = subprocess.Popen(
                ['python3', 'dec.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            do, de = dp.communicate(input=eo)
            self.assertFalse(de)
            self.assertEqual(do[:-1], s)
            log.info('...')

if __name__ == "__main__":
    main()


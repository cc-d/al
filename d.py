import re
import sys
from a import n

def q():
    if len(sys.argv) > 1:
        print("Usage: ...")
        sys.exit(0)
    z = sys.stdin.read().strip()
    v = re.findall(r"\d+", z)
    v = [int(i) for i in v]
    print(n(v))

if __name__ == "__main__":
    q()


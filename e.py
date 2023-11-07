import sys
from a import m

def q():
    if len(sys.argv) > 1:
        print("Usage: ...")
        sys.exit(0)
    z = sys.stdin.read()
    print(m(z))

if __name__ == "__main__":
    q()


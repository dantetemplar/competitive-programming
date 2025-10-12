# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(x: int, y: int, z: int) -> bool:
    # a & b = x
    # b & c = y
    # a & c = z

    # x & y = x & z
    # x & y = y & z
    # x & z = y & z

    if x & y != x & z:
        return False
    if x & y != y & z:
        return False
    if x & z != y & z:
        return False
    return True


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())
        res = solve(x, y, z)
        print("YES" if res else "NO")


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int]) -> bool:
    _ = [0] * (n)

    for i, a in enumerate(A):
        _[a - 1] = i

    min_pos = n + 1
    max_pos = -1

    added = 0

    for v in range(n, 0, -1):
        added += 1
        ppos = _[v - 1]
        if ppos < min_pos:
            min_pos = ppos
        if ppos > max_pos:
            max_pos = ppos
        d = max_pos - min_pos + 1
        if d != added:
            return False

    return True


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        res = solve(n, A)
        print("YES" if res else "NO")


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

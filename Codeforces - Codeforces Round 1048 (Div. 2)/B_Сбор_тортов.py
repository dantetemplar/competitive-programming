# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, m: int, furnaces: list[int]) -> int:
    furnaces.sort(reverse=True)
    s = 0
    for multiplier, furnace in enumerate(furnaces[:m]):
        s += furnace * (m - multiplier)

    return s


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        furnaces = list(map(int, input().split()))
        res = solve(n, m, furnaces)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

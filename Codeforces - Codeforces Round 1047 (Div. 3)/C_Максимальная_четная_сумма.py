# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(a: int, b: int) -> int:
    ab = a * b
    if ab % 2 == 1:
        return ab + 1
    elif b % 2 == 0:
        r2 = ab // 2 + 2
        if r2 % 2 == 0:
            return r2
    return -1


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        res = solve(a, b)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

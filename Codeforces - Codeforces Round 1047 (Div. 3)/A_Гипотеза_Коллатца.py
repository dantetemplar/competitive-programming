# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(k: int, x: int) -> int:
    return x * (2**k)


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        k, x = map(int, input().split())
        res = solve(k, x)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

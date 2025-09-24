# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, A: str) -> int:
    count0 = A.count('0')

    return A[:count0].count('1')


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        n = int(input())
        A = input()
        res = solve(n, A)
        print(res)
if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

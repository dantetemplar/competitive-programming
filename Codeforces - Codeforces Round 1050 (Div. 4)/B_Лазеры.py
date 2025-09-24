# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, m: int, x: int, y: int, h_lasers: list[int], v_lasers: list[int]) -> int:
    h_lasers_count = 0
    v_lasers_count = 0

    for h_laser in h_lasers:
        if h_laser <= y:
            h_lasers_count += 1

    for v_laser in v_lasers:
        if v_laser <= x:
            v_lasers_count += 1

    return h_lasers_count + v_lasers_count


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, input().split())
        h_lasers = list(map(int, input().split()))
        v_lasers = list(map(int, input().split()))

        res = solve(n, m, x, y, h_lasers, v_lasers)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, p_star: list[int]) -> list[int]:
    q_star = [0] * n
    for i, p_i in enumerate(p_star):
        q_star[i] = n + 1 - p_i
    return q_star


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
        p_star = list(map(int, input().split()))
        res = solve(n, p_star)
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

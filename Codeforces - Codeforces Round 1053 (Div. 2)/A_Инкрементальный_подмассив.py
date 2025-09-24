# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, m: int, A: list[int]) -> int:
    if A[0] == A[-1] - m + 1: # monotonic
        return n - A[-1] + 1
    else:
        return 1

# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        res = solve(n, m, A)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

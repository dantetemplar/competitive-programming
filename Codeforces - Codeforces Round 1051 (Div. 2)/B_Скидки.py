# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, k: int, A: list[int], B: list[int]) -> int:
    S = 0

    A.sort(reverse=False)
    B.sort(reverse=True)

    while B and A:
        b = B.pop()
        a = 0
        for _ in range(b):
            if not A:
                break
            a = A.pop()
            S += a
        else:
            S -= a

    while A:
        S += A.pop()

    return S


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(n, k, A, B)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

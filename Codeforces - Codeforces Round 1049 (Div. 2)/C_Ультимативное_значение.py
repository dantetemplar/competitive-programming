# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int]) -> int:
    f = 0
    sign = 1
    for a in A:
        f += sign * a
        sign = -sign

    INF = 10**30
    max_change = 0

    # Earliest index per parity for same-parity case (maximize r - l)
    first_idx = {0: None, 1: None}  # parity -> earliest index (1-based)

    # Running minima for cross-parity cases
    # For l odd, r even: (r + 2A[r]) - (l + 2A[l]) -> keep min (l + 2A[l]) over odd l
    min_odd_lp2a = INF
    # For l even, r odd: (r - 2A[r]) - (l - 2A[l]) -> keep min (l - 2A[l]) over even l
    min_even_lm2a = INF

    for r in range(1, n + 1):
        ar = A[r - 1]
        p = r % 2

        # same parity: r - l
        if first_idx[p] is not None:
            if r - first_idx[p] > max_change:
                max_change = r - first_idx[p]

        # cross parity:
        if p == 0:  # r even: l must be odd -> (r + 2A[r]) - min(l + 2A[l]) over odd l
            if min_odd_lp2a < INF:
                cand = (r + 2 * ar) - min_odd_lp2a
                if cand > max_change:
                    max_change = cand
        else:  # p == 1, r odd: l must be even -> (r - 2A[r]) - min(l - 2A[l]) over even l
            if min_even_lm2a < INF:
                cand = (r - 2 * ar) - min_even_lm2a
                if cand > max_change:
                    max_change = cand

        # update structures with current r for future positions
        if first_idx[p] is None:
            first_idx[p] = r  # earliest index of this parity

        if p == 1:
            # r is odd -> contributes to odd l pool
            val = r + 2 * ar
            if val < min_odd_lp2a:
                min_odd_lp2a = val
        else:
            # r is even -> contributes to even l pool
            val = r - 2 * ar
            if val < min_even_lm2a:
                min_even_lm2a = val

    if max_change > 0:
        f += max_change
    return f


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
        A = list(map(int, input().split()))
        res = solve(n, A)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

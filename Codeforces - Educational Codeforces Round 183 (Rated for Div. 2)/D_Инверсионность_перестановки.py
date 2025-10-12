# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, k: int):
    T = n * (n - 1) // 2
    if not (0 <= k <= T):
        return None
    need = T - k
    tri = [0] + [l * (l - 1) // 2 for l in range(1, n + 1)]

    # dp[len_used][sum_tri] = can reach using block lengths totaling len_used
    dp = [[False] * (need + 1) for _ in range(n + 1)]
    par = [[None] * (need + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for used in range(n + 1):
        for s in range(need + 1):
            if not dp[used][s]:
                continue
            for L in range(1, n - used + 1):
                t = s + tri[L]
                if t <= need and not dp[used + L][t]:
                    dp[used + L][t] = True
                    par[used + L][t] = (used, s, L)

    if not dp[n][need]:
        return None  # impossible → print 0

    # reconstruct lengths
    lengths = []
    u, v = n, need
    while u > 0:
        pu, pv, L = par[u][v]
        lengths.append(L)
        u, v = pu, pv
    lengths.reverse()

    # fill blocks: blocks get decreasing number ranges
    p, cur = [], n
    for L in lengths:
        p.extend(range(cur - L + 1, cur + 1))
        cur -= L
    return p


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        res = solve(n, k)
        print(" ".join(map(str, res)) if res is not None else "0")


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, s: str) -> str:
    c0 = s.count("0")
    c1 = s.count("1")
    r = s.count("2")

    ans = ["?"] * n

    # guaranteed removed by fixed pops
    for i in range(c0):
        ans[i] = "-"
    for i in range(n - c1, n):
        ans[i] = "-"

    L = c0 + 1
    R = n - c1

    if L <= R:
        m = R - L + 1
        if r == m:
            for i in range(L - 1, R): # many c2 will take off cards
                ans[i] = "-"
        elif r < m:
            # guaranteed stay
            left = L + r
            right = R - r
            if left <= right:
                for i in range(left - 1, right):
                    ans[i] = "+"
            # remaining inside [L,R] keep '?' already
        # r>m cannot happen since k<=n then r<=m
    return "".join(ans)


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        res = solve(n, s)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

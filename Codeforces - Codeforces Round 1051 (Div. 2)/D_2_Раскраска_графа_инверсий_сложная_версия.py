# ruff: noqa: F401
import bisect
import heapq
import itertools
from collections import Counter, defaultdict
from typing import Any, Generator, Iterable

# ----------------  Solution   ---------------- #
MOD = 10**9 + 7


class Fenwick:

    def __init__(self, n):
        self.a = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < len(self.a):
            self.a[i] += x
            i += i & -i


def solve(n: int, A: list[int]) -> int:
    fenRow = [Fenwick(n + 2) for _ in range(n + 1)]
    fenCol = [Fenwick(n + 2) for _ in range(n + 1)]
    fenRow[0].add(1, 1)
    fenCol[0].add(1, 1)
    for x in A:
        for i1 in range(0, x + 1):
            s = (fenRow[i1].sum(x + 1) - fenRow[i1].sum(i1)) % MOD
            fenRow[i1].add(x + 1, s)
            fenCol[x].add(i1 + 1, s)

        for i2 in range(x + 1, n + 1):
            s = fenCol[i2].sum(x + 1) % MOD
            fenRow[x].add(i2 + 1, s)
            fenCol[i2].add(x + 1, s)

    S = sum(fenRow[i].sum(n + 1) for i in range(n + 1)) % MOD
    return S


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        res = solve(n, A)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

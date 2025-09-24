# ruff: noqa: F401
import bisect
import heapq
import itertools
from collections import Counter, defaultdict
from typing import Any, Generator, Iterable

# ----------------  Solution   ---------------- #
MOD = 10**9 + 7


def solve(n: int, A: list[int]) -> int:
    dp = defaultdict(int)
    # (a, b) -> number of good subsequences represented as two increasing tails (a, b)
    S = 0
    for v in A:
        S = (S * 2) % MOD

        for (a, b), val in list(dp.items()):
            if v < b:  # (A good subsequence becomes bad)
                S += val
            elif v > a: # (Extending the larger tail)
                dp[(v, b)] = (dp[(v, b)] + val) % MOD
            elif v < a: # (Extending the smaller tail)
                dp[(a, v)] = (dp[(a, v)] + val) % MOD
            else: # (Extending with an equal value), v == a or v == b 
                dp[(a, b)] = (dp[(a, b)] + val) % MOD
        dp[(v, 0)] = (dp[(v, 0)] + 1) % MOD

    return (pow(2, n, MOD) - S) % MOD


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

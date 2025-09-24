# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int]) -> tuple[int, int]:
    S = 0
    prefix_sum = [0]
    postfix_sum = [0]
    for a in A:
        prefix_sum.append(prefix_sum[-1] + a)
        S += a

    for a in A[::-1]:
        postfix_sum.append(postfix_sum[-1] + a)

    postfix_sum = postfix_sum[::-1]

    for l, prefix_sum_l in enumerate(prefix_sum):
        for r in range(l + 2, n + 1):
            postfix_sum_r = postfix_sum[r]
            center_part = S - prefix_sum_l - postfix_sum_r
            c3 = center_part % 3
            p3 = prefix_sum_l % 3
            ps3 = postfix_sum_r % 3
            # all equal
            if (c3 == p3) and (ps3 == p3):
                return l + 1, r
            # or all are different
            elif (c3 != p3) and (ps3 != p3) and (c3 != ps3):
                return l + 1, r

    return 0, 0


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
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

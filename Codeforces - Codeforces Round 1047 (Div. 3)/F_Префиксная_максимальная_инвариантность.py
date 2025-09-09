# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int], B: list[int]) -> int:
    S = 0
    prefix_max_matrix = []

    for l in range(n):
        previous_max_value = 0
        prefix_max_row = []
        for i, v in enumerate(A):
            if i < l:
                prefix_max_row.append((False, 0))
                continue

            if previous_max_value >= v:
                prefix_max_row.append((True, previous_max_value))
            else:
                prefix_max_row.append((False, v))
                previous_max_value = v
        prefix_max_matrix.append(prefix_max_row)

    for l in range(n):
        prefix_max_row = prefix_max_matrix[l]

        for r in range(l + 1, n + 1):
            S += f(A[l:r], B[l:r], prefix_max=prefix_max_row, l=l, r=r)

    return S


def f(
    A_sub: list[int] | tuple[int, ...],
    B_sub: list[int] | tuple[int, ...],
    prefix_max: list[tuple[bool, int]],
    l: int,
    r: int,
) -> int:
    s = 0

    for b, (same_as_previous, prefix_max_value) in zip(B_sub, prefix_max[l : r + 1]):
        if same_as_previous and b <= prefix_max_value:
            s += 1
        elif not same_as_previous and b == prefix_max_value:
            s += 1

    return s


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
        B = list(map(int, input().split()))
        res = solve(n, A, B)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

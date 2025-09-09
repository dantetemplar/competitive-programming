# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict, deque
from typing import Any, Generator


# ----------------  Solution   ---------------- #
def solve(n: int, q: int, A: list[int], LR: list[tuple[int, int]]) -> list[bool]:
    res = []
    for l, r in LR:
        A_sub = A[l-1:r]

        for i in range(len(A_sub) - 2):
            i1, i2, i3 = i, i + 1, i + 2
            a1, a2, a3 = A_sub[i1], A_sub[i2], A_sub[i3]

            if a3 < a2 < a1: # monotonic
                res.append(False)
                break
        else:
            res.append(True)
    return res


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        A = list(map(int, input().split()))
        LR = []
        for _ in range(q):
            l, r = map(int, input().split())
            LR.append((l, r))
        res = solve(n, q, A, LR)
        for r in res:
            print("YES" if r else "NO")


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

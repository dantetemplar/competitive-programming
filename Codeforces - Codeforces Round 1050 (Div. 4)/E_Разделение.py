# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, k: int, A: list[int]) -> int:
    if n % k != 0:
        return 0

    target = Counter(A)
    for value, count in target.items():
        if count % k != 0:
            return 0
        else:
            target[value] = count // k


    cur = defaultdict(int)
    l = 0
    total = 0

    for r, x in enumerate(A):
        cur[x] += 1

        while cur[x] > target[x]:
            y = A[l]
            cur[y] -= 1
            l += 1

        total += (r - l + 1)

    return total


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        res = solve(n, k, A)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

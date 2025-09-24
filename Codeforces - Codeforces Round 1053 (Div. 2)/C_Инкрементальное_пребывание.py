# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int]) -> list[int]:
    m = 2 * n
    gaps = [A[i+1] - A[i] for i in range(m - 1)]  # 1..2n-1 gaps (0-based)
    # Buckets by s_i = min(i, 2n - i), using 1-based gap index
    SO = [0] * (n + 2)  # odd-index gaps
    SE = [0] * (n + 2)  # even-index gaps
    for idx in range(1, m):  # idx = 1..2n-1
        s = min(idx, m - idx)
        if idx % 2 == 1:
            SO[s] += gaps[idx - 1]
        else:
            SE[s] += gaps[idx - 1]
    # Suffix sums so SO[k] = sum over s>=k; same for SE
    for k in range(n - 1, 0, -1):
        SO[k] += SO[k + 1]
        SE[k] += SE[k + 1]
    ans = [0] * (n + 1)
    # k = 1
    ans[1] = sum(gaps[0::2])  # odd indices (1-based)
    # k >= 2
    for k in range(2, n + 1):
        inc = 2 * (SO[k] if k % 2 == 1 else SE[k])
        ans[k] = ans[k - 1] + inc
    return ans[1:]

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
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

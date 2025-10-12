# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, s: str) -> int:
    # a -> +1, b -> -1
    a = s.count("a")
    b = n - a
    D = a - b
    if D == 0:
        return 0

    S = 0
    last = {0: 0}  # prefix sum -> latest index (0..n)
    ans = n + 1

    for i, c in enumerate(s, 1):  # i = length of prefix
        S += 1 if c == "a" else -1
        need = S - D  # want S[j] == need with j < i
        if need in last:
            ans = min(ans, i - last[need])
        # store latest index to minimize length
        last[S] = i

    return -1 if ans >= n else ans


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        res = solve(n, s)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

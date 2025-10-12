# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, B: list[int]) -> int:
    B.sort()

    answer = 1
    prev = B[0]

    for b in B[1:]:
        if b > prev:
            answer += 1
            prev = b

    return answer


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        B = list(map(int, input().split()))
        res = solve(n, B)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

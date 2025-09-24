# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, m: int, S: str, A: list[int]) -> tuple[int, list[int]]:
    blacks = set(A)
    result = set(blacks)

    pos = 1
    for c in S:
        if c == "A":
            pos += 1
        else:  # 'B'
            y = pos + 1
            while y in result:
                y += 1
            pos = y
        
        result.add(pos)

        if c == "B":
            y = pos + 1
            while y in result:
                y += 1
            pos = y

    res = sorted(result)
    return len(res), res


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        S = input()
        A = list(map(int, input().split()))
        k, res = solve(n, m, S, A)
        print(k)
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

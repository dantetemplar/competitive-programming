# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(k: int, x: int) -> tuple[int, list[int]]:
    for n in range(0, k + 1):
        
        if x % (2 ** (1 + k - n)) == 2 ** (k - n):
            steps = []

            for i in range(1, n + 1):
                pos = k - n + i
                bit = (x >> pos) & 1
                if bit == 1:
                    steps.append(2)
                else:
                    steps.append(1)

            return n, steps

    return -1, []

# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        k, x = map(int, input().split())
        res = solve(k, x)
        if res:
            print(res[0])
            print(" ".join(map(str, res[1]) or " "))
        else:
            print("-")

if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

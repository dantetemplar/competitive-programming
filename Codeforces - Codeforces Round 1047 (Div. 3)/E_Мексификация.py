# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, k: int, A: list[int]) -> int:
    # Frequency array: size n+2 is enough
    freq = [0] * (n + 2)
    for a in A:
        freq[a] += 1

    # Correct number of steps (from editorial)
    steps = min(k, (k % 2) + 2)

    for _ in range(steps):
        # Compute mex in O(n)
        mex = 0
        while mex < len(freq) and freq[mex] > 0:
            mex += 1

        new_freq = [0] * (n + 2)
        for val, count in enumerate(freq):
            if count == 0:
                continue
            if val < mex and count == 1:
                new_freq[val] += 1
            else:
                new_freq[mex] += count
        freq = new_freq

    # Compute final sum
    return sum(val * count for val, count in enumerate(freq))

    
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
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

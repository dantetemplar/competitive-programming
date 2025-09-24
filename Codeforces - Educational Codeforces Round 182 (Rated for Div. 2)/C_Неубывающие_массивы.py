# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any

# ----------------  Solution   ---------------- #
MODULUS = 998244353

def solve(n: int, A: list[int], B: list[int]) -> int:
    DP_prev = [1, 1]

    for i in range(1, n):
        DP_curr = [0, 0]
        for swap_prev in (0, 1):
            if DP_prev[swap_prev] == 0:
                continue

            A_prev = A[i - 1] if swap_prev else B[i - 1]
            B_prev = B[i - 1] if swap_prev else A[i - 1]

            for swap_cur in (0, 1):
                A_cur = A[i] if swap_cur else B[i]
                B_cur = B[i] if swap_cur else A[i]
                if A_cur >= A_prev and B_cur >= B_prev:
                    DP_curr[swap_cur] += DP_prev[swap_prev]
                    DP_curr[swap_cur] %= MODULUS

        DP_prev = DP_curr

    return (DP_prev[0] + DP_prev[1]) % MODULUS


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

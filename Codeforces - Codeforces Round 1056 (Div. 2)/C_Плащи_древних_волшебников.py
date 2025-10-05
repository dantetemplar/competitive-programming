# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any

# ----------------  Solution   ---------------- #
M = 676767677


def compute_a(seq):
    n = len(seq)
    prefR = 0
    sufL = seq.count('L')
    res = []
    for i, c in enumerate(seq):
        if c == 'R':
            prefR += 1
        res.append(prefR + sufL)
        if c == 'L':
            sufL -= 1
    return res


def solve(n: int, A: list[int]) -> int:
    d = [A[i+1] - A[i] for i in range(n-1)]
    cnt = 0
    for start in ['L', 'R']:
        s = [start]
        ok = True
        for diff in d:
            prev = s[-1]

            if diff == -1 and prev == 'L':
                s.append('L')
            elif diff == 0 and prev == 'L':
                s.append('R')
            elif diff == 0 and prev == 'R':
                s.append('L')
            elif diff == 1 and prev == 'R':
                s.append('R')
            else:
                ok = False
                break
        if ok and compute_a(s) == A:
            cnt += 1
            
    return cnt


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
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

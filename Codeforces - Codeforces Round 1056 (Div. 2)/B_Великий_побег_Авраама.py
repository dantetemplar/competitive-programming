# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, k: int):
    total = n * n

    r = total - k

    if r == 1 or r < 0:
        return False, None

    table = []

    for i in range(n):
        row = []
        flag = bool(r)
        for j in range(n):
            if r > 0:
                r -= 1
                if j == n - 1:
                    row.append("L")
                else:
                    row.append("R")
            else:
                if flag:
                    flag = False
                    if j == 1:
                        row[-1] = "U"
                    else:
                        row[-1] = "L"
                row.append("D")

        table.append("".join(row))
    return True, table


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        yer_or_no, table = solve(n, k)
        print("YES" if yer_or_no else "NO")
        if yer_or_no:
            print("\n".join(table))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

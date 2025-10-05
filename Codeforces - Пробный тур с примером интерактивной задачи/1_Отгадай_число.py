# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
import sys
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def step(x) -> str:
    sys.stdout.write(f"{x}\n")
    sys.stdout.flush()
    s = sys.stdin.readline().strip()
    return s


def answer(x: int) -> None:
    sys.stdout.write(f"! {x}\n")
    sys.stdout.flush()


def solve() -> None:
    # min 1, max 1_000_000
    # use binary search to find
    left = 1
    right = 1_000_000
    while left < right:
        mid = (left + right + 1) // 2
        s = step(mid)
        if s == ">=":
            left = mid
        elif s == "<":
            right = mid - 1
        else:
            answer(mid)
            return
    answer(left)


# ----------------  Input/Output   ---------------- #
def main():
    solve()


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

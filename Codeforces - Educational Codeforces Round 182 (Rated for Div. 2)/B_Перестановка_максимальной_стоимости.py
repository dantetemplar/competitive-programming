# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


def sub_plus_1_or_0(a: int | None, b: int | None) -> int:
    if a is None or b is None:
        return 0
    return a - b + 1


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int]) -> int:
    zeros_positions = []
    visited = set()
    min_bad_placed_pos = None
    max_bad_placed_pos = None
    for i, a in enumerate(A):
        if a == 0:
            zeros_positions.append(i)
        else:
            visited.add(a)
            if a != i + 1:
                if min_bad_placed_pos is None:
                    min_bad_placed_pos = i
                max_bad_placed_pos = i
    to_place = set(range(1, n + 1)) - visited
    least_bad_placed_pos = None
    most_bad_placed_pos = None

    for to_place_value in to_place:
        for to_place_pos in zeros_positions:
            if to_place_pos + 1 != to_place_value:
                least_bad_placed_pos = to_place_pos
                break
        for to_place_pos in zeros_positions[::-1]:
            if to_place_pos + 1 != to_place_value:
                most_bad_placed_pos = to_place_pos
                break
        if least_bad_placed_pos is not None:
            min_bad_placed_pos = (
                min(min_bad_placed_pos, least_bad_placed_pos)
                if min_bad_placed_pos is not None
                else least_bad_placed_pos
            )
        if most_bad_placed_pos is not None:
            max_bad_placed_pos = (
                max(max_bad_placed_pos, most_bad_placed_pos) if max_bad_placed_pos is not None else most_bad_placed_pos
            )


    return sub_plus_1_or_0(max_bad_placed_pos, min_bad_placed_pos)


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
        res = solve(n, A)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

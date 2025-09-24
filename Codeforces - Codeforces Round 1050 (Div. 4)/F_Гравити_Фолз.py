# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from pprint import pprint
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int, arrays: list[list[int]]) -> list[int]:
    max_len = max(len(arr) for arr in arrays)
    variations: list[dict[int, list[int]]] = [dict() for _ in range(max_len)]
    # i (index) - is the position of value in lowest row after all changes
    # key in dict (int) -  is the possible value in that cell
    # value in dict (list of ints) - is the possible arrays than can be used to get this value

    for arr_index, arr in enumerate(arrays):
        for i, v in enumerate(arr):
            if v not in variations[i]:
                variations[i][v] = []
            variations[i][v].append(arr_index)

    answer = []
    current_length = 0
    for i, variation in enumerate(variations):
        if current_length > i:
            continue
        minimal = min(variation.keys())
        answer.append(minimal)

        if len(variation[minimal]) == 1:
            chosen_array = variation[minimal][0]
            current_length = len(arrays[chosen_array])
            for j in range(i + 1, current_length):
                answer.append(arrays[chosen_array][j])
        else:  # TODO
            ...

    return answer


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
        arrays = []
        for _ in range(n):
            k, *arr = map(int, input().split())
            arrays.append(list(arr))
        res = solve(n, arrays)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict
from typing import Any


# ----------------  Solution   ---------------- #
def solve(n: int) -> int:
    winners = n
    losers = 0

    answer = 0

    while winners > 1 or losers > 1:
        winners_matches = winners // 2
        winners -= winners_matches
        answer += winners_matches

        losers_matches = losers // 2
        losers -= losers_matches
        losers += winners_matches
        answer += losers_matches

    answer += 1
    return answer

# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        res = solve(n)
        print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

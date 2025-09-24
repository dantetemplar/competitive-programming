# ruff: noqa: F401
from itertools import pairwise


# ----------------  Solution   ---------------- #
def solve(n: int, m: int, AB: list[tuple[int, int]]) -> int:
    total = m

    for (ai, bi), (ai1, bi2) in pairwise([(0, 0)] + AB):
        d = ai1 - ai
        if d % 2 == 0:
            if bi != bi2:
                total -= 1
        else:
            if bi == bi2:
                total -= 1

    return total


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        AB = [tuple(map(int, input().split())) for _ in range(n)]

        res = solve(n, m, AB)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

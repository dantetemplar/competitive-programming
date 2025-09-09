# ----------------  Solution   ---------------- #
def solve(a: int, b: int) -> int:
    if a == b:
        return 0

    if a % b == 0 or b % a == 0:
        return 1

    return 2


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    def input():
        return sys.stdin.readline().strip()

    def print(s, end="\n"):
        return sys.stdout.write(str(s) + end)

    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        res = solve(a, b)
        if isinstance(res, list):  # if list, join with spaces so [1, 2, 3] -> "1 2 3"
            print(" ".join(map(str, res)))
        else:
            print(res)


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

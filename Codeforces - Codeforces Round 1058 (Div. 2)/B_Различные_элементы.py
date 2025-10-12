# ruff: noqa: F401

# ----------------  Solution   ---------------- #
def solve(n: int, B: list[int]) -> list[int]:
    A = [0] * n
    nxt = 1

    for i in range(n):
        D_i = B[0] if i == 0 else B[i] - B[i - 1]
        p = i - D_i
        if p < 0:
            A[i] = nxt
            nxt += 1
        else:
            A[i] = A[p]

    return A


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        B = list(map(int, input().split()))
        res = solve(n, B)
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

# ruff: noqa: F401

# ----------------  Solution   ---------------- #
INF = 10**18


def solve(n: int, A: list[int]) -> int:
    def cost_to_median(i, offset) -> int:
        if i < 2:
            return INF
        M = [A[(i + offset) % n], A[(i - 1 + offset) % n], A[i - 2 + offset]]
        M.sort()
        return M[2] - M[0]

    def calc(offset) -> int:
        dp = [INF] * (n + 2)
        dp[0] = 0
        for i in range(1, n):
            cost_pair = abs(A[(i + offset) % n] - A[(i - 1 + offset) % n]) + dp[i - 1]
            cost_triad = cost_to_median(i, offset) + (dp[i - 2] if i > 1 else 0)

            dp[i + 1] = min(cost_pair, cost_triad)

        return dp[n]

    ans = INF
    for j in range(3):
        ans = min(ans, calc(j))

    return ans


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

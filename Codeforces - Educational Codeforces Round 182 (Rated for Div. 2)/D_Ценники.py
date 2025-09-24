def solve(n, y, C):
    M = max(C) + 1
    prefixes = [0] * (M + 1)
    for c in C:
        prefixes[c] += 1
    for i in range(1, M + 1):
        prefixes[i] += prefixes[i - 1]

    answer = -n * y
    for i in range(2, M + 1):
        current = -n * y
        for j in range(1, M // i + 2):
            matched = prefixes[min(j * i, M)] - prefixes[(j - 1) * i]
            count = prefixes[j] - prefixes[j - 1]
            current += y * min(count, matched) + j * matched
        answer = max(answer, current)
    return answer


def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n, y = map(int, input().split())
        C = list(map(int, input().split()))
        print(solve(n, y, C))


if __name__ == "__main__":
    main()

from collections import Counter


# ----------------  Solution   ---------------- #
def solve(n: int, A: list[int]) -> int:
    cnt = Counter(A)
    items = sorted(cnt.items())  # (length, count)

    ans = 0
    pairs_perim = 0  # сумма длин всех пар * 2 в префиксе
    pairs_edges = 0  # число рёбер из пар в префиксе
    odd1 = 0  # максимальная нечётная длина в префиксе
    odd2 = 0  # вторая по величине нечётная длина

    for L, c in items:
        # добавляем вклад текущей длины в пары
        p = c // 2
        pairs_perim += 2 * L * p
        pairs_edges += 2 * p

        # обновляем топ-2 нечётных длин
        if c % 2 == 1:
            if L >= odd1:
                odd2 = odd1
                odd1 = L
            elif L > odd2:
                odd2 = L

        # кандидаты:
        # 0 одиночных: нужно >=4 рёбер
        if pairs_edges >= 4 and 2 * L < pairs_perim:
            ans = max(ans, pairs_perim)

        # 1 одиночная: нужно >=3 рёбер
        if odd1:
            per1 = pairs_perim + odd1
            if pairs_edges + 1 >= 3 and 2 * L < per1:
                ans = max(ans, per1)

        # 2 одиночных: нужно >=4 рёбер
        if odd2:
            per2 = pairs_perim + odd1 + odd2
            if pairs_edges + 2 >= 4 and 2 * L < per2:
                ans = max(ans, per2)

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

# ruff: noqa: F401

# ----------------  Solution   ---------------- #
def solve(n: int) -> bool:
    if n == 0:
        return True
    s = bin(n)[2:]  # без ведущих нулей
    tz = len(s) - len(s.rstrip("0"))  # число замыкающих нулей
    c = s[:-tz] if tz else s  # удалили все хвостовые нули
    if c != c[::-1]:  # палиндром?
        return False
    # если длина нечётная — средний бит должен быть '0'
    if len(c) % 2 == 1 and c[len(c) // 2] != "0":
        return False
    return True


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        res = solve(n)
        print("YES" if res else "NO")


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases

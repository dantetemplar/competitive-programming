import sys


def step(indices: list[int] | set[int]) -> int:
    one_indexed = [i + 1 for i in indices]
    sys.stdout.write(f"? {len(one_indexed)} {' '.join(map(str, one_indexed))}\n")
    sys.stdout.flush()
    s = sys.stdin.readline().strip()
    return int(s)


def answer(A: list[int]) -> None:
    sys.stdout.write(f"! {' '.join(map(str, A))}\n")
    sys.stdout.flush()


def solve(n: int):
    m = 2 * n
    ans = [0] * m

    prefix = {0}
    for x in range(1, m):
        mad = step(prefix | {x})
        if mad == 0: # no pair
            prefix.add(x)
        else: # something from prefix is paired with x
            ans[x] = mad

    suffix = {2 * n - 1}
    for x in range(2 * n - 2, -1, -1):
        if ans[x] != 0: # half is already answered, skip
            suffix.add(x)
        else:
            mad = step(suffix | {x})
            if mad == 0: # no pair
                suffix.add(x)
            else: # something from suffix is paired with x
                ans[x] = mad

    answer(ans)


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        solve(n)


if __name__ == "__main__":
    main()

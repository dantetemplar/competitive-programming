import sys


def step(indices: list[int] | set[int]) -> int:
    sys.stdout.write(f"? {len(indices)} {' '.join(map(str, indices))}\n")
    sys.stdout.flush()
    s = sys.stdin.readline().strip()
    return int(s)


def answer(A: list[int]) -> None:
    sys.stdout.write(f"! {' '.join(map(str, A))}\n")
    sys.stdout.flush()


def solve(n: int):
    m = 2 * n
    B = {1}
    ans = [0] * (m + 1) # 1-indexed

    for x in range(2, m + 1):
        mad = step(B | {x})
        if mad == 0:  # no pair
            B.add(x)
        else:  # something from B is paired with x
            ans[x] = mad
            # need to find exact pair via binary search
            B_copy = list(B)
            while len(B_copy) > 1:
                mid = len(B_copy) // 2
                q = B_copy[:mid] + [x]
                if len(q) == 2: # already answered
                    break
                if step(q) == mad:
                    B_copy = B_copy[:mid]
                else:
                    B_copy = B_copy[mid:]
            ans[B_copy[0]] = mad
            B.discard(B_copy[0])

    answer(ans[1:])


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        solve(n)


if __name__ == "__main__":
    main()

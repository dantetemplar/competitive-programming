import sys


def solve(n): # Funny, but just Dirichlet's pigeonhole principle
    dist = 0
    cursor = 0
    while True:
        if cursor == 0:
            dist += 1
        print(cursor + 1, (cursor + dist) % n + 1)
        sys.stdout.flush()
        x = int(input())
        if x == 1 or x == -1:
            break
        cursor += 1
        cursor %= n


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        solve(n)


if __name__ == "__main__":
    main()

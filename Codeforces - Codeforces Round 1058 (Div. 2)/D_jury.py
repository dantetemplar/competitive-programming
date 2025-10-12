import subprocess
import sys
from pathlib import Path


class Jury:
    def __init__(self, n: int, A: list[int]):
        self.n = n
        self.A = A
        self.queries = 0
        self.max_queries = 3 * n

    def step(self, k: int, indices: list[int]) -> int:
        """
        Мы определяем MAD (максимальный дубликат) целочисленной последовательности как наибольшее целое число, которое появляется как минимум дважды. В частности, если нет числа, которое появляется как минимум дважды, значение MAD равно 0. Вот некоторые примеры:

        MAD⁡([1,2,1])=1;
        MAD⁡([2,2,3,3])=3;
        MAD⁡([1,2,3,4])=0.
        """
        self.queries += 1
        MAD = 0

        used = set()
        for i in indices:
            a = self.A[i - 1]
            if a in used:
                MAD = max(MAD, a)
            else:
                used.add(a)
        return MAD

    def answer(self, A: list[int]) -> bool:
        return A == self.A


def run_test_case(process: subprocess.Popen, jury: Jury, case_num: int):
    print(f"Test case {case_num}: n={jury.n}, a={' '.join(map(str, jury.A))}")
    process.stdin.write(f"{jury.n}\n")
    process.stdin.flush()

    while True:
        try:
            line = process.stdout.readline()
            if not line:
                break

            line = line.strip()
            if not line:
                continue

            print(f"Solution asks: {line}")

            if line.startswith("?"):
                k, *indices = map(int, line[2:].split())
                result = jury.step(k, indices)
                print(f"Jury responds: {result}")
                process.stdin.write(f"{result}\n")
                process.stdin.flush()
            elif line.startswith("!"):
                A = list(map(int, line[2:].split()))
                result = jury.answer(A)
                print(f"Jury responds: {result}")
                if result:
                    print("\033[92mSolution found answer!\033[0m")
                    return True
                else:  # red
                    print(f"\033[91mSolution is incorrect! {A} != {jury.A}\033[0m")
                    return False

        except ValueError:
            print(f"Invalid query format: {line}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Total queries used: {jury.queries}")


def run_interactive_test():
    path = Path(__file__).parent / "D_Интерактивная_задача_на_MAD.py"
    process = subprocess.Popen(
        [sys.executable, path.absolute()],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    def read_stderr():
        for line in process.stderr:
            if line:
                print(f"\033[93m{line.rstrip()}\033[0m")

    import threading

    threading.Thread(target=read_stderr, daemon=True).start()

    test_cases = [
        Jury(2, [2, 2, 1, 1]),
        Jury(2, [1, 2, 1, 2]),
        Jury(2, [1, 1, 2, 2]),
        Jury(2, [2, 1, 2, 1]),
        Jury(2, [2, 1, 1, 2]),
        Jury(3, [1, 2, 3, 1, 2, 3]),
        Jury(3, [3, 3, 2, 2, 1, 1]),
        Jury(3, [1, 1, 2, 3, 2, 3]),
        Jury(3, [3, 2, 1, 3, 2, 1]),
        Jury(3, [1, 3, 2, 1, 3, 2]),
        Jury(3, [2, 3, 2, 1, 3, 1]),
        Jury(3, [1, 2, 1, 3, 3, 2]),
        Jury(3, [1, 2, 1, 2, 3, 3]),
        Jury(4, [1, 1, 2, 2, 3, 3, 4, 4]),
        Jury(4, [4, 3, 2, 1, 4, 3, 2, 1]),
        Jury(4, [1, 2, 3, 4, 1, 2, 3, 4]),
        Jury(4, [2, 2, 1, 1, 4, 4, 3, 3]),
        Jury(4, [3, 1, 4, 2, 3, 1, 4, 2]),
        Jury(4, [1, 2, 1, 3, 2, 4, 3, 4]),
        Jury(1, [1, 1]),
        Jury(5, [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]),
        Jury(5, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),
        Jury(6, [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]),
    ]

    process.stdin.write(f"{len(test_cases)}\n")
    process.stdin.flush()

    results = []
    for i, jury in enumerate(test_cases, 1):
        result = run_test_case(process, jury, i)
        results.append(result)
        print()

    stdout, stderr = process.communicate()
    if stdout:
        print(f"Process stdout: {stdout}")
    if stderr:
        print(f"Process stderr: {stderr}")
    print(f"Process exited with code {process.returncode}")

    print("Failed test cases:")
    for i, (result, jury) in enumerate(zip(results, test_cases), 1):
        pass_queries = jury.queries <= jury.max_queries
        if not results or not pass_queries:
            print(f"\033[91mTest case {i}:")
            print(f"Test case {i} answer is correct: {'✅' if result else '❌'}")
            print(
                f"Queries used: {'✅' if jury.queries <= jury.max_queries else '❌'} {jury.queries} vs {jury.max_queries} "
            )
            print("\033[0m")


if __name__ == "__main__":
    run_interactive_test()

import subprocess
import sys
from pathlib import Path


class BatteryJury:
    """Acts as jury for the battery interactive problem."""

    def __init__(self, n: int, working_batteries: set[int]):
        self.n = n
        self.working = working_batteries
        self.queries = 0
        self.max_queries = (n ** 2) // (len(working_batteries)) + 1

    def test_batteries(self, u: int, v: int) -> int:
        """Test if batteries u and v work together."""
        self.queries += 1
        if self.queries > self.max_queries:
            print(f"Too many queries! Used {self.queries}, limit was {self.max_queries}")
            return -1

        if u in self.working and v in self.working:
            return 1
        return 0


def run_interactive_test():
    """Run the D_Батарейки.py solution with jury simulation."""
    path = Path(__file__).parent / "D_Батарейки.py"
    # Start the solution process
    process = subprocess.Popen(
        [sys.executable, path.absolute()],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    process.stdin.write("2\n")  # t = 2

    # Test case 1: n=3, working batteries {2, 3}
    print("Test case 1: n=3, working batteries {2, 3}")
    jury1 = BatteryJury(3, {2, 3})

    # Send input
    process.stdin.write("3\n")  # n = 3
    process.stdin.flush()

    # Read output and respond
    while True:
        try:
            line = process.stdout.readline()
            if not line:
                break

            line = line.strip()
            if not line:
                continue

            print(f"Solution asks: {line}")

            # Parse the query
            try:
                u, v = map(int, line.split())
                result = jury1.test_batteries(u, v)
                print(f"Jury responds: {result}")
                process.stdin.write(f"{result}\n")
                process.stdin.flush()

                if result == 1:
                    print("Solution found working pair!")
                    break
                elif result == -1:
                    print("Solution exceeded query limit!")
                    break

            except ValueError:
                print(f"Invalid query format: {line}")
                break

        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Total queries used: {jury1.queries}")

    print("Test case 2: n=10, working batteries {1, 4, 6, 9}")
    jury2 = BatteryJury(10, {1, 4, 6, 9})

    process.stdin.write("10\n")  # n = 10
    process.stdin.flush()

    # Read output and respond
    while True:
        try:
            line = process.stdout.readline()
            if not line:
                break

            line = line.strip()
            if not line:
                continue

            print(f"Solution asks: {line}")

            # Parse the query
            try:
                u, v = map(int, line.split())
                result = jury2.test_batteries(u, v)
                print(f"Jury responds: {result}")
                process.stdin.write(f"{result}\n")
                process.stdin.flush()

                if result == 1:
                    print("Solution found working pair!")
                    break
                elif result == -1:
                    print("Solution exceeded query limit!")
                    break

            except ValueError:
                print(f"Invalid query format: {line}")
                break

        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Total queries used: {jury2.queries}")

    # Check if the process exited successfully
    stdout, stderr = process.communicate()
    print(f"Process stdout: {stdout}")
    print(f"Process stderr: {stderr}")
    print(f"Process exited with code {process.returncode}")


if __name__ == "__main__":
    run_interactive_test()

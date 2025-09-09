import io
import sys
import time


# Your custom `out` function
def out(s, end="\n"):
    return sys.stdout.write(str(s) + end)

# Benchmarking function
def benchmark(n=100_000):
    # Redirect stdout to an in-memory buffer
    buffer = io.StringIO()
    sys.stdout = buffer

    # Prepare test data
    string_data = "Hello, world!"
    list_data = list(range(100))

    # --- Benchmark custom `out` with string ---
    start = time.perf_counter()
    for _ in range(n):
        out(string_data)
    end = time.perf_counter()
    out_string_time = end - start

    # --- Benchmark `print` with string ---
    buffer.seek(0)
    buffer.truncate(0)
    start = time.perf_counter()
    for _ in range(n):
        print(string_data, end="\n")
    end = time.perf_counter()
    print_string_time = end - start

    # --- Benchmark custom `out` with list ---
    buffer.seek(0)
    buffer.truncate(0)
    start = time.perf_counter()
    for _ in range(n):
        out(list_data)
    end = time.perf_counter()
    out_list_time = end - start

    # --- Benchmark `print` with list ---
    buffer.seek(0)
    buffer.truncate(0)
    start = time.perf_counter()
    for _ in range(n):
        print(*list_data, end="\n")
    end = time.perf_counter()
    print_list_time = end - start

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Print results
    print(f"Custom out (string): {out_string_time:.6f} seconds")
    print(f"Print (string): {print_string_time:.6f} seconds")
    print(f"Custom out (list): {out_list_time:.6f} seconds")
    print(f"Print (list): {print_list_time:.6f} seconds")

# Run benchmark with smaller n for demo
benchmark(1_000_000)

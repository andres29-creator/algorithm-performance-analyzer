import time
import random
import matplotlib.pyplot as plt

# -----------------------------
# Algorithms
# -----------------------------

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -----------------------------
# Performance Test
# -----------------------------

def measure_time(func, arr):
    start = time.time()
    func(arr)
    return time.time() - start


def run_analysis():
    sizes = [100, 300, 500, 800, 1000]

    bubble_times = []
    merge_times = []

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        bubble_times.append(measure_time(bubble_sort, arr))
        merge_times.append(measure_time(merge_sort, arr))

        print(f"Size {size} done")

    # -----------------------------
    # Print Results
    # -----------------------------

    print("\nRESULTS:")
    for i, size in enumerate(sizes):
        print(f"{size} -> Bubble: {bubble_times[i]:.6f}s | Merge: {merge_times[i]:.6f}s")

    # -----------------------------
    # Graph
    # -----------------------------

    plt.plot(sizes, bubble_times, label="Bubble Sort")
    plt.plot(sizes, merge_times, label="Merge Sort")

    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Algorithm Performance Comparison")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_analysis()
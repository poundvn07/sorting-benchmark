import statistics
import numpy as np
import time
import matplotlib.pyplot as plt

# SORTING ALGORITHMS

"""Quick Sort"""
def quick_sort(arr):
    if isinstance(arr, np.ndarray):
        arr = arr.tolist()
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def quick_sort_helper(arr, first, last):
    if first < last:
        pivot_index = partition(arr, first, last)
        quick_sort_helper(arr, first, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, last)

def partition(arr, first, last):
    pivot_value = median_of_three(arr, first, last)
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1
        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
    arr[first], arr[right_mark] = arr[right_mark], arr[first]
    return right_mark

def median_of_three(arr, first, last):
    mid = (first + last) // 2

    if arr[first] > arr[mid]:
        arr[first], arr[mid] = arr[mid], arr[first]
    if arr[first] > arr[last]:
        arr[first], arr[last] = arr[last], arr[first]
    if arr[mid] > arr[last]:
        arr[mid], arr[last] = arr[last], arr[mid]

    arr[first], arr[mid] = arr[mid], arr[first]

    return arr[first]

"""Heap Sort"""
def heap_sort(arr):
    if isinstance(arr, np.ndarray):
        arr = arr.tolist()

    n = len(arr)

    def heapify(a, n, i):
        largest = i
        l, r = 2*i+1, 2*i+2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, n, 0)
    return arr

"""MergeSort"""
def merge_sort(arr):
    if isinstance(arr, np.ndarray):
        arr = arr.tolist()

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def numpy_sort(arr):
    """NumPy sort"""
    return np.sort(np.array(arr))


# DATASET GENERATION

N = 1_000_000

np.random.seed(42)

datasets = {}

float_asc = np.sort(np.random.uniform(-1e6, 1e6, N)).tolist()
datasets["float_asc"] = float_asc

float_desc = np.sort(np.random.uniform(-1e6, 1e6, N))[::-1].tolist()
datasets["float_desc"] = float_desc

float_rand1 = np.random.uniform(-1e6, 1e6, N).tolist()
datasets["float_rand1"] = float_rand1

float_rand2 = np.random.uniform(-1e6, 1e6, N).tolist()
datasets["float_rand2"] = float_rand2

float_rand3 = np.random.uniform(-1e6, 1e6, N).tolist()
datasets["float_rand3"] = float_rand3

int_rand1 = np.random.randint(-1e6, 1e6, N).tolist()
datasets["int_rand1"] = int_rand1

int_rand2 = np.random.randint(-1e6, 1e6, N).tolist()
datasets["int_rand2"] = int_rand2

int_rand3 = np.random.randint(-1e6, 1e6, N).tolist()
datasets["int_rand3"] = int_rand3

int_rand4 = np.random.randint(-1e6, 1e6, N).tolist()
datasets["int_rand4"] = int_rand4

int_rand5 = np.random.randint(-1e6, 1e6, N).tolist()
datasets["int_rand5"] = int_rand5


print("Datasets generated.")

# BENCHMARK

algorithms = {
    "QuickSort": quick_sort,
    "HeapSort": heap_sort,
    "MergeSort": merge_sort,
    "NumPySort": numpy_sort,
}

results = {}

chart_data = {
    'labels': [(i+1) for i in range(10)],
    'QuickSort': [],
    'HeapSort': [],
    'MergeSort': [],
    'NumPySort': []
}

RUNS = 5

for algo_name, algo_func in algorithms.items():
    results[algo_name] = {}
    print(f"\nRunning {algo_name}")

    for i, (dname, data) in enumerate(datasets.items()):
        print(f"  [{i+1}/10] {dname}:", end=" ", flush=True)

        times = []

        _ = algo_func(data.copy())

        for _ in range(RUNS):
            test_data = data.tolist() if isinstance(data, np.ndarray) else data.copy()

            start = time.perf_counter()
            _ = algo_func(test_data)
            elapsed = time.perf_counter() - start

            times.append(elapsed)

        median_time = statistics.median(times)
        median_ms = round(median_time * 1000, 2)

        results[algo_name][dname] = median_ms
        chart_data[algo_name].append(median_ms)

        print(f"{median_ms} ms")

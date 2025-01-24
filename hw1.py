import timeit
import random
import heapq
from functools import partial

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key 
    return lst

def benchmark_sorting(test_arrays):
    print("\n--- Sorting Benchmark Results ---")
    for size, data in test_arrays.items():
        print(f"\nArray size: {size}")

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        print(f"Insertion sort time: {insertion_time:.6f} seconds")

        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        print(f"Merge sort time: {merge_time:.6f} seconds")

        timsort_time = timeit.timeit(lambda: sorted(data), number=1)
        print(f"Timsort (built-in) time: {timsort_time:.6f} seconds")
        print("-" * 40)

def merge_k_lists(arr):
    return list(heapq.merge(*arr))

def main():
    sizes = [10, 100, 1000, 5000]
    test_arrays = {size: [random.randint(1, 10000) for _ in range(size)] for size in sizes}
    benchmark_sorting(test_arrays)

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()
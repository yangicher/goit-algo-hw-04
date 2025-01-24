import timeit
import random

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

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def benchmark_sorting():
    for size, data in test_arrays.items():
        print(f"Array size: {size}")

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        print(f"Insertion sort time: {insertion_time:.6f} seconds")

        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        print(f"Merge sort time: {merge_time:.6f} seconds")

        timsort_time = timeit.timeit(lambda: sorted(data), number=1)
        print(f"Timsort time: {timsort_time:.6f} seconds")

sizes = [10, 100, 1000, 5000]
test_arrays = {size: [random.randint(1, 10000) for _ in range(size)] for size in sizes}

def main():
    benchmark_sorting()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

def merge_k_lists(arr):
    res = []
    for lst in arr:
        res += merge_sort(lst)
    return merge_sort(res)

if __name__ == "__main__":
    main()
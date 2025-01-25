--- Sorting Benchmark Results ---

Array size: 10
Insertion sort time: 0.000004 seconds
Merge sort time: 0.000010 seconds
Timsort (built-in) time: 0.000001 seconds
----------------------------------------

Array size: 100
Insertion sort time: 0.000080 seconds
Merge sort time: 0.000071 seconds
Timsort (built-in) time: 0.000006 seconds
----------------------------------------

На малих наборах даних три алгоритми працюють ефективно,через те що накладні витрати на рекурсію або складну логіку менші.

Array size: 1000
Insertion sort time: 0.010089 seconds
Merge sort time: 0.000859 seconds
Timsort (built-in) time: 0.000067 seconds
----------------------------------------

На середніх наборах даних Merge Sort і Timsort випереджають Insertion Sort, оскільки час виконання Insertion Sort зростає квадратично.

Array size: 5000
Insertion sort time: 0.262976 seconds
Merge sort time: 0.005412 seconds
Timsort (built-in) time: 0.000418 seconds
----------------------------------------

Array size: 10000
Insertion sort time: 1.101865 seconds
Merge sort time: 0.011359 seconds
Timsort (built-in) time: 0.000821 seconds

При використанні виликих наборів Timsort і Merge Sort працюють ефективно, тоді як Insertion Sort стає занадто повільним через квадратичну складність.

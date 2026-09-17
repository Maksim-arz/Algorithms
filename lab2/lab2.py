import time

arr = [5, 21, 335, 7, 1, 0]
target = 7

def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr_sorted, target):
    low = 0
    counter_bin = 0
    high = len(arr_sorted) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr_sorted[mid]
        if guess == target:
            counter_bin += 1
            return mid, counter_bin
        if guess < target:
            counter_bin += 1
            low = mid + 1
        if guess > target:
            counter_bin += 1
            high = mid - 1
    return -1, counter_bin

def linear_search(arr, target):
    length = len(arr)
    counter_lin = 0
    for i in range(length):
        counter_lin += 1
        if arr[i] == target:
            return i, counter_lin
    return -1, counter_lin

arr_sorted = bubble_sort(arr.copy())
print("Отсортированный массив:", arr_sorted)
print("Цель: ", target)
print("Результат бинарного поиска:", binary_search(arr_sorted, target))
print("Результат линейного поиска:", linear_search(arr, target))

SIZE = 1000000
large_sorted_arr = list(range(SIZE))
large_target = SIZE - 1

start_time = time.perf_counter()
bin_res, bin_ops = binary_search(large_sorted_arr, large_target)
bin_time = time.perf_counter() - start_time

start_time = time.perf_counter()
lin_res, lin_ops = linear_search(large_sorted_arr, large_target)
lin_time = time.perf_counter() - start_time

print(f"\nРазмер массива: {SIZE} элементов")
print(f"Искомый элемент: {large_target}\n")

print(f"Linear Search:\n  Время: {lin_time:.5f} сек\n  Итераций: {lin_ops}")
print(f"Binary Search:\n  Время: {bin_time:.5f} сек\n  Итераций: {bin_ops}")

if bin_time > 0:
    speedup = lin_time / bin_time
    print(f"\nВывод: Binary search быстрее Linear Search в {speedup:.0f} раз")
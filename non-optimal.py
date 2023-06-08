import timeit
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# Menghasilkan array acak dengan panjang n
def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Mengukur waktu eksekusi Bubble Sort
def measure_bubble_sort(n):
    arr = generate_random_array(n)
    bubble_sort_time = timeit.timeit(lambda: bubble_sort(arr), number=1)
    print(f"Bubble Sort: {bubble_sort_time} seconds")

# Mengukur waktu eksekusi Insertion Sort
def measure_insertion_sort(n):
    arr = generate_random_array(n)
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr), number=1)
    print(f"Insertion Sort: {insertion_sort_time} seconds")

# Membandingkan waktu eksekusi Bubble Sort dan Insertion Sort
def compare_sorts(n):
    measure_bubble_sort(n)
    measure_insertion_sort(n)

# Contoh penggunaan
compare_sorts(1000)
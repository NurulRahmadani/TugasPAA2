def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Contoh penggunaan
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Array setelah diurutkan menggunakan Bubble Sort:")
print(sorted_array)
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Contoh penggunaan
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = insertion_sort(array)
print("Array setelah diurutkan menggunakan Insertion Sort:")
print(sorted_array)
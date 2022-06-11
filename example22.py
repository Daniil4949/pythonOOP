def binary_search(arr, low, high, x):
    if low <= high:
        middle = (low + high) // 2
        if x == arr[middle]:
            return middle
        elif x < arr[middle]:
            return binary_search(arr, low, middle - 1, x)
        elif x > arr[middle]:
            return binary_search(arr, middle + 1, high, x)
    else:
        return -1


arr = [4, 5, 6, 7, 8, 10]
print(binary_search(arr, 0, len(arr) - 1, 10))
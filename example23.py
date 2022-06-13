def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if not swapped:
        return


arr = [9, 8, 6, 5, 3, 2, 1]
bubbleSort(arr)
print(arr)









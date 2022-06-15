def quick_sort(array, begin, end):
    right = end
    left = begin
    middle = (left + right) // 2
    while left <= right:
        while array[left] < array[middle]:
            left += 1
        while array[right] > array[middle]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        if left < end:
            quick_sort(array, left, end)
        if begin < right:
            quick_sort(array, begin, right)


arr = [9, 14, 2, -2, 56, 78]
print(quick_sort(arr, 0, len(arr) - 1))
print(arr)
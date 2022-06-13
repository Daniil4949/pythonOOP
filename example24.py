def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j += 1

        array[m], array[i] = array[i], array[m]


array = [9, 7, 6, 4, 33, 2]
sel_sort(array)
print(array)
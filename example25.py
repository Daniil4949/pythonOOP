def digital_root(n):
    result = list(map(int, list(str(n))))
    if sum(result) >= 10:
        return digital_root(sum(result))
    else:
        return sum(result)


print(digital_root(132189))
print(str(3333))


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


def binary_array_to_number(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            result += 2 ** (len(arr) - 1 - i)
    return result


print(binary_array_to_number([ 1, 0, 1]))

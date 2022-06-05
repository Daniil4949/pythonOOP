def order_weight(string):
    string = string.split()
    info = []
    for i in string:
        k = list(i)
        temp = sum(list(map(int, k)))
        l = []
        l.append(temp)
        l.append(i)
        info.append(l)
    result = ''
    info = sorted(info)
    for i in range(len(info)):
        if i != len(info) - 1:
            result += info[i][1]
            result += ' '
        else:
            result += info[i][1]
    return result


print(order_weight(''))

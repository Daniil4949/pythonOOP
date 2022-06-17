# def christmas_tree(n):
#     elements = 2 * n - 1
#     tree = []
#     for i in range(n):
#         temp = [' ' for i in range(elements)]
#         tree.append(temp)
#     middle = elements // 2
#     for i in range(n):
#         for j in range(middle - i, middle + i + 1):
#             tree[i][j] = '*'
#
#     result = ''
#     for i in range(len(tree)):
#         for j in range(len(tree[0])):
#             result += str(tree[i][j])
#         if i != len(tree) - 1:
#             result += '\n'
#
#     return result
    # for i in range(len(tree)):
    #     for j in range(len(tree[0])):
    #         print(tree[i][j], end='')
    #     print('\n')


# result = christmas_tree(5)
# for i in range(len(result)):
#     for j in range(len(result[0])):
#         print(result[i][j], end='')
#     print('\n')

# def christmas_tree(height):
#     WIDTH = height*2 - 1
#     tree = [((2*n - 1)*"*").center(WIDTH) for n in range(1, height + 1)]
#     return "\n".join(tree)

def christmas_tree(height):
    width = height * 2 - 1
    tree = [((2 * n - 1) * '*').center(width) for n in range(1, height + 1)]
    return '\n'.join(tree)


# def rot13(message):
#     result = ''
#     for i in message:
#         result += chr(ord(i) + 13)
#     return result.decode('utf-8')
#
#
# print(rot13("test"))
# print(chr(ord('A') + 13))
#
#
# def rot13(message):
#     result = ''
#     message = list(message)
#     for i in message:
#         result += chr(ord(i) + 13)
#     return result
#
#
# print(rot13('test'))


def direction(facing, turn):
    directions = {'N': 0, 'NW': -45, 'NE':  45,
                 'E':  90, 'S': 180, 'SE':  135,
                 'SW': -135, 'W': -90}
    start_turn = directions[facing]
    result = start_turn + turn
    if result >= 360:
        result -= 360
    elif result == -180:
        result = 180
    for i in directions:
        if directions[i] == result:
            return i


print(direction('S', 180))


print(direction("SE", -45))
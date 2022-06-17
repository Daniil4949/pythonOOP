from random import randint


SPACE = ' '
STRAR = '*'


def toy(line):
    tmp = ''
    index = randint(0, len(line)-1)

    for i in range(len(line)):
        tmp += line[i] if i != index else '*'

    return tmp


def christmas_tree(height):
    rows = height
    spaces = rows-1
    stars = 1

    for i in range(rows):
        print(
            (SPACE*spaces) +
            ((STRAR*stars) if (i % 2) == 0 else toy(STRAR*stars)) +
            (SPACE*spaces)
        )
        stars += 2
        spaces -= 1


christmas_tree(5)
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self.x - self.y)

    def __bool__(self):
        if self. x == 0 and self.y == 0:
            return False
        else:
            return True
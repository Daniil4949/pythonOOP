class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side ** 2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.__side * 4
        return self.__perimeter


r = Square(2)
print(r.area)


class DepartmentIT:

    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(DepartmentIT.GO_DEV)

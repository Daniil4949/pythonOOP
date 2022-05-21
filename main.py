# # class BankAccpount:
# #     def __init__(self, name, balance):
# #         self.name = name
# #         self.__balance = balance
# #
# #     def get_balance(self):
# #         return self.__balance
# #
# #     def set_balance(self, value):
# #         if not isinstance(value, (int, float)):
# #             raise ValueError('Balance must be a number')
# #
# #         self.__balance = value
# #
# #     def delete_balance(self):
# #         del self.__balance
# #
# #     my_balance = property(get_balance, set_balance, delete_balance)
#
# from abc import  ABC, abstractmethod
#
#
# class Figure(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     def __str__(self):
#         return f'Class for figure.'
#
#
# class Square(Figure):
#     def __init__(self, a: float):
#         self.__a = a
#
#     def area(self):
#         return self.__a ** 2
#
#     def set_side(self, value: int):
#         self.__a = value
#
#     def get_side(self):
#         return self.__a
#
#     def del_side(self):
#         del self.__a
#
#     def __str__(self):
#         return super().__str__() + f'Class for Square.'
#
#     side = property(get_side, set_side, del_side)
#
#
# class Rectangle(Figure):
#
#     def __init__(self, a: float, b: float):
#         self.__a = a
#         self.__b = b
#
#     def area(self):
#         return self.__a * self.__b
#
#     def set_side_1(self, a):
#         self.__a = a
#
#     def get_side_1(self):
#         return self.__a
#
#     def set_side_2(self, b):
#         self.__b = b
#
#     def get_side_2(self):
#         return self.__b
#
#     a = property(get_side_1, set_side_1)
#     b = property(get_side_2, set_side_2)
#
#     def __str__(self):
#         return super().__str__() + f'Class for Rectangle.'
#
#     def __bool__(self):
#         if self.__a and self.__b: return True
#         else: return False
#
#
# s = Square(2)
# r = Rectangle(2, 3)
# s.side = 3
# print(s.area())
# print(r.area())

# class Square:
#     def __init__(self, s):
#         self.__side = s
#         self.__area = None
#         self.__perimeter = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             self.__area = self.__side ** 2
#         return self.__area
#
#     @property
#     def perimeter(self):
#         if self.__perimeter is None:
#             self.__perimeter = self.__side * 4
#         return self.__perimeter
#
#
# r = Square(2)
# print(r.area)


class DepartmentIT:

    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(DepartmentIT.GO_DEV)
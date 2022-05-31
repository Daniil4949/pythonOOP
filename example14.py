# from time import perf_counter
#
# class Timer:
#
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         result = self.fn(*args, **kwargs)
#         finish = perf_counter()
#         print(f'Функция отработала за {finish - start} секунд')
#         return result
#
# @Timer
# def fact(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr *= i
#     return pr
#
#
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# print(fact(5))

# class Addition:
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         lst = list(args)
#         sum_result = 0
#         for i in lst:
#             if isinstance(i, (int, float)):
#                 sum_result += i
#         print(f'Сумма переданных значений = {sum_result}')
#
#
# add = Addition()
#
# add(10, 20) # печатает "Сумма переданных значений = 30"
# add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
# add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"


# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def display_info(self):
#         print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')
#
#
# class Bus(Vehicle):
#     pass
#
#
# bus_99 = Bus("Ikarus", 66, 124567)
# bus_99.display_info() #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def is_employee(self):
#         return False
#
#
# class Employee(Person):
#     def is_employee(self):
#         return True
#
#
# emp1 = Person("vasya")
# print(emp1.get_name(), emp1.is_employee())  # vasya False
#
# emp2 = Employee("gena bukin")
# print(emp2.get_name(), emp2.is_employee())  # gena bukin True


class NewInt(int):

    def repeat(self, k=2):
        return int(str(self) * k)

    def to_bin(self):
        return int(bin(self)[2:])


a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

# Кстати, как вы думаете, что вернет данный вызов NewInt() ?
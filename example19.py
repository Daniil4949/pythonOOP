# class MyException(Exception):
#     """This is my first exception"""
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         if self.message:
#             return f'MyException {self.message}'
#         else:
#             return "My exception is empty"
#
#
# raise MyException('Something went wrong', 2, 3)
# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
#
# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')
#
#
# worker_objects = []
# for i in persons:
#     worker = Worker(name=i[0], salary=i[1], gender=i[2], passport=i[3])
#     worker_objects.append(worker)
# for worker in worker_objects:
#     worker.get_info()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee:
#     def __init__(self, name, age, company_name, location):
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# print(emp.personal_data.name)
# print(emp.personal_data.age)
# emp.personal_data.display_person_info()
# print(emp.work.company_name)
# print(emp.work.location)
# emp.work.display_company_info()


# class Stack:
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if self.values:
#             result = self.values[-1]
#             del self.values[-1]
#             return result
#         else:
#             print('Empty Stack')
#
#     def peek(self):
#         if self.values:
#             return self.values[-1]
#         else:
#             print('Empty Stack')
#             return None
#
#     def is_empty(self):
#         return bool(len(self.values) == 0)
#
#     def size(self):
#         return len(self.values)
#
#
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
# print(s.size())  # распечатает 2

# class Building:
#     def __init__(self, n):
#         self.floors = [None for i in range(n)]
#
#     def __setitem__(self, key, value):
#         if 0 <= key < len(self.floors):
#             self.floors[key] = value
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.floors):
#             if self.floors[item]:
#                 return self.floors[item]
#             else:
#                 return None
#
#     def __delitem__(self, key):
#         if 0 <= key < len(self.floors) and self.floors[key]:
#             self.floors[key] = None
#
#
# iron_building = Building(22)  # Создаем здание с 22 этажами
# iron_building[0] = 'Reception'
# iron_building[1] = 'Oscorp Industries'
# iron_building[2] = 'Stark Industries'
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])

class Robot:
    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f"Hello, human! My name is {self.name}")
        else:
            print('У робота нет имени')

    def say_bye(self):
        print(f'See u later alligator')


c3po = Robot()
c3po.say_hello() # печатает У робота нет имени
c3po.set_name('R2D2')
c3po.say_hello() # печатает Hello, human! My name is R2D2
c3po.say_bye() # печатает See u later alligator

r = Robot()
r.set_name('Chappy')
r.say_hello()# печатает Hello, human! My name is Chappy
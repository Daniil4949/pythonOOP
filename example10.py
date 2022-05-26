# class Rectangle:
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b
#
#     @property
#     def area(self):
#         return self.__a * self.__b
#
#
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area)  # 15
# print(r2.area)  # 6


# class Date:
#     def __init__(self, day, month, year):
#         self.__day = str(day)
#         self.__month = str(month)
#         self.__year = str(year)
#
#     def check(self, value: str):
#         if len(value) == 1:
#             value = '0' + value
#         return value
#
#     def check_year(self, value):
#         if 0 < len(value) < 4:
#             while len(value) < 4:
#                 value = '0' + value
#         return value
#
#     @property
#     def date(self):
#         return f'{self.check(self.__day)}/{self.check(self.__month)}/{self.check_year(self.__year)}'
#
#     @property
#     def usa_date(self):
#         return f'{self.check(self.__month)}-{self.check(self.__day)}-{self.check_year(self.__year)}'
#
#
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
#
# print(d1.date) # 05/10/2001
# print(d1.usa_date) # 10-05-2001
# print(d2.date) # 15/03/0999
# print(d2.usa_date) # 03-15-0999


# class Robot:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.population += 1
#         print(f'Робот {self.name} был создан')
#
#     def destroy(self):
#         Robot.population -= 1
#         print(f'Робот {self.name} был уничтожен')
#
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
#
#     @classmethod
#     def how_many(cls):
#         print(f'{cls.population}, вот сколько нас еще осталось')
#
#
# r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
# r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
# Robot.how_many() # печатает "1, вот сколько нас еще осталось"
# r2.destroy() # печатает "Робот R2-D2 был уничтожен"

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        if role in Access.__access_list:
            return True
        else:
            return False

    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            if Access.__check_access(user.role):
                print(f'User {user.name}: success')
            else:
                print('AccessDenied')
        else:
            print('AccessTypeError')


user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError
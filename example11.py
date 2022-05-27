# my_set =['123456','password','123456789','12345','2345678','qwerty','234567','111111','1234567890','123123','abc123','1234','password1','iloveyou','1q2w3e4r','000000','qwerty123','zaq12wsx','Dragon1','sunshine','princess','letmein','654321','monkey','27653','1qaz2wsx','123321','qwertyuiop','superman','asdfghjkl']
#
#
# class Registration:
#     def __init__(self, login, password):
#         self.login = login
#         self.__password = password
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, new_email: str):
#         if new_email.count('@') == 1 and new_email.count('.') >= 1:
#             self.__login = new_email
#         else:
#             if new_email.count('@') < 1:
#                 raise ValueError("Логин должен содержать хотя бы один символ '@'")
#             elif new_email.count('.') < 1:
#                 raise ValueError("Логин должен содержать хотя бы один символ '.'")
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, new_password: str):
#         if isinstance(new_password, str) and 5 <= len(new_password) <= 11 and self.is_include_digit(new_password) and :
#             self.__password = new_password
#
#     @staticmethod
#     def is_include_digit(s: str):
#         s = list(s)
#         for i in s:
#             if i.isdigit() is True:
#                 return True
#         else:
#             return False
#
#     @staticmethod
#     def is_include_all_register(s: str):
#         if s.isalpha():
#             return False
#         elif s.isupper():
#             return False
#         else:
#             return True
#
#     @staticmethod
#


# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         if isinstance(gender, str) and (gender.lower() in ('male', 'female')):
#             self.gender = gender
#         else:
#             print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
#             self.gender = 'male'
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f'Гражданин {self.surname} {self.name}'
#         elif self.gender == 'female':
#             return f'Гражданка {self.surname} {self.name}'
#
#
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"

class Vector:
    def __init__(self, *args):
        values = []
        for i in list(args):
            if isinstance(i, int):
                values.append(i)
        self.values = values

    def __len__(self):
        return len(self.values)

    def __str__(self):
        if len(self) != 0:
            s = 'Вектор('
            lst = sorted(self.values)
            for i in range(len(lst)):
                if i != len(lst) - 1:
                    s += str(lst[i]) + ', '
                else:
                    s += str(lst[i]) + ')'
            return s
        else:
            return 'Пустой вектор'


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"
v3 = Vector([4,5], 'hello', 3, -1.5, 1, 2)
print(v3)
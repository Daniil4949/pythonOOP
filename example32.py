import string
from string import ascii_letters
my_set =['123456','password','123456789','12345','2345678','qwerty','234567','111111','1234567890','123123','abc123','1234','password1','iloveyou','1q2w3e4r','000000','qwerty123','zaq12wsx','Dragon1','sunshine','princess','letmein','654321','monkey','27653','1qaz2wsx','123321','qwertyuiop','superman','asdfghjkl']


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_email: str):
        if new_email.count('@') < 1:
            raise ValueError("Логин должен содержать хотя бы один символ '@'")
        if new_email.count('.') < 1:
            raise ValueError("Логин должен содержать хотя бы один символ '.'")
        else:
            self.__login = new_email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой")
        if 4 > len(new_password) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

        if self.is_include_digit(new_password) is False:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

        if self.is_include_all_register(new_password) is True:
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

        if self.is_include_only_latin(new_password) is False:
            raise ValueError('Пароль должен содержать только латинский алфавит')

        if self.check_password_dictionary(new_password):
            raise ValueError('Ваш пароль содержится в списке самых легких')

        self.__password = new_password

    @staticmethod
    def check_password_dictionary(new_password):
        return new_password in my_set

    @staticmethod
    def is_include_digit(new_password):
        new_password = list(new_password)
        for i in new_password:
            if i.isdigit():
                return True
        return False

    @staticmethod
    def is_include_all_register(new_password):
        return new_password.upper() == new_password.lower()

    @staticmethod
    def is_include_only_latin(new_password):
        fact = False
        for i in new_password:
            if i in string.ascii_letters or i.isdigit():
                fact = True
            else:
                return False
        return fact







# class Registration:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         self.__password = value
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, value):
#         if value.count('@') != 1:
#             raise ValueError("Логин должен содержать один символ '@'")
#         if '.' not in value[value.find('@'):]:
#             raise ValueError("Пароль должен содержать символ '.'")
#         else:
#             self.__login = value



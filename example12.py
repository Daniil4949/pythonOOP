class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    @property
    def area(self):
        return self.a * self.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other


class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other,  int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating

        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating

        else:
            return 'Невозможно выполнить сравнение'


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"

class City:
    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return f'{self.name}'

    def __bool__(self):
        return list(self.name)[-1] not in ('a', 'e', 'o', 'u', 'i')


p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"
class Quadrilateral:
    def __init__(self, *args):
        if len(list(args)) == 1:
            self.width = args[0]
            self.height = args[0]

        elif len(list(args)) == 2:
            self.width = args[0]
            self.height = args[1]

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"


class Building:
    def __init__(self, floors: int):
        self.floors = floors
        self.info = []
        for i in range(self.floors):
            self.info.append(0)

    def __setitem__(self, key, value):
        if 0 <= key < self.floors:
            self.info[key] = value

    def __getitem__(self, item):
        if 0 <= item < self.floors:
            if self.info[item]:
                return self.info[item]
            else:
                return None

    def __delitem__(self, key):
        if 0 <= key < self.floors:
            del self.info[key]


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])


class Counter:

    def __init__(self):
        self.counter = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f'Наш атрибут вызывался {self.counter} раз')
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
        if 5 <= len(new_password) <= 11:
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
            if i in string.ascii_letters:
                fact = True
            else:
                return False
        return fact

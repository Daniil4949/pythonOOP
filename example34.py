# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
#
# except ZeroDivisionError as error:
#     print("Введите корректные значения")
# except ValueError as error:
#     print('Введите корректные значения')
# else:
#     print(f'Результат деления a на b: {c}')


# try:
#     file = open('pentagon_secrets.txt', 'r')
#
# except FileNotFoundError:
#     print("Эх, не судьба тайны пентагона узнать")
# else:
#     print(file.read())

# def func(phrase):
#     try:
#         func(phrase)
#     except RecursionError:
#         print('Кто-то должен остановить это безумие')
#
#
#func("Это рекурсия, детка")
#
# try:
#     string = 'gnbfrn'
#     string()
# except Exception as error:
#     print(error)

# class CustomButton:
#     def __init__(self, text, *args):
#         self.text = text
#         self.args = args
#
#     def config(self, *args):
#         self.args = args
#
#     def click(self):
#         try:
#             self.command()
#         except AttributeError:
#             print('Кнопка не настоена')
#         except TypeError:
#             print('Кнопка сломалась')


class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if isinstance(value, (int, float)) is not True:
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value):
        if not Customer.check_type(value):
            if self.balance > value:
                self.balance -= value
            else:
                raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        if not Customer.check_type(value):
            self.balance += value


bob = Customer('Bob Odenkirk')
#bob.deposit('hello') # TypeError: Банк работает только с числами
bob.deposit(200)
print(bob.balance)  # 200
bob.withdraw(300)  # ValueError: Сумма списания превышает баланс
bob.withdraw(150)
print(bob.balance)  # 50
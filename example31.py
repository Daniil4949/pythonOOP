from collections import defaultdict


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}'


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.balance = self.balance + value

    def payment(self, value):
        if self.balance < value:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.balance = self.balance - value
            return True


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = defaultdict()
        self.__total = 0

    def add(self, product: Product, amount=1):
        if product in self.goods:
            self.goods[product.name] += amount
        else:
            self.goods[product.name] = amount
        self.__total = self.__total + product.price * amount

    def remove(self, product: Product, amount):
        if self.goods[product.name] > amount and self.__total > amount * product.price:
            self.goods[product.name] -= amount
            self.__total -= product.price * amount

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Yor check---\n')
        self.goods = sorted(self.goods)
        for i in range(len(self.goods)):
            print(f'{self.goods[i]} {self.goods[i]} {self.goods[i]} ')
            print()
        print(f'---Total: {self.total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Yor check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20



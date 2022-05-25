# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self, value):
#         if isinstance(value, (int, float)):
#             self.__balance = value
#         else:
#             raise TypeError('Balance is a number!')
#
#     balance = property(get_balance, set_balance)
#
#

# class UserMail:
#
#     def __init__(self, name, mail):
#         self.login = name
#         self.__email = mail
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, new_email):
#         if isinstance(new_email, str)\
#                 and new_email.count('@') == 1 \
#                 and '.' in new_email[new_email.find('@'):]:
#             self.__email = new_email
#         else:
#             print(f'ErrorMail {new_email}')
#
#     email = property(fget=get_email, fset=set_email)
#
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
# k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait

# class Notebook:
#     def __init__(self, *args):
#         self._notes = list(args)
#
#     @property
#     def notes_list(self):
#         res = ''
#         for i in range(len(self._notes)):
#             print(i+1,'.',self._notes[i])
# class Notebook:
#     def __init__(self, lst):
#         self._notes = lst
#
#     @property
#     def notes_list(self):
#         for i, k in enumerate(self._notes):
#             print(f"{i+1}.{k}")


# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
#note.notes_list


# class Money:
#     def __init__(self, d, c):
#         self.dollars = d
#         self.cents = c
#         self.total_cents = self.dollars * 100 + self.cents
#
#     @property
#     def dollars(self):
#         return self.dollars
#
#     @dollars.setter
#     def dollars(self, value):
#         if isinstance(value, int) and value >= 0:
#             self.dollars = value
#             self.total_cents = self.dollars * 100 + self.cents
#         else:
#             print('Error dollars')
#
#     @property
#     def cents(self):
#         return self.cents
#
#     @cents.setter
#     def cents(self, value):
#         if isinstance(value, int) and 0 <= value < 100:
#             self.cents = value
#             self.total_cents = self.dollars * 100 + self.cents
#         else:
#             print('Error cents')
#
#     def __str__(self):
#         return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


class Money:
    def __init__(self, d, c):
        self.total_cents = d*100 + c

    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value*100 + self.cents
        else:
            print('Error dollars')

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = self.dollars * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
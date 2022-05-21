class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print("__add__ was declared.")
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplementedError('This operation is not supported.')

    def __radd__(self, other):
        return self + other


b = BankAccount('Misha', 20)
c = BankAccount('Slava', 23)
print(13 + b)
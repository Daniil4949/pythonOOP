class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance must be a number')

        self.__balance = value

    def delete_balance(self):
        del self.__balance

    my_balance = property(get_balance, set_balance, delete_balance)
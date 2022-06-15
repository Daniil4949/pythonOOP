# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# carrot = Product('carrot', 30)
# print(carrot.name, carrot.price)


class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        else:
            print(f'Прочитали все содержимое файла {self.name}')
            return

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        else:
            print(f'Записали значение {content} в файл {self.name}')


class Trash:
    def __init__(self):
        self.content = []

    @staticmethod
    def add(file: File):
        file.in_trash = True





f1 = File('puppies.jpg')
print(f1.__dict__)  # {'name': 'puppies.jpg', 'in_trash': False, 'is_deleted': False}
f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение hello в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)

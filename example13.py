# class Constructor:
#     def add_atribute(self, value_1, value_2):
#         self.__setattr__(value_1, value_2)
#
#     def display(self):
#         print(self.__dict__)
#
#
# obj1 = Constructor()
# obj1.display() # печатает {}
# obj1.add_atribute('color', 'red')
# obj1.add_atribute('width', 20)
# obj1.display() # печатает {'color': 'red', 'width': 20}
#
# obj2 = Constructor()
# obj2.display() # печатает {}
# obj2.add_atribute('height', 100)
# obj2.display() # печатает {'height': 100}


# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# class Worker:
#
#     def __init__(self, name: str, salary: int, gender: str, passport: int):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')
#
#     @staticmethod
#     def workers(persons: list):
#         worker_object = []
#         for i in persons:
#             worker = Worker(name=i[0], salary=i[1], gender=i[2], passport=i[3])
#             worker_object.append(worker)
#         for worker in worker_object:
#             worker.get_info()
#
#
# bob = Worker('Bob Moore', 330000, 'M', '1635777202')
# bob.get_info() # печатает "Worker Bob Moore; passport-1635777202"
# Worker.workers(persons)


# class UnitedKingdom:
#     @staticmethod
#     def capital():
#         print(f'London is the capital of Great Britain.')
#
#     @staticmethod
#     def language():
#         print('English is the primary language of Great Britain.')
#
#
# class Spain:
#     @staticmethod
#     def capital():
#         print('Madrid is the capital of Spain.')
#
#     @staticmethod
#     def language():
#         print("Spanish is the primary language of Spain.")


class Building:
    def __init__(self, n):
        self.floors = [None for i in range(n)]

    def __setitem__(self, key, value):
        if 0 <= key < len(self.floors):
            self.floors[key] = value
        else:
            raise IndexError

    def __getitem__(self, item):
        if 0 <= item < len(self.floors):
            return self.floors[item]
        else:
            raise IndexError

    def __delitem__(self, key):
        if 0 <= key < len(self.floors):
            del self.floors[key]
        else:
            raise IndexError


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
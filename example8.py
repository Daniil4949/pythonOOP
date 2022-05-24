persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]


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
#Worker.workers(persons)

# class Cat:
#     __shared_attr = {
#         'color': 'black',
#         'breed': 'pers'
#     }
#
#     def __init__(self):
#         self.__dict__ = Cat.__shared_attr
#

# class Student:
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f'Имя: {self.__name}\n'
#               f'Возраст: {self.__age}\n'
#               f'Направление: {self.__branch}')
#
#     def access_private_method(self):
#         self.__display_details()
#
#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()

class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass


maker = PizzaMaker()
maker._make_barbecue()
maker._PizzaMaker__make_pepperoni()
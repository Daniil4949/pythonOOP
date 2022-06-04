# class Student:
#     def __init__(self, name, surname, marks):
#         self.name = name
#         self.surname = surname
#         self.marks = marks
#
#     def __next__(self):
#         if self.index >= len(self.name):
#             raise StopIteration
#         letter = self.name[self.index]
#         self.index += 1
#         return letter
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#
# person1 = Student('Igor', 'Nikolaev', [1, 2, 3, 4])
#
# for i in person1:
#     print(i, end=' ')

class PowerTwo:
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self.index
        self.index += 10
        return number


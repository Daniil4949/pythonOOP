# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.a == other.a and self.b == other.b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area < other.area
#         elif isinstance(other, (int, float)):
#             return self.area < other
#
#     def __le__(self, other):
#         return self == other or self < other


# class ChessPlayer:
#     def __init__(self, name, surname, rating):
#         self.name = name
#         self.surname = surname
#         self.rating = rating
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.rating == other
#         elif isinstance(other, ChessPlayer):
#             return self.rating == other.rating
#         else:
#             return 'Невозможно выполнить сравнение'
#
#     def __gt__(self, other):
#         if isinstance(other,  int):
#             return self.rating > other
#         elif isinstance(other, ChessPlayer):
#             return self.rating > other.rating
#
#         else:
#             return 'Невозможно выполнить сравнение'
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.rating < other
#         elif isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#
#         else:
#             return 'Невозможно выполнить сравнение'
#
#
# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000) # False
# print(ian == 2789) # True
# print(magnus == ian) # False
# print(magnus > ian) # True
# print(magnus < ian) # False
# print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"

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
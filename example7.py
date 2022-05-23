# class Person:
#     pass
#
# class Doctor(Person):
#
#     def sleep(self):
#
#         print('Доктор спит')
# class Counter:
#     def start_from(self, value=0):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def display(self):
#         print(self.value)
#
#     def reset(self):
#         self.value = 0
#
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance(self, other):
#         if isinstance(other, Point):
#             return ((other.x - self.x)**2 + (other.y-self.y)**2)**0.5
#         else:
#             print('Передана не точка')
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
#     def description(self):
#         return(f'{self.name} is {self.age} years old')

# jack = Dog("Jack", 4)
#
# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'

# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, value=1):
#         self.goals += value
#
#     def make_assist(self, value=1):
#         self.assists += value
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} -  голы: {self.goals}, передачи: {self.assists}')
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"

class Zebra:
    def __init__(self):
        self.value = 0

    def which_stripe(self):

        if self.value % 2 == 0:
            print('Полоска белая')
        else:
            print('Полоска черная')
        self.value += 1


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"

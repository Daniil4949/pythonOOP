# class Doctor:
#     def can_cure(self):
#         print('Я могу лечить, я доктор')
#
#
# class Builder:
#     def can_biuld(self):
#         print('Я строитель, я могу строить')
#
#
# class Person(Builder, Doctor):
#     pass
#
#
# s = Person()
# s.can_biuld()
# s.can_cure()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee(Person, Company):
#     def __init__(self, name, age, company_name, location):
#         super().__init__(name, age)
#         Company.__init__(self, company_name, location)


# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# emp.display_person_info()
# emp.display_company_info()


class First(object):
    def __init__(self):
        print("First(): entering")
        super(First, self).__init__()
        print("First(): exiting")


class Second(object):
    def __init__(self):
        print("Second(): entering")
        super(Second, self).__init__()
        print("Second(): exiting")


class Third(First, Second):
    def __init__(self):
        print("Third(): entering")
        super(Third, self).__init__()
        print("Third(): exiting")


Third()

print(Third.__mro__)
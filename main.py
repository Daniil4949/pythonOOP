# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __add__(self, other):
#         print("__add__ was declared.")
#         if isinstance(other, BankAccount):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         raise NotImplementedError('This operation is not supported.')
#
#     def __radd__(self, other):
#         return self + other
#
#
# b = BankAccount('Misha', 20)
# c = BankAccount('Slava', 23)
# print(13 + b)


# def tribonacci(signature: list, n: int):
#     if n in (1, 2, 3):
#         return signature[0:n]
#     elif n == 0:
#         return []
#     else:
#         result = signature
#         for i in range(n - 3):
#             result.append(signature[i] + signature[i+1] + signature[i+2])
#         return result


# def tribonacci(signature, n):
#     res = signature[:n]
#     for i in range(n-3): res.append(sum(res[-3:]))
#     return res
import math


# def find_next_square(sq):
#     if sq**0.5 == int(sq**0.5):
#         return int((pow(sq, 0.5) + 1) ** 2)
#     else:
#         return -1

# def is_prime(a):
#     k = 0
#     for i in range(2, a // 2+1):
#         if (a % i == 0):
#             k += 1
#     if a < 2 : return False
#     elif (k <= 0): return True
#     else: return False

# import sympy
# def is_prime(x):
#     return sympy.isprime(x)
# print(sympy.isprime(4))
# #print(find_next_square(121))


import string
# import re
#
#
# def is_pangram(s):
#     pattern = r'[a-z]'
#     s = s.lower()
#     temp = []
#     for item in s:
#         if re.search(pattern, item):
#             temp.append(item)
#     temp = set(temp)
#     temp = list(temp)
#     sorted_chars = sorted(temp)
#     sorted_str = ''.join(sorted_chars)
#     if len(sorted_str) == 26: return True
#     else: return False

#print(is_pangram('The quick, brown fox jumps over the lazy dog!'))


# def find_short(s):
#     result = list(map(len, s.split()))
#     return min(result)
#
#
# print(find_short('bitcoin take over the world maybe who knows perhaps'))
#

# def dublicate_encode(word: str) -> str:
#     result = ''
#     word = word.lower()
#     for i in range(len(list(word))):
#         if word.count(word[i]) == 1:
#             result += '('
#         else:
#             result += ')'
#     return result
#
#
# print(dublicate_encode('(( @'))

# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
#
#
# phil = Student("Phil", 2, 2, 1)
# cam = Student("Cameron", 2, 2, 0)
# geoff = Student("Geoff", 0, 3, 0)
#
#
# def most_money(students):
#     money = []
#     for student in students:
#         value = student.fives * 5 + student.tens * 10 + student.twenties * 20
#         money.append(value)
#     max_money = max(money)
#     result = ''
#     for i in range(len(students)):
#         if max_money == students[i].fives * 5 + students[i].tens * 10 + students[i].twenties * 20:
#             result = students[i].name
#     if len(set(money)) == 1 and len(money) != 1:
#         return 'all'
#     else:
#         return result
#
#
# print(most_money([geoff]))


# def create_phone_number(n: list):
#     result = '('
#     result += str(n[0]) + str(n[1]) + str(n[2]) + ')' + ' ' + str(n[3]) + str(n[4]) + str(n[5]) + '-' + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
#     return result

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
#
#
# print(create_phone_number([1, 1, 1, 1, 2, 1, 1, 1, 1, 1]))

def sum_of_differences(arr: list) -> int:
    arr.sort(reverse=True)
    result = 0
    for i in range(len(arr) - 1):
        result += (arr[i] - arr[i+1])
    return result


print(sum_of_differences([1, 2, 10]))
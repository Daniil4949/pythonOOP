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

def dublicate_encode(word: str) -> str:
    result = ''
    word = word.lower()
    for i in range(len(list(word))):
        if word.count(word[i]) == 1:
            result += '('
        else:
            result += ')'
    return result


print(dublicate_encode('(( @'))
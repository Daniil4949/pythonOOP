# from time import perf_counter
#
# class Timer:
#
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         result = self.fn(*args, **kwargs)
#         finish = perf_counter()
#         print(f'Функция отработала за {finish - start} секунд')
#         return result
#
# @Timer
# def fact(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr *= i
#     return pr
#
#
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# print(fact(5))

class Addition:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        lst = list(args)
        sum_result = 0
        for i in lst:
            if isinstance(i, (int, float)):
                sum_result += i
        print(f'Сумма переданных значений = {sum_result}')


add = Addition()

add(10, 20) # печатает "Сумма переданных значений = 30"
add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"
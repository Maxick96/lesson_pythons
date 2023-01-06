"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""

def my_func(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    print(res)

my_func(400, 200, 300)
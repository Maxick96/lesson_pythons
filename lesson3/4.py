"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(chislo1, chislo2):
    try:
        if chislo2 < 0:
            return chislo1 ** chislo2
        else:
            print('Vy ne vveli vtoroe otricatelnoe chislo! ')
    except TypeError:
        print('Vvodite tolko chisla! ')


print(my_func(5, -1))

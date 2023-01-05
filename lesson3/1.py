"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль i vvoda tolko chisel.
"""

def delenie(chislo1, chislo2):
    try:
        return chislo1 / chislo2
    except ZeroDivisionError:
        return 'Na nol delit nelizya'

try:
    ch1 = int(input('Vvedite pervoe chislo - '))
    ch2 = int(input('Vvedite vtoroe chislo - '))
    print(delenie(ch1, ch2))
except ValueError:
    print('Vvodite tolko chisla! ')
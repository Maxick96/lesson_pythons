"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

generator = [el for el in range(100, 1001, 2)]
print(generator)

print(reduce(lambda item, item2: item * item2, generator))
"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

spisok = [1, 5, 10, 9, 8, 11, 100, 0, 3, 1]
spisok2 = [spisok[el] for el in range(
    1, len(spisok)) if spisok[el] > spisok[el -1]]
print(spisok2)
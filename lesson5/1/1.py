"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

my_f = open('1.txt', 'w+', encoding='utf-8')
lines = []
while True:
    line = input('Vvedite dannye ili nazhmite ENTER dlya zaversheniya! ')
    if line != '':
        lines.append(line + '\n')
    else:
        break
my_f.writelines(lines)
my_f.close()
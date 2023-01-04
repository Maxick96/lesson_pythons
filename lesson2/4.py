"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""
i = 0
stroka = input('Vvedite elementy cherez probel: ').split(' ')
for el in stroka:
    if len(el) > 10:
        print(f' {i} element - {el[:10]}')
    else:
        print(f' {i} element - {el}')
    i += 1
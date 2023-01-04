"""
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func()
"""

def int_func(word):
    return word.title()

def title_func(word):
    word_up = []
    words = word.split()
    for i in words:
        word_up.append(int_func(i))
    print(*word_up)

title_func('show must go on')
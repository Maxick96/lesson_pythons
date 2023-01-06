"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dict = {'One': 'Odin', 'Two': 'Dva', 'Three': 'tri', 'Four': 'chetyre'}

with open('4_old.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dict.keys():
            line = line.replace(key, dict[key])
        print(line)
        with open('4_new.txt', 'a') as f_rus:
            f_rus.write(f'\n {line}')
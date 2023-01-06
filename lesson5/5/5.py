"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
res = 0

with open('5.txt', 'w', encoding='utf-8') as f_obj:
    mas = input('Vvedite chisla cherez probel - ')
    f_obj.write(f'{mas}')

with open('5.txt', encoding='utf-8') as f_obj:
    content = f_obj.read().split(' ')
    for n in content:
        res = res + int(n)
    print(f'Summa = {res}')

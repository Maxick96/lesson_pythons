"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

count_lines = 0
count_words = 1
with open("2.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                count_words += 1
        count_lines += 1
        print(f"Количество слов в строке {count_lines} = {count_words} \n")
        count_words = 1
    print(f"В файле {count_lines} строк(и)")
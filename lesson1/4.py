"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

chislo = int(input("Vvedite polozhitelnoe chislo: "))
max_num = 0
while chislo != 0:
    current_n = chislo % 10
    if max_num < current_n:
        max_num = current_n
    chislo = chislo // 10
print (f"Max cifra: {max_num}")
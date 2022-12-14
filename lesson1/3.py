"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

chislo = int(input("Vvedite polozhitelnoe chislo: "))
summa = chislo + (chislo * 2) + (chislo * 3)
print(f"Summa = {summa} ")
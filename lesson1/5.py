"""
 Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма.
 Например, прибыль — выручка больше издержек,
 или убыток — издержки больше выручки.
 Выведите соответствующее сообщение.
"""

vyruch = int(input("Vvedite zhachenie vyruchki: "))
izderzh = int(input("Vvedite znachenie izderzhki: "))
if vyruch > izderzh:
    print("Pribyl!")
elif vyruch < izderzh:
    print("Ubytok!")
else:
    print("Vyshli v nol!")

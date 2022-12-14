"""
 Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма.
 Например, прибыль — выручка больше издержек,
 или убыток — издержки больше выручки.
 Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки.
 Это отношение прибыли к выручке.
 Далее запросите численность сотрудников фирмы
 и определите прибыль фирмы в расчёте на одного сотрудника.
"""

vyruch = int(input("Vvedite zhachenie vyruchki: "))
izderzh = int(input("Vvedite znachenie izderzhki: "))
prof = vyruch - izderzh
if prof > 0:
    people = int(input("Vvedite kol-vo sotrudnkiov: "))
    prof_people = prof / people
    ren = (prof / vyruch) * 0.01
    print(f"Pribyl = {prof}, \nRentabelnost vyruchki = {ren}"
          f"\nPribyl na odnovo sotrudnika = {prof_people}")
elif prof < 0:
    print(f"Ubytok = {prof}")
else:
    print("Vyshli v nol!")
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys
vyr, stavka, premiya, result = sys.argv


def zarplata(vyr_ch, stavka_r, premiya_r, result_r):
    try:
        print(f'Sotrudnik s vyrabotkoi {vyr_ch} chasov, '
              f'so stavkoi {stavka_r} rublei, '
              f'i s premiya {premiya_r} rublei - '
              f'zarabotal - {result_r} rublei')
    except TypeError:
        print('Vvedite tolko chisla! ')
        exit()

zarplata(vyr, stavka, premiya, result)
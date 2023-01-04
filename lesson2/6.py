"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:

[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Нужно собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

tovary = []
while True:
    tovary.append((int(input('Vvedite nomer tovara - ')),
                   {"Nazvanie ": input('Nazvanie - '),
                    "Coin ": int(input('Coin - ')),
                    "Kolvo ": int(input('Kolvo - ')),
                    "Edinitsa ": input('Edinitsa - ')
                    }))
    check = input('Vvedite 1 dlya vvoda new tovar - vvedite 2 dlya vykhoda - ')
    if check == '2':
        print(tovary)
        break

tovary1 = [
    (1, {'Nazvanie': 'Computer', 'Coin': 20000, 'Kolichestvo': 5, 'Ed': 'sht'}),
    (2, {'Nazvanie': 'Printer', 'Coin': 6000, 'Kolichestvo': 2, 'Ed': 'sht'}),
    (3, {'Nazvanie': 'Scanner', 'Coin': 2000, 'Kolichestvo': 7, 'Ed': 'sht'})
]
nazvanie_list = []
coin_list = []
kolichetvo_list = []
ed_list = []
result_list = {}

for i in range(len(tovary1)):
    nazvanie_list.append(tovary1[i][1]['Nazvanie'])
    coin_list.append(tovary1[i][1]['Coin'])
    kolichetvo_list.append(tovary1[i][1]['Kolichestvo'])
    ed_list.append(tovary1[i][1]['Ed'])

result_list.update({'Nazvanie': nazvanie_list,
                    'Coin': coin_list,
                    'Kolichestvo': kolichetvo_list,
                    'Ed': ed_list})
print(result_list)
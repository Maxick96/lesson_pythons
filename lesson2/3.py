"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dic
"""

month_list1 = ['Winter', 'Winter', 'Spring', 'Spring',
               'Spring', 'Summer', 'Summer', 'Summer',
               'Autumn', 'Autumn', 'Autumn', 'Winter']
month_list2 = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring',
               5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
               9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

month1 = int(input('Vvedite month v vide chisla: '))

print(f'Reshenie cherez spisok - {month_list1[month1-1]}')
print(f'Reshenie cherez spisok - {month_list2.get(month1)}')

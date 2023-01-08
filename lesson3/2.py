"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""

def func_dannye (name, surname, year, city, email, phonenumber):
    print(f'Name - {name}, '
          f'Surname - {surname},'
          f'year - {year},'
          f'city - {city},'
          f'email - {email},'
          f'phonenumber - {phonenumber}')

func_dannye('Maxim', 'Fursov', 1978, 'Moscow', 'maxick.95@mail.ru', 89773438888)
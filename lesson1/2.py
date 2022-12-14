"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
seconds = int(input("Vvedite vremya v secundah: "))

hours = seconds / 3600;
minutes = seconds / 60;

print (f"Vremya: - {hours:.2f}h: {minutes:.2f}m: {seconds:.0f}s")
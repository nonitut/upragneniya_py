# Задание 6: Функция с аргументами по умолчанию
# Напишите функцию power(base, exponent=2), которая принимает два аргумента: base и exponent 
# Если exponent не указан, он должен принимать значение 2
# Функция должна возвращать base в степени exponent

def power(base, exponent=2):
    return base ** exponent

# Пример вызова:
print(power(3))    # Вывод: 9 (3 в квадрате)
print(power(3, 3)) # Вывод: 27 (3 в кубе)

# ✅ Оператор ** (возведение в степень) — встроенная операция Python
# ✅ Аргументы по умолчанию — если exponent не указан, используется 2
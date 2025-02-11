# Задание 4: Функция с циклом
# Напишите функцию print_multiples(n, count), которая принимает два аргумента: 
# число n и количество count. Функция должна выводить первые count кратных n.

def print_multiples(n, count):  
    for i in range(1, count + 1):  
        print(n * i)

print_multiples(3, 5) 


# 1. Цикл for - перебор элементов (чисел от 1 до 5)
print("Цикл for - перебор чисел:")
for i in range(1, 6):
    print(i)

print("Цикл for - умножение числа:")
# 2. Цикл for - умножение числа (вывести первые 5 кратных 3)
for i in range(1, 6):
    print(3 * i)

print("Цикл while - пока условие True:")
# 3. Цикл while - пока условие True (вывести числа от 1 до 5)
i = 1
while i <= 5:
    print(i)
    i += 1  # Увеличиваем i, чтобы цикл не был бесконечным

print("Цикл for с break и continue:")
# 4. Цикл for с break (остановка) и continue (пропуск)
for i in range(1, 10):
    if i == 5:
        break  # Остановит цикл, когда i станет 5
    if i == 3:
        continue  # Пропустит число 3
    print(i)

print("Функция с циклом for:")

# 5. Функция, использующая цикл for (выводит таблицу умножения)
def print_multiples(n, count):
    for i in range(1, count + 1):
        print(n * i)

print_multiples(3, 5)  # Выведет 3, 6, 9, 12, 15


# ✅ Цикл for для перебора чисел
# ✅ Цикл for для умножения
# ✅ Цикл while с условием
# ✅ Цикл for с break и continue
# ✅ Функция print_multiples(), использующая for
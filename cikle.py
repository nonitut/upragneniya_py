# Задание 4: Функция с циклом
# Напишите функцию print_multiples(n, count), которая принимает два аргумента: число n и количество count. Функция должна выводить первые count кратных n.
# Пример вызова:
# print_multiples(3, 5)

def print_multiples(n, count):
    for i in range(1, count + 1):
        print(n * i)

print_multiples(2, 3)

# 2
# 4
# 6

# 🔹 range(start, stop) – это функция, которая создает последовательность чисел.
# 🔹 start = 1, stop = count + 1 → значит, цикл будет идти от 1 до count (включительно)
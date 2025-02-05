n = int(input("Введите число для вычисления факториала: "))

factorial = 1

if n < 0:
    print("Факториал определен только для неотрицательных чисел.")
elif n == 0:
    print(f"Факториал числа 0 равен 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал числа {n} равен {factorial}.")

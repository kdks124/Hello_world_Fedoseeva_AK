n = int(input("Сколько чисел будете вводить? "))
max_value = float(input(f"Введите число №1: "))
i = 2
while i <= n:
    current = float(input(f"Введите число №{i}: "))
    if current > max_value:
        max_value = current
    i = i + 1
print("Максимальное число:", max_value)
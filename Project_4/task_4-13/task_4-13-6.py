n = int(input("Введите число N: "))
summa = 0
i = 1
while i <= n:
    summa = summa + i * i
    i = i + 1
print(f"Сумма квадратов первых {n} чисел: {summa}")
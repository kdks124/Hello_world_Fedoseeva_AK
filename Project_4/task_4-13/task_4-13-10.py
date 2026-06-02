arr = [10, 20, 30, 40, 50]
n = len(arr)
i = 0
summa = 0
while i < n:
    # Проверяем сам индекс i
    if i % 2 != 0:
        summa = summa + arr[i]
    i = i + 1
print("Сумма элементов с нечетными индексами:", summa)
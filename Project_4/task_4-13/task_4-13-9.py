arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
i = 0
summa = 0
while i < n:
    if arr[i] % 2 != 0:
        summa = summa + arr[i]
    i = i + 1
print("Сумма нечетных элементов:", summa)
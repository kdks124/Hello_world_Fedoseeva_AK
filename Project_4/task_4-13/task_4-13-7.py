arr = [10, 20, 30, 40, 50]
n = len(arr)
i = 0
summa = 0
while i < n:
    summa = summa + arr[i]
    i = i + 1
if n > 0:
    srednee = summa / n
    print("Среднее арифметическое:", srednee)
else:
    print("Массив пуст")
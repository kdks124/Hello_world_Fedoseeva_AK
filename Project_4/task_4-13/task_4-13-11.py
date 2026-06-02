arr = [10, 20, 30, 40, 50]
n = len(arr)
i = 0
summa = 0
count = 0
while i < n:
    if i % 2 == 0:
        summa = summa + arr[i]
        count = count + 1
    i = i + 1
if count > 0:
    srednee = summa / count
    print("Среднее арифметическое элементов с четными индексами:", srednee)
else:
    print("Нет элементов с четными индексами")
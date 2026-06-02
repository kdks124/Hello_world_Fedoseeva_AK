arr = [5, -2, 10, -15, 7, 0, 3]
n = len(arr)
i = 0
count = 0
while i < n:
    if arr[i] > 0:
        count = count + 1
    i = i + 1
print("Количество положительных чисел:", count)
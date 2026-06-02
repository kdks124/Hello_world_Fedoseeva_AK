a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
c = float(input("Введите число C: "))
d = float(input("Введите число D: "))

if a <= b and a <= c and a <= d:
    min_value = a
elif b <= a and b <= c and b <= d:
    min_value = b
elif c <= a and c <= b and c <= d:
    min_value = c
else:
    min_value = d
print("Минимальное число:", min_value)
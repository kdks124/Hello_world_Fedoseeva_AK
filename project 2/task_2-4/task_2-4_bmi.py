weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

# Перевод роста из см в метры
height_m = height / 100

# Расчёт ИМТ
bmi = weight / (height_m ** 2)

print("")
print("")

print("--- Отчет о состоянии здоровья ---")
print("")
print(f"Рост:\t\t{height} см")
print(f"Вес:\t\t{weight} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")
#.2f округление до двух знаков после запятой
total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_capacity = int(input("Введите количество капсул в одной упаковке: "))

# Расчёт с использованием // и %
full_packs = total_capsules // pack_capacity
remainder = total_capsules % pack_capacity

# Пустые строки для оформления
print("")
print("")

# Вывод отчёта с использованием \t для отступов
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remainder}")
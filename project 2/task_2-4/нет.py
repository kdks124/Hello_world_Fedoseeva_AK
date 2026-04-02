researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод: ")

# Открываем файл и записываем данные
with open("journal.txt", "w", encoding="utf-8") as file:
    # Верхняя рамка
    file.write("+--------------------------------------------------+\n")
    file.write("| Электронный лабораторный журнал                  |\n")
    file.write("+--------------------------------------------------+\n")

    # Данные исследователя
    file.write(f"| ФИО исследователя : {researcher_name:<30} |\n")
    file.write(f"| Дата             : {experiment_date:<30} |\n")
    file.write(f"| Эксперимент      : {experiment_name:<30} |\n")

    # Разделитель
    file.write("+--------------------------------------------------+\n")

    # Вывод
    file.write(f"| Вывод: {experiment_conclusion:<43} |\n")

    # Нижняя рамка
    file.write("+--------------------------------------------------+\n")

# Сообщение об успехе
print("\nЖурнал успешно сохранён в файл journal.txt!")



V = int(input("нужный объем раствора (в мл): "))
solb = round(V * 0.009, 2)
voda = round(V + solb, 2)
kal = "-" * 23
with open("recipe2.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write(f"{kal}\n")
    file.write(f"Общий объем: {voda} мл\nМасса соли: {solb} г\nОбъем воды: {voda} мл")
donor_blood = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient_blood = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor_blood == recipient_blood:
    print("Переливание ВОЗМОЖНО: группы крови совпадают.")
elif donor_blood == "I":
    print("Переливание ВОЗМОЖНО: донор имеет универсальную группу I (O).")
else:
    print("Переливание НЕВОЗМОЖНО: группы крови несовместимы.")


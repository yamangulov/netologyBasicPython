year=int(input("Ввведите год:"))
if (year - 2020) % 4 == 0:
    print("Високосный год")
else:
    print("Обычный год")
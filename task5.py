number = int(input("Введите 6-значное число: "))
if len(str(number)) != 6:
    print("Число должно быть 6-значным!!!")
    exit()
str_number = str(number)
if ((int(str_number[0]) + int(str_number[1]) + int(str_number[2]))
        == (int(str_number[3]) + int(str_number[4]) + int(str_number[5]))):
    print("Счастливый билет")
else:
    print("Несчастливый билет")

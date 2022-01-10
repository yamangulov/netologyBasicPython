width = int(input("Введите ширину товара в см:"))
length = int(input("Введите длину товара в см:"))
height = int(input("Введите высоту товара в см:"))

if width <= 15 and length <= 15 and height <= 15:
    print("Коробка №1")
elif length > 200:
    print("Упаковка для лыж")
elif 15 < width < 50 or 15 < length < 50 or 15 < height < 50:
    print("Коробка №2")
else:
    print("Стандартная коробка №3")
import math

fig = int(input("Для вычисления площади круга введите 1, для треугольника - 2, для прямоугольника - 3: "))

if fig == 1:
    print("Круг")
    r = float(input("Введите радиус круга: "))
    s = math.pi * r * r / 2
    print("Площадь круга: ", s)
elif fig == 2:
    print("Треугольник")
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    c = float(input("Введите длину стороны C: "))
    if a == b + c or a + b == c or a + c == b:
        print("Треугольник с такими сторонами вырождается в отрезок, его площадь равна 0")
        exit()
    elif a > b + c or c > a + b or b > a + c:
        print("Треугольник с такими сторонами на может существовать!!!")
        exit()
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь треугольника: ", s)
elif fig == 3:
    print("Прямоугольник")
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    s = a * b
    print("Площадь прямоугольника: ", s)
else:
    print("Неизвестный тип фигуры!!!")
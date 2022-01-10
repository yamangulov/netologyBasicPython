numbers = []

while 1:
    number = int(input("Введите число: "))
    if number != 0:
        numbers.append(number)
    else:
        break

summer = 0
for number in numbers:
    summer += number

print("Результат: ")
print(summer)

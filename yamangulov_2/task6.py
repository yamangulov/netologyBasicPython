numbers = input("Введите числа:")

list_numbers = numbers.split(" ")
uniq_numbers = []
counts = []

for number in list_numbers:
    if number in uniq_numbers:
        counts[uniq_numbers.index(number)] = counts[uniq_numbers.index(number)] + 1
    else:
        uniq_numbers.append(number)
        counts.append(1)

result = []

for number in uniq_numbers:
    if counts[uniq_numbers.index(number)] > 1:
        result.append(number)

result.sort()
str_result = " ".join(result)
print("Результат:")
print(str_result)
# my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

for i in reversed(range(len(my_list))):
    if i != 0:
        el = {my_list[i - 1]: my_list[i]}
        my_list.remove(my_list[i])
        my_list.remove(my_list[i - 1])
        my_list.append(el)

result = my_list[0]

print(result)

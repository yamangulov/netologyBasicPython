queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт'
]

queries_by_quantity = {}

for query in queries:
    query_len = len(query.split(' '))
    if query_len in queries_by_quantity.keys():
        queries_by_quantity[query_len] += 1
    else:
        queries_by_quantity[query_len] = 1

words_1 = int(input("Введите кол-во слов в первом запросе: "))
words_2 = int(input("Введите кол-во слов во втором запросе: "))

counter_1 = queries_by_quantity[words_1]
counter_2 = queries_by_quantity[words_2]

percentage_1 = round((counter_1 / len(queries)) * 100, 2)
percentage_2 = round((counter_2 / len(queries)) * 100, 2)

print('Поисковых запросов, содержащих ', words_1, ' слов(а):', percentage_1, '%')
print('Поисковых запросов, содержащих ', words_2, ' слов(а):', percentage_2, '%')


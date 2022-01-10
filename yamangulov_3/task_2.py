queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт'
]

lens = [len(query.split(' ')) for query in queries]

counter_2 = 0
counter_3 = 0

for n in lens:
    if n == 2:
        counter_2 += 1
    else:
        counter_3 += 1

percentage_2 = round((counter_2 / (counter_2 + counter_3)) * 100, 2)
percentage_3 = 100 - percentage_2

print('Поисковых запросов, содержащих 2 слов(а):', percentage_2, '%')
print('Поисковых запросов, содержащих 3 слов(а):', percentage_3, '%')


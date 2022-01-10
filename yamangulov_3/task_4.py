stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

key_max_sales = ''
value_max_sales = 0

for key, value in stats.items():
    if value > value_max_sales:
        key_max_sales = key
        value_max_sales = value

print('Максимальный объем продаж на рекламном канале: ', key_max_sales)

print('Максимальный объем продаж на рекламном канале, при помощи функции max(): ', max(stats, key=stats.get))
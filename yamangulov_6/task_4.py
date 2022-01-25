DEFAULT_USER_COUNT = 3

def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    # при втором вызове функции print(delete_and_return_last_user(1)) она пытается вернуть
    # значение из списка default_list[1], в то время как в списке остался уже только один элемент с индексом 0
    # ошибка list index out of range означает, что мы вышли за пределы списка и ищем не существующий элемент
    return default_list[DEFAULT_USER_COUNT-2]

print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))
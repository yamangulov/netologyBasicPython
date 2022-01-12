documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}


def current_docs():
    print('Текущий список документов:')
    for document in documents:
        shelf = [key for (key, value) in directories.items() if document['number'] in value][0]
        print(
            f'№: {document["number"]}, тип: {document["type"]}, владелец: {document["name"]}, полка хранения: {shelf}')

def current_shelves():
    print(f'Текущий перечень полок: {", ".join(directories.keys())}.')


while 1:
    command = input('Введите команду: ')
    if command == 'p' or command == 's' or command == 'ad' or command == 'd' or command == 'm':
        number = input('Введите номер документа: ')
        doc = [document for document in documents if document['number'] == number]
        if command == 'p' and doc:
            name = [document['name'] for document in documents if document['number'] == number][0]
            print('Владелец документа: ', name)
        elif command == 'p':
            print('Документ не найден в базе')
        elif command == 's' and doc:
            shelf = [key for (key, value) in directories.items() if number in value][0]
            print('Документ хранится на полке: ', shelf)
        elif command == 's':
            print('Документ не найден в базе')
        elif command == 'ad' and doc:
            print('Документ с таким номером уже существует в базе')
        elif command == 'ad':
            type = input('Введите тип документа: ')
            name = input('Введите владельца документа: ')
            shelf = input('Введите полку для хранения: ')
            if shelf not in directories.keys():
                print('Такой полки не существует. Добавьте полку командой as.')
            else:
                documents.append({'type': type, 'number': number, 'name': name})
                directories[shelf].append(number)
                print('Документ добавлен.', end='')
            current_docs()
        elif command == 'd' and doc:
            shelf = [key for (key, value) in directories.items() if number in value][0]
            del documents[documents.index(doc[0])]
            del directories[shelf][directories[shelf].index(number)]
            print('Документ удален.')
            current_docs()
        elif command == 'd':
            print('Документ не найден в базе.')
            current_docs()
        elif command == 'm' and doc:
            new_shelf = input('Введите номер полки: ')
            if new_shelf in directories.keys():
                shelf = [key for (key, value) in directories.items() if number in value][0]
                del directories[shelf][directories[shelf].index(number)]
                directories[new_shelf].append(number)
                print('Документ перемещен.')
                current_docs()
            else:
                print('Такой полки не существует. ', end='')
                current_shelves()
        elif command == 'm':
            print('Документ не найден в базе.')
            current_docs()
    elif command == 'l':
            current_docs()
    elif command == 'ads' or command == 'ds':
        shelf = input('Введите номер полки: ')
        if command == 'ads' and shelf in directories.keys():
            print('Такая полка уже существует. ', end='')
            current_shelves()
        elif command == 'ads':
            directories[shelf] = []
            print('Полка добавлена. ', end='')
            current_shelves()
        elif command == 'ds' and shelf not in directories.keys():
            # эту ветка не предполагалась, но напрашивается
            print('Такой полки уже не существует. ', end='')
            current_shelves()
        elif command == 'ds' and directories[shelf]:
            print('На полке есть документы, удалите их перед удалением полки. ', end='')
            current_shelves()
        elif command == 'ds':
            del directories[shelf]
            print('Полка удалена. ', end='')
            current_shelves()
    elif command == 'q':
        print('Работа с программой завершена!')
        break
    else:
        # эту ветка не предполагалась, но напрашивается
        print('Введен неизвестный тип команды!')

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


def current_docs(documents, directories):
    print('Текущий список документов:')
    for document in documents:
        shelf = [key for (key, value) in directories.items() if document['number'] in value][0]
        print(
            f'№: {document["number"]}, тип: {document["type"]}, владелец: {document["name"]}, полка хранения: {shelf}')

def current_shelves(directories):
    print(f'Текущий перечень полок: {", ".join(directories.keys())}.')


def find_doc_by_number(documents, number):
    return [document for document in documents if document['number'] == number]


def find_doc_name_by_number(documents, number):
    return [document['name'] for document in documents if document['number'] == number][0]


def find_shelf_by_number(directories, number):
    return [key for (key, value) in directories.items() if number in value][0]


def clear_shelf_from_doc_number(directories, shelf, number):
    del directories[shelf][directories[shelf].index(number)]


def clear_doc_from_documents(documents, doc):
    del documents[documents.index(doc[0])]


def add_doc_to_dir_by_number(directories, shelf, number):
    directories[shelf].append(number)


def documents_operate(documents, directories):
    while 1:
        command = input('Введите команду: ')
        if command == 'p' or command == 's' or command == 'ad' or command == 'd' or command == 'm':
            number = input('Введите номер документа: ')
            doc = find_doc_by_number(documents, number)
            if command == 'p' and doc:
                name = find_doc_name_by_number(documents, number)
                print('Владелец документа: ', name)
            elif command == 'p':
                print('Документ не найден в базе')
            elif command == 's' and doc:
                shelf = find_shelf_by_number(directories, number)
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
                    add_doc_to_dir_by_number(directories, shelf, number)
                    print('Документ добавлен.', end='')
                current_docs(documents, directories)
            elif command == 'd' and doc:
                shelf = find_shelf_by_number(directories, number)
                clear_doc_from_documents(documents, doc)
                clear_shelf_from_doc_number(directories, shelf, number)
                print('Документ удален.')
                current_docs(documents, directories)
            elif command == 'd':
                print('Документ не найден в базе.')
                current_docs(documents, directories)
            elif command == 'm' and doc:
                new_shelf = input('Введите номер полки: ')
                if new_shelf in directories.keys():
                    shelf = find_shelf_by_number(directories, number)
                    clear_shelf_from_doc_number(directories, shelf, number)
                    add_doc_to_dir_by_number(directories, new_shelf, number)
                    print('Документ перемещен.')
                    current_docs(documents, directories)
                else:
                    print('Такой полки не существует. ', end='')
                    current_shelves(directories)
            elif command == 'm':
                print('Документ не найден в базе.')
                current_docs(documents, directories)
        elif command == 'l':
            current_docs(documents, directories)
        elif command == 'ads' or command == 'ds':
            shelf = input('Введите номер полки: ')
            if command == 'ads' and shelf in directories.keys():
                print('Такая полка уже существует. ', end='')
                current_shelves(directories)
            elif command == 'ads':
                directories[shelf] = []
                print('Полка добавлена. ', end='')
                current_shelves(directories)
            elif command == 'ds' and shelf not in directories.keys():
                # эта ветка не предполагалась, но напрашивается
                print('Такой полки уже не существует. ', end='')
                current_shelves(directories)
            elif command == 'ds' and directories[shelf]:
                print('На полке есть документы, удалите их перед удалением полки. ', end='')
                current_shelves(directories)
            elif command == 'ds':
                del directories[shelf]
                print('Полка удалена. ', end='')
                current_shelves(directories)
        elif command == 'q':
            print('Работа с программой завершена!')
            break
        else:
            # эту ветка не предполагалась, но напрашивается
            print('Введен неизвестный тип команды!')


documents_operate(documents, directories)

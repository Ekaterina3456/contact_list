phonebook = []


def open_file(path):
    global phonebook
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phonebook.append({'name': contact[0], 'phone': contact[1]})

def save_file(path):
    global phonebook
    result = []
    for contact in phonebook:
        cont = ';'.join(contact.values())
        result.append(cont)
    result = '\n'.join(result)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(result)

def print_book(book: list):
    for contact in book:
        cont = f'{contact["name"]} {contact["phone"]}'
        print(cont)


def find_contact(word: str):
    global phonebook
    result = []
    for contact in phonebook:
        for field in contact.values():
            if word in field:
                result.append(contact)
    return result

def add_contact(name, phone):
    global phonebook
    phonebook.append({'name': name, 'phone': phone})

def delete_contact(name_to_del):
    global phonebook
    for contact in phonebook:
        for field in contact.values():
            if name_to_del in field:
                phonebook.remove(contact)
    return phonebook

def change_contact(name_to_change):
    global phonebook
    for contact in phonebook:
        for field in contact.values():
            if name_to_change in field:
                print('\t1. Изменить имя\n'
                      '\t2. Изменить номер\n'
                      '\t3. Изменить имя и номер\n')
                choise = int(input('выбирите пункт '))
                match choise:
                    case 1:
                        contact['name'] = input('введите новое имя контакта ')
                    case 2:
                        contact['phone'] = input('введите новый номер контакта ')
                    case 3:
                        contact['name'] = input('введите новое имя контакта ')
                        contact['phone'] = input('введите новый номер контакта ')
    return phonebook

def menu():
    while True:
        print('Главное меню:\n'
              '\t1. Открыть файл\n'
              '\t2. Сохранить файл\n'
              '\t3. Посмотреть все контакты\n'
              '\t4. Найти контакт\n'
              '\t5. Добавить контакт\n'
              '\t6. Удалить контакт\n'
              '\t7. Изменить контакт\n'
              '\t8. Выход\n')
        choice = int(input('выберите пункт меню '))
        match choice:
            case 1:
                open_file('contacts.txt')
            case 2:
                save_file('contacts.txt')
            case 3:
                print_book(phonebook)            
            case 4:
                search = input('введите ключевое слово для поиска ')
                result = find_contact(search)
                print_book(result)            
            case 5:
                name = input('введите имя ')
                phone = input('введите номер ')
                add_contact(name, phone)
            case 6:
                name_to_del = input('введите имя контакта который нужно удалить ')
                delete_contact(name_to_del)
            case 7:
                name_to_change = input('введите имя контакта который нужно изменить ')
                change_contact(name_to_change)
            case 8:
                break


# open_file('contacts.txt')
# print_book(phonebook)

if __name__ == '__main__':
    menu()





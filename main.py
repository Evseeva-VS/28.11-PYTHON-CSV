from csv_csv import file_open, insert, drop_by_arg, find, go_to_next_curs, save

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти',
    '5': 'Перевести на следующий курс',
    '6': 'Вывести совершеннолетних студентов',
    '7': 'Вывести сводку по количеству студентов',
    '8': 'Вывести записи',
    '9': 'Сохранить в файл',
    '0': '<- Меню',
    'exit': 'Выход'
}

# Вывод меню
def showMenu():
    print('\n'.join([f'{key}: {value}' for key, value in MENU.items()]))

showMenu()

while True:
    command = input()
    if command == '1':
        file_open()
    elif command == '2':
        insert(input('ФИО: '), input('Пол: '), int(input('Возраст: ')), input('Телефон: '), input('Почта: '), input('Группа: '), input('Курс: '))
    elif command == '3':
        col = input('Колонка: ')
        val = input('Значение: ')
        drop_by_arg(val, col_name=col)
    elif command == '4':
        col = input('Колонка: ')
        val = input('Значение: ')
        find(val, col_name=col)
    elif command == '5':
        go_to_next_curs()
    elif command == '6':
        print(6)
    elif command == '7':
        print(7)
    elif command == '8':
        print(8)
    elif command == '9':
        save()
    elif command == '0':
        showMenu()
    elif command == 'exit':
        break
    else:
        print('Неверная команда, попробуйте ещё раз', '0: <- Меню', sep='\n')
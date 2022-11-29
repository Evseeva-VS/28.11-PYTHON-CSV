from csv_csv import file_open, insert

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
        print(3)
    elif command == '4':
        print(4)
    elif command == '5':
        print(5)
    elif command == '6':
        print(6)
    elif command == '7':
        print(7)
    elif command == '8':
        print(8)
    elif command == '9':
        print(9)
    elif command == '0':
        showMenu()
    elif command == 'exit':
        break
    else:
        print('Неверная команда, попробуйте ещё раз', '0: <- Меню', sep='\n')
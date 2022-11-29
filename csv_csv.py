import csv

csv_file = []

# Открываем csv файл
def file_open():
    global csv_file
    fileName = input('Название файла (по умолчанию data.csv): ')
    # Если файл не указан - задаём значение по умолчанию
    if (fileName == ''):
        fileName = 'data.csv'
    
    # Если расширение не указано - добавляем расширение
    if (fileName.index('.') == -1):
        fileName += '.csv'

    # Открываем файл
    try:
        with open(fileName, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                csv_file.append(row)
        print('Файл открыт. Записей:', len(csv_file))
    # Если не получилось - выводим сообщение об ошибке
    except:
        print('Файл не получилось открыть!', 'Проверьте наличие файла', sep='\n')

# Добавление данных
def insert(fio, gender, age, tel, email, group, curs):
    global csv_file
    try:
        try:
            mx = max(csv_file, key=lambda x: int(x['ном']))
        except:
            mx = {'ном': 0}
        csv_file.append({'ном': int(mx['ном']) + 1, 'фио': fio, 'пол': gender, 'возраст': age, 'телефон': tel, 'почта': email, 'группа': group, 'курс': curs})
    except Exception as e:
        print('Ошибка при добавленнии новой записи: ', e, sep='\n')
        return
    print('Данные добавлены.')
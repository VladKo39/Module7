''''''
'''
"Позиционирование в файле".
Цель: Закрепить знания о позиционировании в файле, 
использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.

Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), 
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, 
Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')

Файл module_7_2.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''


def custom_write(file_name, strings):
    # принимает аргументы
    # file_name - название файла для записи,
    # strings - список строк для записи.
    # Функция должна:
    # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    # Возвращать словарь strings_positions, где
    # ключом будет кортеж( <номер строки >, < байт начала строки >),а значением - записываемая строка.)

    strings_positions = {}
    # создаем пустой словарь
    file = open(file_name, 'w', encoding='utf-8')
    # открываем файл text.txt для записи (w),с кодировкой utf-8
    for line, string in enumerate(strings, 1):
        # для записи в файл text.txt(file_name) и словарь strings_positions
        # проходим циклом по списку strings(info)
        # line номер строки индекс первой записи 1 , string значение строки, из enumerate(string,1)
        bites = file.tell()
        # tell() возвращает текущую позицию указателя чтения/записи в файле в байтах.
        file.write(f'{string}\n')
        # добавляем строку в text.txt со значением string с последующим переходом на новую строку
        strings_positions[(line, bites)] = string
        # добавляем в словарь strings_positions ключ (номер строки, позиция байты : текущее значение)
        file.close
        # закрываем файл
    return strings_positions
    # возврат словаря


info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
# список значений

result = custom_write('text.txt', info)

for elem in result.items():
    # выбор ключ:значение из словаря
    print(elem)

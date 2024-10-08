''''''
'''
Домашнее задание по теме "Файлы в операционной системе".
Цель задания:

Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
 и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:

Ключевая идея – использование вложенного for

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, 
    Размер: {filesize} байт, 
    Время изменения: {formatted_time}, 
    Родительская директория: {parent_dir}')
Так как в разных операционных системах разная схема расположения папок, 
тестировать проще всего в папке проекта (directory = “.”)
Пример возможного вывода:
Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.

'''
import os

'''импорт бибилиотеки для работы с файлами import os'''
import time

'''импорт библиотеки для работы с форматом времени import time'''

directory = "."
'''задание текущей дирректории, начало локального пути "." '''

for dirpath, dirnames, filenames in os.walk(directory):
    '''os.walk() в цикле проходит от текущего каталога вниз, возвращает кортеж
    dirpath - путь к текущему каталогу
    dirnames -это список имен подкаталогов в dirpath, исключая особые символы '.' и '..'.
    filenames - это список имен файлов в dirpath (не-каталогов).
    '''
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        '''локальный путь к фаилу путь к текущему каталогу \\ имя файла'''
        filetime = os.path.getmtime(filepath)
        '''время изменения файла(локальному путь)'''
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        '''время изменения файла в формате день.месяц.год ч:м'''
        file_size = os.path.getsize(filepath)
        '''размер файла'''
        parent_dir = os.path.dirname(filename)
        '''родительская дирректория '''
        abs_path = os.path.abspath(filename)
        '''Абсолютный путь к фаилу '''
        print(f'Обнаружен файл: {filename}, '
              f'Путь: {filepath}, Размер: {file_size} байт, '
              f'Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}, Абсолютный путь: {abs_path}')

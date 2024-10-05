''''''
'''"Оператор "with".
Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
Задача "Найдёт везде":
Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

Вывод на консоль:
{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки',
 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
{'test_file.txt': 3}
{'test_file.txt': 4}
Файл module_7_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''


class WordsFinder:
    '''Класс WordsFinder'''

    def __init__(self, *file_names):
        ''' Объект класса принимает при создании неограниченного количество
        названий  файлов и записывает их в атрибут file_names в виде списка или кортежа.
        '''
        self.file_names = file_names
        return

    def get_all_words(self):
        '''Метод, который возвращает словарь dict_all_words следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4']}
        Где: ключ - 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
         ['word1', 'word2'], ['word3', 'word4'] - слова содержащиеся в этом файле.'''
        dict_all_words = {}
        # Словарь с файлами и текстом в них
        words = []
        # слова в файле
        punct_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        # символы для удаления

        for name in self.file_names:
            # Проход по списку файлов
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for punct in punct_list:
                        if punct in line:
                            line = line.replace(punct, ' ')

                    line_split = line.strip().split(' ')

                    for line_s in line_split:
                        words.append(line_s)

                dict_all_words[name] = words

        return dict_all_words

    def find(self, word):
        ''' метод, c атрибутом word - искомое слово.
            Возвращает словарь, dict_find:
            ключ - название файла,
            значение - позиция первого такого слова в списке слов этого файла.'''

        word = word.lower()
        dict_find = {}
        for name, words in self.get_all_words().items():
            for w in words:
                nn = words.index(word) + 1
                dict_find[name] = nn
        return dict_find

    def count(self, word):
        ''' метод, c атрибутом word - искомое слово.
                    Возвращает словарь, dict_count:
                    ключ - название файла,
                    значение - количество слов в списке слов этого файла.'''
        word = word.lower()
        dict_count = {}
        for name, words in self.get_all_words().items():
            for w in words:
                nn = words.count(word)
                dict_count[name] = nn
        return dict_count


WF = WordsFinder
finder2 = WF('test_file.txt')
print(finder2.get_all_words())
print(finder2.find("TEXT"))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего



''''''
'''
"Режимы открытия файлов"
Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

Задача "Учёт товаров":
Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине

Как выглядит файл после запусков:
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

Файл module_7_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''
import os
#для проверки наличия product.txt

class Product:
    #Класс Product
    def __init__(self, name: str, weight: float, category: str):
        #метод устанавливаем атрибуты
        self.name = name
        #name название продукта (строка), ддествительно в классе Product
        self.weight = weight
        # общий вес товара (дробное число), дествительно в классе Product
        self.category = category
        # категория продукта (строка), дествительно в классе Product
        return

    def __str__(self):
        # Метод возвращает строку в формате '<название>, <вес>, <категория>'.
        self.article = (f'{self.name}, {str(self.weight)}, {self.category}')
        return self.article


class Shop:
    # Класс Shop
    def __init__(self):
        # метод устанавливаем атрибуты
        self.__file_name = 'product.txt'
        #Инкапсулированный атрибут
    def get_products(self):
        #Метод считывает всю информацию из файла __file_name,
        # возвращает единую строку со всеми товарами из этого файла

        #Проверка на наличие файла product, если нет , то создаем(для первого запуска)
        file_path = os.path.abspath(self.__file_name)
        # Определение пути до текущей диррекиории
        if not os.path.exists(file_path):
            #если фаила нет
            file = open(self.__file_name, 'x')
            #открываем файл в режиме создания(x)
            file.close
            #Закрываем файл

        file = open(self.__file_name, 'r')
        #открываем в режиме редактирования
        self.list_article = file.read()
        #считывание данных единой строкой из файла
        file.close
        # Закрываем файл
        return self.list_article

    def add(self, *products):
        #ринимает неограниченное количество объектов класса Product.
        #Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по артикулу).
        #Если такой продукт уже есть, не добавляетm и выводить строку
        # 'Продукт <название> уже есть в магазине'.

        list_old = self.get_products()
        #строка всего товара из Product.txt
        file_app = open(self.__file_name, 'a')
        #открытие файла product в режиме добавления
        for article in products:
        #Проходим циклом по списку добавленного товара p1,p2,p3
            if list_old.find(f'{article.name}, {article.weight}, {article.category}') == -1:
                #исли данные списка (name,weght,category) не нашлись в строке всеко товара
                file_app.write(f'{article}\n')
                #добавляем в файл
            else:
            #иначе выводим на печать
               print(f'Продукт {article} уже есть в магазине')
        file_app.close()
        #Закрываем файл

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

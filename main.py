'''
1) Вывести "Привет, мир!"
'''
# def print_hi_world():
#     print('Hello, world!')

# print_hi_world()
'''
2) Вывести текущий год
'''
# from datetime import datetime
# def print_current_date():
#     print(f'Сейчас {datetime.now().year} год')

# print_current_date()
'''
3) Вывести список покупок
'''
# shoplist = ["Молоко", "Яйца", "Хлеб", "Яблоки", "Бананы", "Масло", "Сахар"]

# def print_shoplist():
#     for i in shoplist:
#         print(i)

# print_shoplist()
'''
4) Вывести ваше имя
'''
# name = 'Solomon'

# def print_name(s):
#     print(s)

# print_name()
'''
5) Вывести дни недели
'''
# week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# def print_week():
#     for i in week:
#         print(i)

# print_week()
'''
6) Вывести название вашего любимого фильма
'''
# film = input('Введите название вашего любимого фильма: ')

# def fav_film(s):
#     print(s)

# fav_film(film)
'''
7) Вывести предупреждение о низком заряде батареи
'''
# battery = 14

# def low_battery(s):
#     if s < 15:
#         print('Низкий заряд батареи')
#     else:
#         pass

# low_battery(battery)
'''
8) Определение четности чисел в списке
'''
# numbers = [37, 71, 23, 12, 12]

# def count_even_numbers(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count += 1
#         else:
#             pass
#     print(f'В вашем списке {count} четных чисел')

# count_even_numbers(numbers)
'''
9) Подсчет элементов в списке ["яблоко", "банан", "яблоко", "груша", "банан"]
'''
# fruits = ["яблоко", "банан", "яблоко", "груша", "банан"]
# numbers = [37, 71, 23]

# def count_list_elements(list):
#     count = 0
#     for i in list:
#         count += 1
#     print(f'В этом списке {count} элементов')

# count_list_elements(fruits)
# count_list_elements(numbers)
'''
10) Поиск максимального числа в списке
'''
# numbers = [37, 71, 23, 12, 12]

# def max_list_element(list):
#     max_num = 0
#     for i in list:
#         if i > max_num:
#             max_num = i
#     return max_num

# print(max_list_element(numbers))
'''
11) Сумма чисел до N, включая N
'''
# def summa_till_n():
#     N = int((input('Введите целое число: ')))
#     summa = 0
#     for i in range(1, N+1):
#         summa += i
#     return summa

# print(summa_till_n())
'''
12) Задача состоит в том, чтобы написать функцию, которая принимает два списка:
ключи и значения, и затем объединяет их в словарь:
'''
# keys = ["имя", "возраст", "город"]
# values = ["Иван", 25, "Москва"]

# def lists_2_dict(k, v):
#     my_dict = {}
#     for i in range(len(k)):
#         key = k[i]
#         value = v[i]
#         my_dict[key] = value
#     return my_dict

# result = lists_2_dict(keys, values)
# print(result)

'''
Задача 1: Уникальные элементы

Напишите функцию, которая принимает список и возвращает новый список
только с уникальными элементами из исходного списка.
'''
# def delete_similar_elements(a):
#     set_list = set(a)
#     unique = list(set_list)
#     return unique

# my_list = [1, 2, 3, 4, 4, 4, 5, 4, 4]
# print(delete_similar_elements(my_list))

'''
Задача 2: Переводчик с латиницы на кириллицу

Создайте словарь для перевода символов с латиницы на кириллицу.
Напишите функцию, которая принимает строку на латинице и возвращает её перевод
на кириллицу с использованием вашего словаря.
'''
# def latin_cyrillic(text):
#     text = text.lower()
#     my_dict = {
#             'a': 'а',
#             'b': 'б',
#             'c': 'ц',
#             'd': 'д',
#             'e': 'е',
#             'f': 'ф',
#             'g': 'г',
#             'h': 'х',
#             'i': 'и',
#             'j': 'й',
#             'k': 'к',
#             'l': 'л',
#             'm': 'м',
#             'n': 'н',
#             'o': 'о',
#             'p': 'п',
#             'q': 'к',
#             'r': 'р',
#             's': 'с',
#             't': 'т',
#             'u': 'у',
#             'v': 'в',
#             'w': 'в',
#             'x': 'кс',
#             'y': 'й',
#             'z': 'з'
#         }
#     cyrillic = ''
#     for element in text:
#         cyrillic += my_dict.get(element, element)
    
#     return cyrillic

# latin_text = "Sozdavat slovar dolgo"

# print(latin_cyrillic(latin_text))
'''
Задача 3: Объединение списков в кортежи

Напишите функцию, которая принимает два списка одинаковой длины
и возвращает список кортежей, где каждый кортеж состоит из элементов этих списков,
стоящих на одинаковых позициях.
'''
# def zip_two_lists(list_one, list_two):
#     if len(list_one) != len(list_two):
#         print('Списки должны быть одинаковой длины')

#     ziped_list = []
#     for element in range(len(list_one)):
#         ziped_list.append((list_one[element], list_two[element]))
    
#     return ziped_list

# list1 = [1, 2, 3, 4]
# list2 = [4, 3, 2, 1]

# print(zip_two_lists(list1, list2))

'''
Задача 4: Подсчет слов в тексте

Напишите функцию, которая анализирует текст (предоставленный в виде строки)
и возвращает словарь, где ключи — это уникальные слова, а значения —
количество их появлений в тексте.
'''
# text = 'Задача 4: Подсчет слов в тексте Напишите функцию, которая анализирует текст'
# text_list = text.split()

# def list_to_dict_count(text_list):
#     my_dict = {}
#     for element in text_list:
#         if element in my_dict:
#             my_dict[element] += 1
#         else:
#             my_dict[element] = 1
#     return my_dict

# print(list_to_dict_count(text_list))
'''
Задача 5: Слияние словарей

Напишите функцию, которая объединяет два словаря
и суммирует значения одинаковых ключей.
'''
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3.5, 'c': 4, 'd': 5}
# print(dict2['b'].isdigit())

# def merge_n_sum_same_keys(dict1, dict2):
#     result = dict1
#     for key, value in dict2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value
#     return result

# print(merge_n_sum_same_keys(dict1, dict2))
'''
Задача 6: Частота элементов в списке

Напишите функцию, которая принимает список и возвращает словарь,
где ключи — это элементы списка, а значения — частота их появления.
'''
# def list_to_dict_counter(list):
#     dictionary = {}
#     for element in list:
#         if element in dictionary:
#             dictionary[element] += 1
#         else:
#             dictionary[element] = 1
#     return dictionary

# text = 'Напишите функцию, которая принимает список и возвращает словарь, где ключи — это элементы списка, а значения — частота их появления.'
# text_list = text.split()
# result = list_to_dict_counter(text_list)
# print(result)
'''
Задача 7: Разница между множествами

Напишите функцию, которая находит разницу
между двумя множествами и возвращает её в виде нового множества.
'''
# def find_difference(set1, set2):
#     set3 = set()
#     for i in set1:
#       if i not in set2:
#          set3.add(i)
#     for i in set2:
#        if i not in set1:
#           set3.add(i)
#     return set3
'''
Задача 8: Сортировка списка кортежей

Напишите функцию, которая принимает список кортежей,
и каждый кортеж содержит два элемента.
Функция должна возвращать список кортежей,
отсортированный по второму элементу каждого кортежа.
'''
# def sort_tuples_by_second_element(tuple_list):
#     def get_second_element(item):
#         return item[1]
    
#     return sorted(tuple_list, key=get_second_element)

# list = [(1, 5), (2, 3), (3, 8), (4, 1)]
# print(sort_tuples_by_second_element(list))
'''
Задача 9: Самое длинное слово в строке

Напишите функцию, которая принимает строку
и возвращает самое длинное слово в этой строке.
'''
# def longest_word(text):
#     text_list = text.split()
#     longest = ''
#     for word in text_list:
#         if len(word) > len(longest):
#             longest = word
#     return longest
'''
Задача 10: Генерация пароля
Напишите функцию, которая будет генерировать случайный пароль.
В пароле должно быть от 8 до 15 символов Юникода из диапазонов 48-57 (цифры),
65-90 (буквы латинского алфавита в верхнем регистре)
и 97-122 (буквы латинского алфавита в нижнем регистре).
Сгенерируйте и выведите на экран три пароля.
'''
# import random

# def generate_password():
#     length = random.randint(8, 15)
#     password = ''
#     for _ in range(length):
#         category = random.choice([1, 2, 3])
#         if category == 1:           
#             char = chr(random.randint(48, 57))
#         elif category == 2:
#             char = chr(random.randint(65, 90))
#         else:
#             char = chr(random.randint(97, 122))
#         password += char
#     return password

# print(generate_password())

# print(generate_password())

# print(generate_password())
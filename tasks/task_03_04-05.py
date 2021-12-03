"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла
и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.

5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и
вывод всех подстрок, состоящих из букв и цифр, например: example345.
"""

from random import randint, choices, sample
from string import ascii_letters
import os
import re
from typing import Union


def get_random_string() -> str:
    """
    Функция возвращает случайную строку длинной от 5 до 10 букв латинского алфавита
    :return: str
    """
    length = randint(5, 10)
    return ''.join(choices(ascii_letters, k=length))


def create_data_file(list_length: int, filename: str):
    """
    Функция создаёт текстовый файл со строками, состоящими из строки и числа.
    Значения строк и числе формируются случайным образом.
    :param list_length: количество строк
    :param filename: имя файла для записи
    :return: None
    """
    if os.path.exists(filename):
        raise FileExistsError(f'Файл с именем {filename} уже существует!')
    if list_length <= 0 or not isinstance(list_length, int):
        raise ValueError(f'Длина списков должна быть положительным целым числом!')

    strings_list = [get_random_string() for _ in range(list_length)]
    numbers_list = [randint(1, 100) for _ in range(list_length)]

    with open(filename, 'w', encoding='utf-8') as file:
        for item in zip(strings_list, numbers_list):
            print(*item, file=file)


def get_data_from_file(filename):
    """
    Функция для построчного вывода данных из файла
    :param filename: имя файла
    :return: None
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


def create_data_file_refactored(list_length: int, filename: str):
    """
    Функция создаёт текстовый файл со строками, состоящими из строки и числа.
    Значения строк и числе формируются случайным образом.
    Некторорые строки случайным образом заменяются на значение строка+число.
    :param list_length: количество строк
    :param filename: имя файла для записи
    :return: None
    """
    # if os.path.exists(filename):
    #     raise FileExistsError(f'Файл с именем {filename} уже существует!')
    if list_length <= 0 or not isinstance(list_length, int):
        raise ValueError(f'Длина списков должна быть положительным целым числом!')

    strings_list = [get_random_string() for _ in range(list_length)]
    numbers_list = [randint(1, 100) for _ in range(list_length)]
    replace_number = randint(1, list_length)
    indexes = sample(range(list_length), k=replace_number)
    for idx in indexes:
        strings_list[idx] = f'{strings_list[idx]}{numbers_list[idx]}'

    with open(filename, 'w', encoding='utf-8') as file:
        for item in zip(strings_list, numbers_list):
            print(*item, file=file)


def get_data_from_file_replaces(filename: str, replace_value: Union[str, int],
                                new_value: Union[str, int], all_substrings=False):
    """
    Функция выводит в консоль строки из файла, предварительно заменив в них указанные подстроки на новое значение
    (только первое вхождение или все, в зависимости от флага).
    Помимо этого функция выводит все строки, содержащие смешанные подстроки (где имеются числа и буквы вперемешку)
    :param filename: имя файла
    :param replace_value: значение, которое требуется заменить
    :param new_value: значение, на которое требуется заменить
    :param all_substrings: флаг, определяющий, уровень замены подстрок (первое вхождение или все)
    :return: None
    """
    pattern = re.compile(r'([a-zA-Z]+\d+)|(\d+\[a-zA-Z]+)')
    substrings = []
    with open(filename, encoding='utf-8') as file:
        flag = True
        for line in file:
            is_include = str(replace_value) in line
            if is_include:
                line = line.replace(str(replace_value), str(new_value))
            if re.match(pattern, line) or (is_include and flag):
                if is_include:
                    if not all_substrings:
                        flag = False
                substrings.append(line)
        print(*substrings, sep='')


if __name__ == '__main__':
    print('****************************************************')
    print('Работа функций create_data_file и get_data_from_file:\n')
    create_data_file(50, 'file_01.txt')
    get_data_from_file('file_01.txt')
    print('****************************************************\n')
    print('Работа функций create_data_file_refactored и get_data_from_file_replaces:\n')
    create_data_file_refactored(50, 'file_02.txt')
    get_data_from_file_replaces('file_02.txt', 0, 'abc', True)
    print('****************************************************\n')

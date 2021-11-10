"""
Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""

import os


def print_directory_contents(s_path: str):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    :param s_path: путь к каталогу
    :return: None
    """
    if not os.path.isdir(s_path):
        print(os.path.dirname(os.path.realpath(s_path)), os.path.basename(s_path), sep='\t')
        return
    else:
        print(os.path.realpath(s_path))
        for path in os.listdir(s_path):
            abs_path = os.path.join(s_path, path)
            print_directory_contents(abs_path)


if __name__ == '__main__':
    print_directory_contents('../venv')

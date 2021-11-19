"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения).
"""

import os
from typing import Tuple


def get_file_name(filename: str) -> Tuple[str, str]:
    """
    Функция возвращает полный путь до файла с указанным именем, а также имя файла без расширения
    :param filename: имя файла с расширением
    :return: кортеж строк
    """
    if os.path.exists(filename):
        full_path = os.path.realpath(filename)
        name = os.path.basename(full_path).split('.')[0]
        return full_path, name
    raise FileExistsError(f'Файл {filename} отсутствует в текущей дирректории')


if __name__ == '__main__':
    print(get_file_name('task_03_01.py'))

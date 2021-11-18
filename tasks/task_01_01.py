"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""

from typing import Callable

DATA_TO_STR = lambda data_list: '\t'.join(f'{item[0]} x {item[1]} = {item[2]}' for item in data_list)


class DimensionMultiplicationTableError(ValueError):
    def __str__(self):
        return 'Ошибка размерности: параметры должны быть целыми числами от 1 до 10!'


def multiplication_table(a: int, b: int):
    """
    Функция выводит в консоль таблицу умножения, размерностью A x B
    :param a: параметр A
    :param b: параметр B
    :return: None
    """
    if not (isinstance(a, int) and isinstance(b, int) and 0 < a < 11 and 0 < b < 11):
        raise DimensionMultiplicationTableError
    for number_1 in range(1, a + 1):
        data_row = []
        for number_2 in range(1, b + 1):
            data_row.append((number_2, number_1, number_2 * number_1))
        print(DATA_TO_STR(data_row))


# вариант, где лямбда-функция передаётся как аргумент:
def multiplication_table_2(a: int, b: int, data_to_str: Callable):
    """
    Функция выводит в консоль таблицу умножения, размерностью A x B
    :param a: параметр A
    :param b: параметр B
    :param data_to_str: функция-обработчик для формирования строк
    :return: None
    """
    if not (0 < a < 11 and 0 < b < 11 and isinstance(a, int) and isinstance(b, int)):
        raise DimensionMultiplicationTableError
    for number_1 in range(1, a + 1):
        data_row = []
        for number_2 in range(1, b + 1):
            data_row.append((number_2, number_1, number_2 * number_1))
        print(data_to_str(data_row))


if __name__ == '__main__':

    multiplication_table(10, 10)
    multiplication_table_2(10, 10, DATA_TO_STR)

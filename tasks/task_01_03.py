"""
Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""

from time import time
from typing import Union
from pprint import pprint


class RandomNumberParameterError(ValueError):
    def __str__(self):
        return 'Ошибка границ генерации: ' \
               'начальная граница не может быть больше или равна конечной, ' \
               'параметром функции не может быть ноль'


def random_number(start_number: Union[int, float],
                  end_number: Union[int, float],
                  float_numbers=False) -> Union[int, float]:
    """
    Функция генерирует случайное число в диапазоне от start_number до end_number
    :param start_number: начало диапазона
    :param end_number: конец диапазона
    :param float_numbers: флаг, определяющий тип случайного числа (int или float)
    :return: случайное число (int или float)
    """
    if start_number >= end_number or start_number == 0 or end_number == 0:
        raise RandomNumberParameterError
    rand_num = int(str(time())[-3:])/1000
    result_number = rand_num * (end_number - start_number) + start_number
    return result_number if float_numbers else round(result_number)


if __name__ == '__main__':
    data_list = [random_number(-100, 100) for _ in range(25)]
    data_dict = {f'elem_{key:02}': random_number(-90.5, 90.5, True) for key in range(25)}

    print(data_list)
    pprint(data_dict)

"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""

import re


def number_parts_equal(number: str):
    """
    Функция принимает строку, содержащую число, и возвращает True,
    если число дробное и его целая и дробная части равны.
    Также функция выводит в консоль сообщение о том, является ли число дробным или целым
    :param number: строка, содержащая число
    :return: True или False
    """
    number_parts = number.split('.')
    print(f'Число {number} дробное' if len(number_parts) == 2 else f'Число {number} целое')
    if len(number_parts) == 2 and number_parts[0] == number_parts[1]:
        return True
    return False


def is_number_parts_equal() -> bool:
    """
    Функция запрашивает у пользователя число и возвращает True,
    если число дробное и его целая и дробная части равны.
    :return: True или False
    """
    number = input('Введите число:')
    pattern = re.compile(r'^\d+[.,]?\d*$')
    if re.match(pattern, number):
        number = number.replace(',', '.')
        return number_parts_equal(number)
    raise ValueError('Значение не соответствует формату целого или дробного числа')


if __name__ == '__main__':
    print(is_number_parts_equal())

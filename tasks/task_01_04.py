"""
Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка:

1 000 – 10 000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10 000 – 100 000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100 000 – 1 000 000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов
и выполнять расчет по нужной процентной ставке.
Функция возвращает сумму вклада на конец срока.
"""

from typing import Union


class DepositProductError(ValueError):
    def __str__(self):
        return 'Ошибка входных данных: сумма или срок вклада вне возможного диапазона '


# Решила сделать банковские продукты в виде словаря,
# где ключами были бы кортежи - всегда хотелось попробовать, как такое работает.

# В данном случае банковские продукты определены прямо в функции для простоты,
# хотя было бы предпочтительнее определить их как константу и передавать в функцию как параметр,
# если это функция для использования в нескольких проектах
# или просто обращаясь к константе из функции напрямую, если у функции исключительно локальное применение

def deposit_sum(dep_sum: Union[int, float], dep_period: int) -> float:
    """
    Функция возвращает сумму вклада на конец срока на основании начальной суммы и срока вклада.
    Условия начисления процентов не изменяются в течение срока вклада,
    если сумма вклада в какой-то момент превысит изначальный диапазон.
    :param dep_sum: начальная сумма вклада
    :param dep_period: срок вклада в месяцах
    :return: сумма вклада на конец срока
    """

    dep_products = {
        (1000, 10000): {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        (10000, 100000): {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        (100000, 1000000): {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    }

    dep_product = None

    for start, end in dep_products:
        if start <= dep_sum <= end:
            dep_product = dep_products.get((start, end))
            break

    if dep_product:
        percent = dep_product.get(dep_period)
        if not percent:
            raise DepositProductError
        current_sum = dep_sum * (1 + percent / 12 / 100 * dep_period)
        return round(current_sum, 2)

    raise DepositProductError


if __name__ == '__main__':

    TEST_DATA = (
        (1000, 6),
        (1000, 24),
        (1000, 7),
        (10500, 24),
        (1000000, 6),
        (500, 12),
    )

    for item in TEST_DATA:
        try:
            print(deposit_sum(*item))
        except DepositProductError as error:
            print(error)
"""
Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.
"""

from typing import Union
from task_01_04 import DepositProductError


def deposit_sum(dep_sum: Union[int, float], dep_period: int, additional_sum: Union[int, float]) -> float:
    """
    Функция возвращает сумму вклада на конец срока на основании начальной суммы, срока вклада и
    суммы ежемесячного пополнения (без учёта первого и последнего месяцев).
    Условия начисления процентов не изменяются в течение срока вклада,
    если сумма вклада в какой-то момент превысит изначальный диапазон.
    :param dep_sum: начальная сумма вклада
    :param dep_period: срок вклада в месяцах
    :param additional_sum: сумма ежемесячного пополнения
    :return: сумма вклада на конец срока
    """
    def calculate_additional_sum() -> float:
        """
        Функция для вычисления суммы дополнительных взносов с процентами за весь период,
        без учёта первого и последнего месяца
        :return: сумма дополнительных взносов с процентами
        """
        # Возможно что-то напутала с вычислением процентов. Есть разные способы начисления,
        # исходила из того, что сумма начисления каждый раз увеличивается на дополнительную сумму и
        # новый процент берётся от увеличенной суммы, но без учёта начисленных процентов.
        # Тогда получим, что проценты от дополнительной суммы за период без учёта двух месяцев будут равны:
        # additional_sum * процент + 2 * additional_sum * процент + ... + n * additional_sum * процент =
        # = additional_sum * (1 + 2 + ... + n) * процент
        percents = additional_sum * sum(range(1, dep_period - 1)) * (percent / 12 / 100)
        result_add_sum = additional_sum * (dep_period - 2) + percents
        return result_add_sum

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

    if dep_product and additional_sum >= 0:
        percent = dep_product.get(dep_period)
        if not percent:
            raise DepositProductError
        current_sum = dep_sum * (1 + percent / 12 / 100 * dep_period) + calculate_additional_sum()
        return round(current_sum, 2)
    raise DepositProductError


if __name__ == '__main__':

    TEST_DATA = (
        (1000, 6, 100),
        (1000, 6, 0),
        (1000, 7, 0),
        (10500, 24, 1000),
        (1000000, 6, 15000),
        (1000, 12, -200),
    )

    for item in TEST_DATA:
        try:
            print(deposit_sum(*item))
        except DepositProductError as error:
            print(error)


"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи,
во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""


def create_dict(keys: list, values: list) -> dict:
    """
    Функция, создающая словарь из двух списков (в т.ч. неравной длины)
    :param keys: список ключей
    :param values: список значений
    :return: словарь
    """
    result_dict = dict().fromkeys(keys)
    result_dict.update(zip(keys, values))
    return result_dict


if __name__ == '__main__':
    keys_list_1 = [f'key_{num:02}' for num in range(1, 10)]
    keys_list_2 = [f'key_{num:02}' for num in range(1, 15)]
    values_list_1 = [f'value_{num:02}' for num in range(1, 15)]
    values_list_2 = [f'value_{num:02}' for num in range(1, 10)]

    print(create_dict(keys_list_1, values_list_1))
    print(create_dict(keys_list_2, values_list_2))

"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    __name = 'Product'
    __price = 45

    @classmethod
    def get_price(cls):
        return cls.__price

    @classmethod
    def get_name(cls):
        return cls.__name


class ItemDiscountReport(ItemDiscount):

    @classmethod
    def get_parent_data(cls):
        return f'Название: {cls.get_name()}; цена: {cls.get_price()}'

    # А так будет ошибка:
    # @classmethod
    # def get_parent_data(cls):
    #     return f'Название: {cls.__name}; цена: {cls.__price}'


if __name__ == '__main__':

    parent_item = ItemDiscount()
    print(ItemDiscountReport.get_parent_data())

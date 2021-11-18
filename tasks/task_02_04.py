"""
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке).
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

    @classmethod
    def set_price(cls, price):
        cls.__price = price


class ItemDiscountReport(ItemDiscount):

    @classmethod
    def get_parent_data(cls):
        return f'Название: {cls.get_name()}; цена: {cls.get_price()}'


if __name__ == '__main__':

    parent_item = ItemDiscount()
    parent_item.set_price(100)
    print(ItemDiscountReport.get_parent_data())

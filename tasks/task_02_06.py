"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportPrice(ItemDiscount):

    @classmethod
    def get_info(cls):
        return f'Цена: {cls.get_price()}'


class ItemDiscountReportName(ItemDiscount):

    @classmethod
    def get_info(cls):
        return f'Название: {cls.get_name()}'


if __name__ == '__main__':

    print(ItemDiscountReportName.get_info())
    print(ItemDiscountReportPrice.get_info())

    print(getattr(ItemDiscountReportName, 'get_info')())
    print(getattr(ItemDiscountReportPrice, 'get_info')())

    a = ItemDiscountReportName()
    b = ItemDiscountReportPrice()
    print(a.get_info())
    print(b.get_info())

"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
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

    def __init__(self, discount):
        super().__init__()
        self.discount = discount

    def __str__(self):
        discount_price = self.get_price() * (1 - self.discount / 100)
        return f'Цена товара {self.get_name()} со скидкой: {discount_price}'

    @classmethod
    def get_parent_data(cls):
        return f'Название: {cls.get_name()}; цена: {cls.get_price()}'


if __name__ == '__main__':

    parent_item = ItemDiscount()
    discount_item = ItemDiscountReport(10)
    print(discount_item)
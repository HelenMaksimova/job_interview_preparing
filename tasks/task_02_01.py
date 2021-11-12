"""
Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    name = 'Product'
    price = 45


class ItemDiscountReport(ItemDiscount):

    @classmethod
    def get_parent_data(cls):
        return f'Название: {cls.name}; цена: {cls.price}'


if __name__ == '__main__':

    parent_item = ItemDiscount()
    print(ItemDiscountReport.get_parent_data())

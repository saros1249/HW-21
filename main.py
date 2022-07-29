from abstract_class import Storage


class Store(Storage):

    def __init__(self, capacity=100):
        self._items = {'печенье': 5, 'ёлка': 9, 'ёжик': 2, 'вода': 10, 'пиво': 16, 'хлеб': 25}
        self._capacity: int = capacity

    def get_items(self):
        return self._get_items

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def _get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._items)

    @_get_items.setter
    def _get_items(self, data):
        self._items.update(data)
        for key in self._items:
            self._capacity = self._capacity - self._get_items[key]

    def add(self, title, change_qnt):
        qnt = self._get_items[title]
        if (self.get_free_space + change_qnt) <= 100:
            self._get_items[title] = (qnt + change_qnt)
            self._capacity = self._capacity + change_qnt
        else:
            print('Нет места')

    def remove(self, title, change_qnt):
        qnt = self._get_items[title]
        if (self.get_free_space - change_qnt) >= 0 and change_qnt <= qnt:
            self._get_items[title] = (qnt - change_qnt)
            self._capacity = self._capacity - change_qnt
        else:
            print('Нет запрошенного количества')


class Shop(Storage):

    def __init__(self, capacity=20):
        self._items = {'ёлка': 1, 'ёжик': 1, 'вода': 5, 'пиво': 6, 'хлеб': 2}
        self._capacity: int = capacity

    def get_items(self):
        return self._get_items

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def _get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._items)

    @_get_items.setter
    def _get_items(self, data):
        self._items.update(data)
        for key in self._items:
            self._capacity = self._capacity - self._get_items[key]

    def add(self, title, change_qnt):
        qnt = self._get_items[title]
        if (self.get_free_space + change_qnt) <= 20 and self.get_unique_items_count < 5:
            self._get_items[title] = (qnt + change_qnt)
            self._capacity = self._capacity + change_qnt
        else:
            print('Нет места')

    def remove(self, title, change_qnt):
        qnt = self._get_items[title]
        if (self.get_free_space - change_qnt) >= 0 and change_qnt <= qnt:
            self._get_items[title] = (qnt - change_qnt)
            self._capacity = self._capacity - change_qnt
        else:
            print('Нет запрошенного количества')


# class Request:
#
#     def __init__(self):
#         pass
#
#     def way(self, amount, product, where_from, to):
#         return where_from, to, amount, product

if __name__ == '__main__':
    # print('Здравствуйте. Вас приветствует симулятор логистики. Давайте познакомимся. Как Вас зовут?')
    # name = input('Введите ваше имя: ')
    # print(f'Здрвствуйте, {name}! Начнём?')
    # var = input(f'Введите "y", если хотите продолжить, или "n", если хотите выйти')
    # if var == 'n':
    #     quit()
    # else:
    store = Store()
    shop = Shop()
    # request = Request()
    print('На складе доступно:')
    print(store.get_items())
    print('В магазине доступно:')
    print(shop.get_items())
    while True:
        amount, product, where_from = input('Введите количество и название товара, откуда его нужно забрать через запятую: ')
        print(f'Курьер забирает {amount} {product} из {where_from}')

        if where_from == 'склад':
            var_d = store.get_items()
        elif where_from == 'магазин':
            var_d = shop.get_items()
        else:
            print(f'{where_from} - такого места не существует.')

        if {product: amount} in var_d and amount <= var_d[product]:
            print(f'Нужное количество есть на {where_from}')
        else:
            print(f'Не хватает на {where_from}, попробуйте заказать меньше')

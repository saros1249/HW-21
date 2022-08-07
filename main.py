from os import abort

from abstract_class import Storage


class Store(Storage):

    def __init__(self):
        self._items = {'печенье': 5, 'ёлка': 9, 'ёжик': 2, 'вода': 10, 'пиво': 16, 'хлеб': 25}
        self._capacity = 100

    def get_items(self):
        return self._get_items

    @property
    def get_free_space(self):
        space = 0
        for key in self._items:
            space = space + self._get_items[key]
        return self._capacity - space

    @property
    def _get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._get_items)

    @_get_items.setter
    def _get_items(self, data):
        self._items.update(data)
        for key in self._items:
            self._capacity = self._capacity - self._get_items[key]

    def add(self, title, change_qnt):
        qnt = self._get_items[title]
        if (self.get_free_space + int(change_qnt)) <= 100:
            self._get_items[title] = (qnt + int(change_qnt))
            return True
        else:
            return False

    def remove(self, title, change_qnt):

        if (self.get_free_space - int(change_qnt)) >= 0 and int(change_qnt) <= self._get_items[title]:
            qnt = self._get_items[title]
            self._get_items[title] = (qnt - int(change_qnt))
            return True
        else:
            return False


class Shop(Storage):

    def __init__(self):
        self._items = {'ёлка': 1, 'ёжик': 1, 'вода': 5, 'пиво': 6, 'хлеб': 2}
        self._capacity = 20

    def get_items(self):
        return self._get_items

    @property
    def get_free_space(self):
        space = 0
        for key in self._items:
            space = space + self._get_items[key]
        return self._capacity - space

    @property
    def _get_items(self):
        return self._items

    @property
    def get_unique_items_count(self):
        return len(self._get_items)

    @_get_items.setter
    def _get_items(self, data):
        self._items.update(data)
        for key in self._items:
            self._capacity = self._capacity - self._get_items[key]

    def add(self, title, change_qnt):
        if self.get_unique_items_count < 5 and (self.get_free_space + int(change_qnt)) <= 20:
            qnt = self._get_items[title]
            self._get_items[title] = (qnt + int(change_qnt))
            return True
        else:
            return False

    def remove(self, title, change_qnt):
        qnt = self._get_items[title]
        if (self.get_free_space - int(change_qnt)) >= 0 and int(change_qnt) <= self._get_items[title]:
            self._get_items[title] = (qnt - int(change_qnt))
            return True
        else:
            return False


class Request:

    def __init__(self):

        self.amount = int
        self.product = ''
        self.where_from = ''
        self.to = ''

    def way(self, amount, product, where_from):

        global var_where_from, var_to
        if where_from == 'склад':
            to = 'магазин'
            var_where_from = store
            var_to = shop
        elif where_from == 'магазин':
            to = 'склад'
            var_where_from = shop
            var_to = store
        else:
            return print(f'Ошибка. Места загрузки либо выгрузки не существует.')

        if var_where_from.remove(product, amount):
            print(f'Нужное количество есть на {where_from}')
            if var_to.add(product, amount):
                return print(f'Курьер забирает {amount} {product} из {where_from} для доставки в {to}\n'
                             f'Курьер забрал {amount} {product} из {where_from}\n'
                             f'Курьер везет {amount} {product} из {where_from} в {to}\n'
                             f'Курьер доставил {amount} {product} в {to}')
            var_where_from.add(product, amount)
            return print(f'Не хватает места в {to}, попробуйте заказать другое количество')
        return print(f'Не хватает в {where_from}, попробуйте заказать меньше')


if __name__ == '__main__':
    print('Здравствуйте. Вас приветствует симулятор логистики. Давайте познакомимся. Как Вас зовут?')
    name = input('Введите ваше имя: ')
    print(f'Здрвствуйте, {name}! Начнём?')

    store = Store()
    shop = Shop()
    request = Request()

    while True:
        print('На складе доступно:')
        print(store.get_items())
        print('В магазине доступно:')
        print(shop.get_items())

        amount = input('Введите количество товара, которое нужно переместить:')
        product = input('Введите название товара, который нужно переместить:')
        where_from = input('Введите место, откуда его нужно забрать товар:')

        request.way(amount, product, where_from)

        var = input(f'Введите "д", если хотите продолжить, или "н", если хотите выйти')
        if var == 'н':
            quit()
        else:
            continue

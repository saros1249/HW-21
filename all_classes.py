from abstract_class import Storage


class Store(Storage):

    capacity = 100

    def __init__(self, item, title, capacity):
        super().__init__()
        self._items = item
        self.title = title
        self._capacity = capacity

    @property
    def get_free_space(self):
        return Store.capacity - self._capacity

    @property
    def get_items(self):
        return self._items.items(self.title)

    @property
    def get_unique_items_count(self):
        return len(self._items)

    def add(self, change_qnt):
        qnt = self.get_items[self.title]
        if (self.get_free_space + change_qnt) <= Store.capacity:
            self.get_items[self.title] = (qnt + change_qnt)

    def remove(self, change_qnt):
        qnt = self.get_items[self.title]
        if (self.get_free_space - change_qnt) >= 0:
            self.get_items[self.title] = (qnt + change_qnt)

class Shop(Storage):

    capacity = 20

    def __init__(self, item, title, capacity):
        super().__init__()
        self._items = item
        self.title = title
        self._capacity = capacity

    @property
    def get_free_space(self):
        return Shop.capacity - self._capacity

    @property
    def get_items(self):
        return self._items.items(self.title)

    @property
    def get_unique_items_count(self):
        return len(self._items)

    def add(self, change_qnt):
        qnt = self.get_items[self.title]
        if (self.get_free_space + change_qnt) <= Shop.capacity and self.get_unique_items_count < 5:
            self.get_items[self.title] = (qnt + change_qnt)

    def remove(self, change_qnt):
        qnt = self.get_items[self.title]
        if (self.get_free_space - change_qnt) >= 0:
            self.get_items[self.title] = (qnt + change_qnt)

class Request():
    def __init__(self, where_from, to, amount, product):
        self.where_from = where_from
        self.to = to
        self.amount = amount
        self.product = product


    def way(self, amount, product, where_from, to):

        return where_from, to, amount, product


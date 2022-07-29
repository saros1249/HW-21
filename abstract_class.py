from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def _get_items(self):
        pass

    @_get_items.setter
    @abstractmethod
    def _get_items(self, data):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


    @abstractmethod
    def add(self, title, change_qnt):
        pass

    @abstractmethod
    def remove(self, title, change_qnt):
        pass


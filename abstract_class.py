from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self):
        self.items = item
        self.capacity = capacity

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass

    @abstractmethod
    def add(self, change_qnt):
        pass

    @abstractmethod
    def remove(self, change_qnt):
        pass


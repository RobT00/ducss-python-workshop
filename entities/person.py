from abc import abstractmethod
from abc import ABC


class Person(ABC):
    def __init__(self, my_town):
        self._my_town = my_town
        self._my_world = my_town.get_world()

    @abstractmethod
    def do_work(self):
        pass

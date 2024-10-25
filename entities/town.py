import sys

from entities.farmer import Farmer
from entities.mason import Mason
from entities.world import Food
from entities.world import Gold
from entities.world import Wood
from entities.world import Stone
from entities.world import World


class Town:
    def __init__(self, my_world: World):
        self._my_world = my_world
        self._persons = []
        self._food_store = [Food(), Food()]
        self._wood_store = []
        self._stone_store = []
        self._gold_store = []

        self.create_farmer()
        self.create_farmer()

    def _consume_food(self, food_qty):
        if len(self._food_store) >= food_qty:
            for _ in range(food_qty):
                self._food_store.pop()
        else:
            print("insufficient food", file=sys.stderr)

    def create_farmer(self) -> Farmer:
        my_farmer = Farmer(self)
        self._consume_food(1)
        self._persons.append(my_farmer)
        return my_farmer

    def create_mason(self) -> Mason:
        my_mason = Mason(self)
        self._consume_food(2)
        self._persons.append(my_mason)
        return my_mason

    def time_elapsed(self):
        for person in self._persons:
            resource = person.do_work()

            if isinstance(resource, Food):
                self._food_store.append(resource)
            elif isinstance(resource, Wood):
                self._wood_store.append(resource)
            elif isinstance(resource, Gold):
                self._gold_store.append(resource)
            elif isinstance(resource, Stone):
                self._stone_store.append(resource)

    def stats(self):
        return f"""
Food                    {len(self._food_store)}
Wood                    {len(self._wood_store)}
Gold                    {len(self._gold_store)}
Stone                   {len(self._stone_store)}
Person                  {len(self._persons)}
"""

    def get_world(self) -> World:
        return self._my_world

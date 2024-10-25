from typing import Optional


class Gold:
    pass


class Stone:
    pass


class Wood:
    pass


class Food:
    pass


class World:
    def __init__(self):
        pass

    def mine_gold(self) -> Optional[Gold]:
        return Gold()

    def cut_wood(self) -> Optional[Wood]:
        return Wood()

    def get_food(self) -> Optional[Food]:
        return Food()

    def mine_stone(self) -> Optional[Stone]:
        return Stone()

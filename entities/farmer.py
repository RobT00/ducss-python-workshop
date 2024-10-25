from entities.person import Person


class Farmer(Person):
    def do_work(self):
        return self._my_world.get_food()

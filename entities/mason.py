from entities.person import Person


class Mason(Person):
    def do_work(self):
        return self._my_world.mine_stone()

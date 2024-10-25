import itertools

from entities.town import Town
from entities.world import World


def main():
    my_world = World()
    my_town = Town(my_world)

    for time_point in itertools.count(start=0):
        print(my_town.stats())
        cmd_line_text = input(f"Timepoint {time_point} $> ")  # prompt

        if cmd_line_text == "exit":  # Exit infinite loop
            break

        if cmd_line_text == "create farmer":
            my_town.create_farmer()
        elif cmd_line_text == "create mason":
            my_town.create_mason()

        my_town.time_elapsed()


if __name__ == "__main__":
    main()

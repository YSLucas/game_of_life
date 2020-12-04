from World import *
import copy

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        width = self.world.width
        height = self.world.height

        prev_state_world = copy.copy(self.world)
        for x in range(0, width):
            for y in range(0, height):
                cell_state = prev_state_world.get(x, y)
                neighbours = prev_state_world.get_neighbours(x, y).count(1)
                
                # rule 1
                if cell_state and neighbours < 2:
                    self.world.set(x, y, 0)
                # rule 2
                elif cell_state and neighbours > 3:
                    self.world.set(x, y, 0)
                # rule 3
                elif cell_state and 1 < neighbours < 4:
                    self.world.set(x, y, 1)
                # rule 4
                elif not cell_state and neighbours == 3:
                    self.world.set(x, y, 1)
                else:
                    continue


        self.generation += 1


        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world
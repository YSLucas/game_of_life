from unittest import TestCase
from Simulator import *
from World import *


class TestNewRules(TestCase):

    def setUp(self):

        self.width, self.height = 10, 12
        self.sim = Simulator(world=World(self.width, self.height), bx=4, sy=45)
        self.world = self.sim.get_world()
    
    def test_new_birth(self):
        """
        Tests simulation with new birth rule
        """

        x, y = 4, 4

        alive_neighbours = self.sim.bx # set number of alive neighbours to given parameter

        # set neighbours and middle cell
        for x_minmax in range(x - 1, x + 2):
            for y_minmax in range(y - 1, y + 2):
                
                if (x_minmax, y_minmax) == (x, y):
                    self.world.set(x, y, 0)
                    continue

                elif alive_neighbours != 0:
                    self.world.set(x_minmax, y_minmax, 1)
                    alive_neighbours -= 1
                else:
                    self.world.set(x_minmax, y_minmax, 0)
        
        prev_value = self.world.get(x, y)          # get current state of cell
        
        self.sim.set_world(self.world)             # set sim world
        self.sim.update()                          # update world once
        self.world = self.sim.get_world()          # get world after sim

        new_value = self.world.get(x, y)           # get new state of cell
        
        # do test
        self.assertNotEqual(prev_value, new_value)

    def test_new_survival(self):
        """
        Tests simulation with new survival rule
        """

        x, y = 4, 4

        alive_neighbours = self.sim.sy # set number of alive neighbours to given parameter
        alive_neighbours = [int(i) for i in str(alive_neighbours)] # 23 should be 2, 3

        # set neighbours and middle cell
        for x_minmax in range(x - 1, x + 2):
            for y_minmax in range(y - 1, y + 2):
                
                if (x_minmax, y_minmax) == (x, y):
                    self.world.set(x, y, 0)
                    continue

                elif alive_neighbours != 0:
                    self.world.set(x_minmax, y_minmax, 1)
                    alive_neighbours -= 1
                else:
                    self.world.set(x_minmax, y_minmax, 0)
        
        prev_value = self.world.get(x, y)          # get current state of cell
        
        self.sim.set_world(self.world)             # set sim world
        self.sim.update()                          # update world once
        self.world = self.sim.get_world()          # get world after sim

        new_value = self.world.get(x, y)           # get new state of cell
        
        # do test
        self.assertEqual(prev_value, new_value)
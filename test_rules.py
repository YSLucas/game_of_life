from unittest import TestCase
from Simulator import *
import random


class TestRules(TestCase):

    def setUp(self):

        self.width, self.height = 10, 12
        self.sim = Simulator(world=World(self.width, self.height))
        self.world = self.sim.get_world()


    def test_exposure(self):
        """
        Test for exposure rule. 
        Exposure rule: any alive cell with less than 2 alive neighbour cells dies
        """
        x, y = 4, 4
        # set cell to alive
        self.world.set(x, y, 1)
        # set neighbour cells according to rule
        self.world.set(3, 3, 1)
        self.world.set(3, 4, 0)
        self.world.set(3, 5, 0)
        self.world.set(4, 3, 0)
        self.world.set(4, 5, 0)
        self.world.set(5, 3, 0)
        self.world.set(5, 4, 0)
        self.world.set(5, 5, 0)


        prev_value = self.world.get(x, y)          # get current state of cell
        # self.sim.set_world(self.world)
        self.sim.update()                          # update world once
        # self.world = self.sim.get_world()
        new_value = self.world.get(x, y)           # get new state of cell

        self.assertNotEqual(prev_value, new_value) # check if cell state changed from alive (1) to dead (0)


        # Deze versie kan werken maar dan moet de test tijdens de simulatie worden uitgevoerd.
        # get world info
        # width = self.world.width
        # height = self.world.height
        # x, y = None, None
        # prev_value = None

        # for search_x in range(0, width + 1):
        #     for search_y in range(0, height + 1):

        #         cell_state = self.world.get(search_x, search_y)
        #         neighbours = self.world.get_neighbours(search_x, search_y)

        #         if prev_value and ( neighbours.count(1) < 2 ):
        #             x, y, prev_value = search_x, search_y, cell_state
        #             break
        #     break

        # if prev_value == None:
        #     print('No alive cell found') # raise error
        #     self.assertEqual(prev_value, 0)
        # else:
        #     self.sim.update                            
        #     new_value = self.world.get(x, y)          
        #     self.assertNotEqual(prev_value, new_value)



    def test_overcrowding(self):
        """
        Test for overcrowding rule. 
        Overcrowding rule: any alive cell with more than 3 alive neighbour cells dies
        """
        x, y = 4, 4

        # set cell to alive
        self.world.set(x, y, 1)
        # set neighbour cells according to rule
        self.world.set(3, 3, 1)
        self.world.set(3, 4, 1)
        self.world.set(3, 5, 1)
        self.world.set(4, 3, 1)
        self.world.set(4, 5, 0)
        self.world.set(5, 3, 0)
        self.world.set(5, 4, 0)
        self.world.set(5, 5, 0)

        prev_value = self.world.get(x, y)          # get current state of cell
        # self.sim.set_world(self.world)
        self.sim.update()                          # update world once
        new_value = self.world.get(x, y)           # get new state of cell
        # self.world = self.sim.get_world()
        self.assertNotEqual(prev_value, new_value) # check if cell state changed from alive (1) to dead (0)

    def test_survival(self):
        """
        Test for survival rule. 
        Survival rule: any alive cell with 2 or 3 neighbours stays alive
        """
        x, y = 4, 4

        # set cell to alive
        self.world.set(x, y, 1)
        # set neighbour cells according to rule
        self.world.set(3, 3, 1)
        self.world.set(3, 4, 1)
        self.world.set(3, 5, 1)
        self.world.set(4, 3, 0)
        self.world.set(4, 5, 0)
        self.world.set(5, 3, 0)
        self.world.set(5, 4, 0)
        self.world.set(5, 5, 0)

        prev_value = self.world.get(x, y)          # get current state of cell
        # self.sim.set_world(self.world)
        self.sim.update()                          # update world once
        # self.world = self.sim.get_world()
        new_value = self.world.get(x, y)           # get new state of cell

        self.assertEqual(prev_value, new_value)    # check if cell state stayed alive (1)


    def test_birth(self):
        """
        Test for birth rule. 
        Birth rule: any dead cell with exaxtly 3 nieghbours becomes alive
        """
        x, y = 4, 4

        # set cell to dead
        self.world.set(x, y, 0)
        # set neighbour cells according to rule
        self.world.set(3, 3, 1)
        self.world.set(3, 4, 1)
        self.world.set(3, 5, 1)
        self.world.set(4, 3, 0)
        self.world.set(4, 5, 0)
        self.world.set(5, 3, 0)
        self.world.set(5, 4, 0)
        self.world.set(5, 5, 0)
        
        prev_value = self.world.get(x, y)          # get current state of cell
        # self.sim.set_world(self.world)             # set sim world
        self.sim.update()                          # update sim world once
        # self.world = self.sim.get_world()          # get world after sim
        new_value = self.world.get(x, y)           # get new state of cell

        self.assertNotEqual(prev_value, new_value) # check if cell state changed from dead (0) to alive (1)


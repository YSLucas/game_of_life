from unittest import TestCase
from Simulator import *
import random

class TestRules(TestCase):

    def setUp(self):
        self.sim = Simulator()
        self.width, self.height = 10, 12
        self.world = World(self.width, self.height)
    
    def test_alive(self):

        pass

    def test_dead(self):
        pass


    def test_exposure(self):
        """
        Test for exposure rule. 
        Exposure rule: any alive cell with less than 1 alive neighbour cells dies
        """
        # get world info
        width = self.world.width
        height = self.world.height

        while True:
            x, y = random.randint(0, width), random.randint(0, height) # get random x and y in range of board

            neighbours = self.world.get_neighbours(x, y)   # find neighbours of cell at x, y
            if neighbours.count(1) < 2:                    # check if cell has less than 2 alive nieghbours
                prev_value = self.world.get(x, y)          # get state of cell at x, y
                self.sim.update                            # update world
                new_value = self.world.get(x, y)           # get new state of cell at x, y
                self.assertNotEqual(prev_value, new_value) # check if cell changed from alive (1) to dead (0)
                break


    def test_overcrowding(self):
        x, y = 4, 4
        # TODO code die zoekt naar levende cellen
        neighbours = self.world.get_neighbours(x, y)
        if neighbours.count(1) > 3:
            prev_value = self.world.get(x, y)
            self.sim.update
            new_value = self.world.get(x, y)
            self.assertNotEqual(prev_value, new_value)
            

    def test_survival(self):
        x, y = 1, 1
        # TODO: code die zoekt naar levende cel met 2 of 3 buren

        prev_value = self.world.get(x, y)
        self.sim.update()
        new_value = self.world.get(x, y)
        self.assertEqual(prev_value, new_value) # previous value en new value blijven hetzelfde (=1)


    def test_birth(self):
        x, y, = 1, 1
        # TODO: code die zoekt naar dode een cel met 3 levende buren

        prev_value = self.world.get(x, y)
        self.sim.update()
        new_value = self.world.get(x, y)
        self.assertNotEqual(prev_value, new_value) # check of previous value van 0 (dood) naar 1 (levend) gaat

from unittest import TestCase
from Simulator import *

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
        x, y = 4, 4
        # TODO code die zoekt naar levende cellen
        neighbours = self.world.get_neighbours(x, y)
        if neighbours.count(1) < 2:
            prev_value = self.world.get(x, y)
            self.sim.update
            new_value = self.world.get(x, y)
            self.assertNotEqual(prev_value, new_value)


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

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

    def test_cell_dies(self):

        pass

    def test_exposure(self):
        x, y = 4, 4
        value = self.world.get(x, y)
        neighbours = self.world.get_neighbours(x, y)
        if neighbours.count(1) < 2:
            self.assertEqual(value, 0)
        else:
            self.assertEqual(value, 1)

    def test_overcrowding(self):
        x, y = 4, 4
        value = self.world.get(x, y)
        neighbours = self.world.get_neighbours(x, y)
        if neighbours.count(1) > 3:
            self.assertEqual(value, 0)
        else:
            self.assertEqual(value, 1)

    def test_survival(self):
        x, y = 1, 1
        self.world.set(x, y, 1)
        value = self.world.get(x, y)
        self.sim.update()
        new_value = self.world.get(x, y)
        self.assertEqual(value, new_value)


    def test_birth(self):
        pass
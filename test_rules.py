from unittest import TestCase
from Simulator import *
from World import *
import random


class TestRules(TestCase):

    def setUp(self):

        self.width, self.height = 10, 12
        self.sim = Simulator(world=World(self.width, self.height))
        self.world = self.sim.get_world()

    def test_ruleset(self, set_state, alive_neighbours):
        """
        Deze functie wordt bij iedere test uitgevoerd om de verandering van een cel na éém stap in de sumulatie terug te geven.
        Deze functie is dynamisch, dus kan voor elke test gebruikt worden zolang de juiste parameters worden meegegeven.

        (deze functie kan misschien beter buiten deze class staan)
        """
        x, y = 4, 4

        # set neighbours and middle cell
        for x_minmax in range(x - 1, x + 2):
            for y_minmax in range(y - 1, y + 2):
                
                if (x_minmax, y_minmax) == (x, y):
                    self.world.set(x, y, set_state) # middle cel (x, y) krijgt de juiste  meegegeven staat (0 of 1)
                    continue

                elif alive_neighbours != 0:
                    self.world.set(x_minmax, y_minmax, 1) # zolang er nog levende neighbours toegevoegd moeten worden wordt deze code uitgevoerd
                    alive_neighbours -= 1
                else:
                    self.world.set(x_minmax, y_minmax, 0)
        

        prev_value = self.world.get(x, y)          # get current state of cell
        
        self.sim.set_world(self.world)             # set sim world
        self.sim.update()                          # update world once
        self.world = self.sim.get_world()          # get world after sim

        new_value = self.world.get(x, y)           # get new state of cell
        
        return [prev_value, new_value]             # return result (daadwerkelijke tests worden in de bijbehorende functie zelf uitgevoerd)


    def test_exposure(self):
        """
        Test for exposure rule. 
        Exposure rule: any alive cell with less than 2 alive neighbour cells dies
        """

        for n in range(0, 2):
            result = self.test_ruleset(1, n)
            self.assertNotEqual(result[0], result[1])


    def test_overcrowding(self):
        """
        Test for overcrowding rule. 
        Overcrowding rule: any alive cell with more than 3 (max 8) alive neighbour cells dies
        """

        for n in range(4, 9):
            result = self.test_ruleset(1, n)
            self.assertNotEqual(result[0], result[1])


    def test_survival(self):
        """
        Test for survival rule. 
        Survival rule: any alive cell with 2 or 3 neighbours stays alive
        """

        for n in range(2, 4):
            result = self.test_ruleset(1, n)
            self.assertEqual(result[0], result[1])


    def test_birth(self):
        """
        Test for birth rule. 
        Birth rule: any dead cell with exaxtly 3 nieghbours becomes alive
        """

        result = self.test_ruleset(0, 3)
        self.assertNotEqual(result[0], result[1])





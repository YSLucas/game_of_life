from unittest import TestCase
from Simulator import *
import random


class TestRules(TestCase):

    def setUp(self):

        self.width, self.height = 10, 12
        self.sim = Simulator(world=World(self.width, self.height))
        self.world = self.sim.get_world()

    def test_ruleset(self, rule, set_state, alive_neighbours):
        x, y = 4, 4

        # set neighbours and middle cell
        for x_minmax in range(x - 1, x + 2):
            for y_minmax in range(y - 1, y + 2):
                
                if (x_minmax, y_minmax) == (x, y):
                    self.world.set(x, y, set_state)
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
        if rule in [1, 2, 4]:
            self.assertNotEqual(prev_value, new_value)
        else:
            self.assertEqual(prev_value, new_value)


    def test_exposure(self):
        """
        Test for exposure rule. 
        Exposure rule: any alive cell with less than 2 alive neighbour cells dies
        """
        
        self.test_ruleset(1, 1, 1) # test rule 1 with 1 neigbour alive
        self.test_ruleset(1, 1, 0) # test rule 1 with 0 neighbours alive


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

        self.test_ruleset(2, 1, 4) # test rule 2 with 4 neighbours alive
        self.test_ruleset(2, 1, 5) # test rule 2 with 5 neighbours alive
        self.test_ruleset(2, 1, 6) # test rule 2 with 6 neighbours alive
        self.test_ruleset(2, 1, 7) # test rule 2 with 7 neighbours alive
        self.test_ruleset(2, 1, 8) # test rule 2 with 8 neighbours alive


    def test_survival(self):
        """
        Test for survival rule. 
        Survival rule: any alive cell with 2 or 3 neighbours stays alive
        """

        self.test_ruleset(3, 1, 2) # test rule 3 with 2 neighbours alive
        self.test_ruleset(3, 1, 3) # test rule 3 with 3 neighbours alive


    def test_birth(self):
        """
        Test for birth rule. 
        Birth rule: any dead cell with exaxtly 3 nieghbours becomes alive
        """

        self.test_ruleset(4, 0, 3) # test rule 4 with 3 neighbours alive



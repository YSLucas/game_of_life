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
        x, y = None, None
        prev_value = None

        for search_x in range(0, width + 1):
            for search_y in range(0, height + 1):

                cell_state = self.world.get(search_x, search_y)
                neighbours = self.world.get_neighbours(search_x, search_y)

                if prev_value and ( neighbours.count(1) < 2 ):
                    x, y, prev_value = search_x, search_y, cell_state
                    break
            break

        if prev_value == None:
            print('No alive cell found') # raise error
        else:
            self.sim.update                            
            new_value = self.world.get(x, y)          
            self.assertNotEqual(prev_value, new_value)

        # while True:
        #     x, y = random.randint(0, width), random.randint(0, height) # get random x and y in range of board
        #     prev_value = self.world.get(x, y)
        #     if prev_value:                                     # check if cell is alive
        #         neighbours = self.world.get_neighbours(x, y)   # find neighbours of cell at x, y
        #         if neighbours.count(1) < 2:                    # check if cell has less than 2 alive nieghbours; else get a new cell
        #             self.sim.update                            # update world
        #             new_value = self.world.get(x, y)           # get new state of cell at x, y
        #             self.assertNotEqual(prev_value, new_value) # check if cell changed from alive (1) to dead (0)
        #             break


    def test_overcrowding(self):
        """
        Test for overcrowding rule. 
        Overcrowding rule: any alive cell with more than 3 alive neighbour cells dies
        """
        # get world info
        width = self.world.width
        height = self.world.height
        x, y = None, None
        prev_value = None

        for search_x in range(0, width + 1):
            for search_y in range(0, height + 1):

                cell_state = self.world.get(search_x, search_y)
                neighbours = self.world.get_neighbours(search_x, search_y)

                if prev_value and ( neighbours.count(1) > 3 ):
                    x, y, prev_value = search_x, search_y, cell_state
                    break
            break

        if prev_value == None:
            print('No alive cell found') # raise error
        else:
            self.sim.update                            
            new_value = self.world.get(x, y)          
            self.assertNotEqual(prev_value, new_value)

    def test_survival(self):
        """
        Test for survival rule. 
        Survival rule: any alive cell with 2 or 3 neighbours stays alive
        """
        # get world info
        width = self.world.width
        height = self.world.height
        x, y = None, None
        prev_value = None

        for search_x in range(0, width + 1):
            for search_y in range(0, height + 1):

                cell_state = self.world.get(search_x, search_y)
                neighbours = self.world.get_neighbours(search_x, search_y)

                if prev_value and ( 1 < neighbours.count(1) < 4 ):
                    x, y, prev_value = search_x, search_y, cell_state
                    break
            break

        if prev_value == None:
            print('No alive cell found') # raise error
        else:
            self.sim.update                            
            new_value = self.world.get(x, y)          
            self.assertEqual(prev_value, new_value)


    def test_birth(self):
        """
        Test for birth rule. 
        Birth rule: any dead cell with exaxtly 3 nieghbours becomes alive
        """
        # get world info
        width = self.world.width
        height = self.world.height
        x, y = None, None
        prev_value = None

        for search_x in range(0, width + 1):
            for search_y in range(0, height + 1):

                cell_state = self.world.get(search_x, search_y)
                neighbours = self.world.get_neighbours(search_x, search_y)

                if prev_value and ( neighbours.count(1) == 3 ):
                    x, y, prev_value = search_x, search_y, cell_state
                    break
            break

        if prev_value == None:
            print('No alive cell found') # raise error
        else:
            self.sim.update                            
            new_value = self.world.get(x, y)          
            self.assertNotEqual(prev_value, new_value)

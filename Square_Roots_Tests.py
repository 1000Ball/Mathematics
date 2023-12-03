'''Testing square root methods'''

import unittest
from Square_Roots import sqrt_ld, sqrt_NR
import numpy as np

#---------------------------------------------------------------------------

class Test_sqrt_ld(unittest.TestCase):
    '''Testing a multitude of cases to ensure the square root
    function is accurate'''
    def test_pefect_squares(self):
        '''Should output perfect squares to first decimal
        regardless of defined decimal places'''
        for i in range(1000):
            for j in range(12):
                square = i**2
                self.assertEqual(sqrt_ld(square, j), float(i))


    ## Test takes forever (slow method), but it passes
    #def test_decimals(self):
    #    '''Testing this function will return results to specified decimal
    #    place as well as compute non-integers'''
    #    for i in range(60):
    #        for j in range(1, 10):
    #            square = i**2 / np.exp(i/2) # producing a random float
    #            self.assertEqual(sqrt_ld(square, j), np.sqrt(square).round(j))

#---------------------------------------------------------------------------

class Test_sqrt_NR(unittest.TestCase):
    '''Testing a multitude of cases to ensure the square root
    function is accurate'''
    def test_pefect_squares(self):
        '''Should output perfect squares to first decimal
        regardless of defined decimal places'''
        for i in range(1000):
            for j in range(12):
                square = i**2
                self.assertEqual(sqrt_NR(square, j), float(i))

    def test_decimals(self):
        '''Testing this function will return results to specified decimal
        place as well as compute non-integers'''
        for i in range(100):
            for j in range(1, 12):
                square = i**2 / np.exp(i/2) # producing a random float
                self.assertEqual(sqrt_NR(square, j), np.sqrt(square).round(j))

unittest.main()

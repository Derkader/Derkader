"""
Created on July 26, 2022

@author: derek nash

Battleship Sea Unit Tests
"""

import unittest
from battleship_class import BattleshipSea as sea


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.battleshipsea = sea(50)

    def tearDown(self):
        del self.battleshipsea

    def test_object_created_required_attributes(self):
        self.assertEqual(self.battleshipsea.initial_guesses, 50)
        self.assertEqual(self.battleshipsea.guesses, 50)
        self.assertEqual(self.battleshipsea.grid_the_sea, [[0 for i in range(10)] for j in range(10)])
        self.assertEqual(self.battleshipsea.boats[1].size, 4)
        self.assertEqual(self.battleshipsea.boats[1].name, 'Battleship')

    def test_random_boat_arrangement(self):
        p = sea(50)
        p.set_boats()
        pp = sea(50)
        pp.set_boats()
        self.assertNotEqual(p.grid_the_sea, pp.grid_the_sea)

    def test_does_this_boat_fit(self):
        self.assertEqual(self.battleshipsea.does_this_boat_fit(5, 4, 4, 'vertical'), True)

    def test_does_this_boat_fit_false(self):
        self.assertEqual(self.battleshipsea.does_this_boat_fit(5, 8, 8, 'vertical'), False)

    def test_check_if_all_boats_sunk_yet(self):
        self.assertEqual(self.battleshipsea.check_if_all_boats_sunk_yet(), False)

    def test_boat_get_coords(self):
        self.assertEqual(self.battleshipsea.boats[0].return_coords(), [])

    def test_boat_set_and_get_coords(self):
        self.battleshipsea.set_boats()
        self.assertNotEqual(self.battleshipsea.boats[0].return_coords(), [])

if __name__ == '__main__':
    unittest.main()

import unittest
import base_and_derived_class as t


class RectangleClassTest(unittest.TestCase):

    def test_rectangle_initial_value_no_attributes(self):
        r = t.Rectangle()
        self.assertEqual('RED', r.color)
        self.assertEqual(0, r.length)
        self.assertEqual(0, r.width)

    def test_rectangle_initial_value_optional_attributes(self):
        r = t.Rectangle('GREEN', 5.2, 7.2)
        self.assertEqual('GREEN', r.color)
        self.assertEqual(5.2, r.length)
        self.assertEqual(7.2, r.width)

    def test_rectangle_ojbect_not_created_invalid_attributes(self):
        with self.assertRaises(t.InvalidColorError):
            t.Rectangle('blue')
        with self.assertRaises(ValueError):
            t.Rectangle('BLUE', -1, 1)
        with self.assertRaises(ValueError):
            t.Rectangle('BLUE', 1, -1)

    def test_rectangle_change_color_valid_attribute(self):
        r = t.Rectangle()
        r.change_color('ORANGE')
        self.assertEqual(r.color, 'ORANGE')

    def test_rectangle_change_color_invalid_attribute(self):
        with self.assertRaises(t.InvalidColorError):
            t.Rectangle().change_color('purple')

    def test_rectangle_display_color(self):
        self.assertEqual(t.Rectangle('PURPLE').display_color(), 'Rectangle color PURPLE')

    def test_ractangle_araa(self):
        r = t.Rectangle('BLUE', 5.2, 7.2)
        self.assertAlmostEqual(37.44, r.area(), 2)  # Used for approximation, 2 decimal places, try with assertEqual

import unittest
import base_and_derived_class as t


class ShapeClassTest(unittest.TestCase):

    def setUp(self):
        self.shape = t.Shape()

    def tearDown(self):
        del self.shape

    def test_shape_initial_value_no_attributes(self):
        self.assertEqual(self.shape.color, 'BLUE')

    def test_shape_initial_value_optional_attributes(self):
        s = t.Shape('RED')  # local value used, not self.shape
        assert s.color == 'RED'

    def test_shape_ojbect_not_created_invalid_attributes(self):
        with self.assertRaises(t.InvalidColorError):
            s = t.Shape('blue')

    def test_shape_change_color_valid_attribute(self):
        self.shape.change_color('ORANGE')
        self.assertEqual(self.shape.color, 'ORANGE')

    def test_shape_change_color_invalid_attribute(self):
        s = t.Shape()
        with self.assertRaises(t.InvalidColorError):
            s.change_color('purple')

    def test_shape_str(self):
        self.assertEqual(t.Shape('PURPLE').display_color(), 'PURPLE')


if __name__ == '__main__':
    unittest.main()

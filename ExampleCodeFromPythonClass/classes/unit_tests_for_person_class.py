import unittest
from person_class import Person as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person = t('Duck', 'Daisy')

    def tearDown(self):
        del self.person

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.person.last_name, 'Duck')
        self.assertEqual(self.person.first_name, 'Daisy')

    def test_inital_all_attributes(self):
        person = t('Duck', 'Daisy', '111-11-1111') # this is not self.person from setUp, but local
        assert person.last_name == 'Duck'                 # note no self here on person or assert
        assert person.first_name == 'Daisy'
        assert person.ssn == '111-11-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t('123', 'Daisy')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t('Duck', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t('Duck', 'Daisy', 'abc')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.person), "Duck, Daisy:")   # Uses person from setUp()

    def test_person_class_display_name_ssn(self):
        p = t('Duck', 'Daisy', '111-11-1111')    # Does not use person from setUp(), has local p
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.person), 'Duck, Daisy:')

if __name__ == '__main__':
    unittest.main()

'''
assertEqual(a, b)	a == b
assertNotEqual(a,b)	a != b
assertTrue(x)	bool(x) is True
assertFalse(x)	bool(x) is False
assertIs(a, b)	a is b
assertIsNot(a,b)	a is not b
assertIsNone(x)	x is None
assertIsNotNone(x)	x is not None
assertIn(a, b)	a in b
assertNotIn(a, b)	a not in b
assertAlmostEqual(a, b)	round(a - b, 7) == 0
assertGreater(a, b)	a > b
assertGreaterEqual(a, b)	a >= b
assertLess(a, b)	a < b
assertLessEqual(a, b)	a <= b
'''

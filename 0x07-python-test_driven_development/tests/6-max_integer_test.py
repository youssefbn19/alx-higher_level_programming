"""
Module for testing max_integer using unittests Testing
"""

import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for testing function on "6-max_integr module"""
    def test_max_integer(self):
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([34, 42, 56, 1, 12]), 56)
        self.assertEqual(max_int("ALX"), 'X')
        with self.assertRaises(TypeError):
            max_int([34, 43, "alx school"])

"""
Module for Testing Base Class
"""
from models.base import Base
import unittest


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        """
        Preparing some Base class instances
        """
        self.b1 = Base()
        self.b2 = Base(18)

    def test_attribute_id(self):
        """
        Testing the Base id attribute
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 18)

"""
Module for Testing Square Class
"""
from models.square import Square
import unittest


class TestSquareClass(unittest.TestCase):
    def setUp(self):
        """
        Preparing some Square class instances
        """
        self.s1 = Square(6, 0, 0, 1)
        self.s2 = Square(4, 3, 2, 23)

    def test_square_attributes(self):
        """
        Testing the Square intances attributes
        """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.size, 6)
        self.assertEqual(self.s1.width, 6)
        self.assertEqual(self.s1.height, 6)

        self.assertEqual(self.s2.id, 23)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s2.width, 4)
        self.assertEqual(self.s2.height, 4)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s2.y, 2)

    def test_square_attributes_validation(self):
        """
        Testing attributes exceptions
        """
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.s1.size = '23'
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.s1.x = True
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.s1.y = 'Alx'

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.s1.size = -10
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.s1.x = -3
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.s1.y = -8

    def test_square_area(self):
        """
        Testing the are method of the class Square
        """
        self.assertEqual(self.s1.area(), 36)
        self.assertEqual(self.s2.area(), 16)

    def test_square_str(self):
        """
        Testing the __str__ method of the class Square
        """
        self.assertEqual(str(self.s1), "[square] (1) 0/0 - 6")
        self.assertEqual(str(self.s2), "[square] (23) 3/2 - 4")

    def test_square_update(self):
        """
        Testing the update method of the class Square
        """
        self.s1.update(89)
        self.assertEqual(self.s1.id, 89)
        self.s1.update(89, 2)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 2)
        self.s1.update(89, 2, 3)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 3)
        self.s1.update(89, 2, 3, 4)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 4)
        self.s2.update(size=2)
        self.assertEqual(self.s2.size, 2)
        self.s2.update(x=5, size=3)
        self.assertEqual(self.s2.x, 5)
        self.assertEqual(self.s2.size, 3)
        self.s2.update(y=1, x=3, size=8)
        self.assertEqual(self.s2.y, 1)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s2.size, 8)
        self.s2.update(1, 2, x=0, y=0)
        self.assertEqual(self.s2.id, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s2.y, 1)

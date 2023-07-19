"""
Module for Testing Rectangle Class
"""
from models.rectangle import Rectangle
import unittest


class TestRectangleClass(unittest.TestCase):
    def setUp(self):
        """
        Preparing some Rectangle class instances
        """
        self.r1 = Rectangle(10, 2, 0, 0, 1)
        self.r2 = Rectangle(8, 3, 2, 2, 16)

    def test_rectangle_attributes(self):
        """
        Testing the Rectangle intances attributes
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.id, 16)
        self.assertEqual(self.r2.width, 8)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 2)

    def test_rectangle_attributes_validation(self):
        """
        Testing attributes exceptions
        """
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.r1.width = '23'
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.r1.height = True
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.r1.x = None
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.r1.y = [3, 2, 1]

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.r1.width = -10
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            self.r1.height = 0

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.r1.x = -3
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.r1.y = -1

    def test_rectangle_area(self):
        """
        Testing the are method of the class Rectangle
        """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 24)
        self.r1.width = 4
        self.assertEqual(self.r1.area(), 8)

    def test_rectangle_str(self):
        """
        Testing the __str__ method of the class Rectangle
        """
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(self.r2), "[Rectangle] (16) 2/2 - 8/3")

    def test_rectangle_update(self):
        """
        Testing the update method of the class Rectangle
        """
        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)
        self.r1.update(89, 2)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.r1.update(89, 2, 3, 4)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)
        self.r2.update(height=6)
        self.assertEqual(self.r2.height, 6)
        self.r2.update(id=23)
        self.assertEqual(self.r2.id, 23)
        self.r2.update(width=2)
        self.assertEqual(self.r2.width, 2)
        self.r2.update(x=5)
        self.assertEqual(self.r2.x, 5)
        self.r2.update(y=1)
        self.assertEqual(self.r2.y, 1)

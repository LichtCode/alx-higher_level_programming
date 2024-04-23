#!/usr/bin/python3

"""Defines unittests for base.py."""
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect1))

    def test_create_rectangle_new(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect2))

    def test_create_rectangle_is(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equals(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertNotEqual(rect1, rect2)

    def test_create_square_original(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr1))

    def test_create_square_new(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sqr2))

    def test_create_square_is(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertIsNot(sqr1, sqr2)

    def test_create_square_equals(self):
        sqr1 = Square(3, 5, 1, 7)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertNotEqual(sqr1, sqr2)


if __name__ == "__main__":
    unittest.main()

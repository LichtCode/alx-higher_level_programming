#!/usr/bin/python3

"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sqr1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sqr2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        sqr1 = Square(5, 1, 3, 3)
        sqr2 = Square(9, 5, 2, 3)
        Square.save_to_file([sqr1, sqr2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()

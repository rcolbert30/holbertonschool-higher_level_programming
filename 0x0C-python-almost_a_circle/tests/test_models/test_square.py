#!/usr/bin/python3
"""Square Test Module"""
import sys
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_input(self):
        with self.assertRaises(ValueError):
            s = Square(0, 0)
        with self.assertRaises(ValueError):
            s = Square(13, 12, -69, -96)
        with self.assertRaises(TypeError):
            s = Square("1")
        with self.assertRaises(TypeError):
            s = Square(1, "2")
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(TypeError):
            s = Square(3, 6, 2.0, 5.0)
        with self.assertRaises(TypeError):
            s = Square("test", "this", 6.0, 7.5)
        with self.assertRaises(TypeError):
            s = Square(2.0, 6.7)

    def test_area(self):
        s = Square(10, 2)
        self.assertEqual(s.area(), 100)

    def test_str(self):
        r = Square(3, 6, 9, 12)
        self.assertEqual("[Square] (12) 6/9 - 3", str(r))

    def test_size(self):
        s = Square(5, 4, 3, 2)
        s.size = 69
        self.assertEqual(69, s.height)
        self.assertEqual(69, s.size)
        self.assertEqual(69, s.width)

    def test_size_2(self):
        s = Square(5, 0, 0, 2)
        with self.assertRaises(ValueError):
            s.size = 0
        s = Square(3, 6, 9, 12)
        with self.assertRaises(TypeError):
            s.size = 5.0
        with self.assertRaises(TypeError):
            s.size = "string"

    def test_to_dictionary(self):
        s = Square(3, 6, 9, 12)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict['id'], 12)
        self.assertEqual(s_dict['size'], 3)
        self.assertEqual(s_dict['x'], 6)
        self.assertEqual(s_dict['y'], 9)

    def test_square(self):
        s1 = Square(1, 2)
        self.assertEquals(s1.id, s1.id)

    def test_save_to_file(self):
        s2 = Square.save_to_file(None)
        self.assertEqual(s2, None)
        with self.assertRaises(TypeError):
            s2 = Square.save_to_file([])


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
            s = Square("test", "this")
        with self.assertRaises(TypeError):
            s = Square(3, 6, 2.0, 5.0)
        with self.assertRaises(TypeError):
            s = Square("test", "this", 6.0, 7.5)
        with self.assertRaises(TypeError):
            s = Square(2.0, 6.7)

    def test_area(self):
        s = Square(10, 2)
        self.assertEqual(s.area(), 20)

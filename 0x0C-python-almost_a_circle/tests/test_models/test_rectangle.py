#!/usr/bin/python3
"""Rectangle Test Module"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rec(self):
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_set(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_set_3(self):
        r = Rectangle(10, 2, 30)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 0)

    def test_set_4(self):
        r = Rectangle(10, 2, 30, 69)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 69)

if __name__ == '__main__':
    unittest.main()

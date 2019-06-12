#!/usr/bin/python3
"""Base Class Test Module"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_input(self):
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base("id")
        self.assertEqual(b2.id, "id")
        with self.assertRaises(TypeError):
            b3 = Base(1, 2)

if __name__ == '__main__':
    unittest.main()

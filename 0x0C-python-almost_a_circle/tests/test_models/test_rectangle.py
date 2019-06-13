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

    def test_id(self):
        '''testing id'''
        a = Rectangle(10, 2)
        a2 = Rectangle(2, 10)
        a3 = Rectangle(10, 20)
        self.assertEqual(a2.id + 1, a3.id)

    def test_set(self):
        a = Rectangle(10, 2)
        a2 = Rectangle(2, 10)
        a3 = Rectangle(10, 20)
        a4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(a2.id + 1, a3.id)
        self.assertEqual(12, a4.id)

    def test_set_3(self):
        with self.assertRaises(TypeError):
            x = Rectangle("try", "this")
        with self.assertRaises(TypeError):
            x = Rectangle(5.0, 4.0)
        with self.assertRaises(TypeError):
            x = Rectangle(5.0, 4.0, "try")
        with self.assertRaises(TypeError):
            x = Rectangle(10, 2, 5.0, 4.0)
        with self.assertRaises(TypeError):
            x = Rectangle(1.0, 2.0, 3.0, 4.0)

    def test_set_4(self):
        r = Rectangle(10, 2, 30)
        r.update(69)
        self.assertEqual(69, r.id)
        r.update(69, 6)
        self.assertEqual(6, r.width)
        r.update(69, 6, 7)
        self.assertEqual(7, r.height)
        r.update(69, 6, 7, 8,)
        self.assertEqual(8, r.x)
        r.update(69, 6, 7, 8, 9)
        self.assertEqual(9, r.y)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", str(r))

    def test_kwarg(self):
        r = Rectangle(30, 11, 35, 23, 6)
        r.update(69, id=6, width=9)
        self.assertEqual(69, r.id)

    def test_dict(self):
        r = Rectangle(31, 11, 35, 23, 6)
        r_dict = r.to_dictionary
        self.assertEqual(r_dict['id'], 6)
        self.assertEqual(r_dict['width'], 30)
        self.assertEqual(r_dict['height'], 11)
        self.assertEqual(r_dict['x'], 35)
        self.assertEqual(r_dict['y'], 23)

if __name__ == '__main__':
    unittest.main()

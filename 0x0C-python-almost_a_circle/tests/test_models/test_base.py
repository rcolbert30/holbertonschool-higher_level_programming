#!/usr/bin/python3

"""Base Class Test Module"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_a(self):
        b0 = Base(1)
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_b(self):
        b = Base()
        b2 = Base(30)
        b3 = Base(4)
        b4 = Base()
        self.assertEqual(4, b3.id)
        self.assertEqual(b.id + 1, b4.id)

    def test_from_json(self):
        j = Base.from_json_string("")
        self.assertEqual(len(j), 0)
        j = Base.from_json_string(None)
        self.assertEqual(len(j), 0)

    def test_to_json_string(self):
        r = Base.to_json_string(None)
        self.assertEqual(len(r), 0)
        r1 = Base.to_json_string([])
        self.assertEqual(len(r1), 0)

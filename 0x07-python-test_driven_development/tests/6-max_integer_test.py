#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    
    def test_max_integer_(self):
        self.assertEqual(max_int([]), None)

    def test_max_integer_neg(self):
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_int(test_list), 8)
    
    def test_max_integer(self):
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_int(test_list), 8)



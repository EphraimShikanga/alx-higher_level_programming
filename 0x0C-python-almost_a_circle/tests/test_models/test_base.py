#!usr/bin/python3

"""
Unittest for base model
"""

import unittest
from models import Base


class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)


if __name__ == '__main__':
    unittest.main()

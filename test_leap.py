import unittest
import pytest
import leap

class TestLeap(unittest.TestCase):
    def test1(self):
        self.assertEqual(leap.is_leap(2000), True)

    def test2(self):
        self.assertEqual(leap.is_leap(1900), False)

    def test3(self):
        self.assertEqual(leap.is_leap(4), True)

    def test4(self):
        self.assertEqual(leap.is_leap(2022), False)

    def test5(self):
        self.assertEqual(leap.is_leap(800), True)

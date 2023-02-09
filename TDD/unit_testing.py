#!/usr/bin/python3
"""Demo-ing unittesting in Python"""

import unittest

class TestStringMethods(unittest.TestCase):
    """Test case class"""
    def test_upper(self):
        """test string for uppercase"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """test string to see if its uppercase"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """test for string splitting"""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

a = [1, 2, 3]
print(type(a))
print(id(a))

a = 89
b = 89
print(a is b)
print(a == b)
print(type(a))
print(type(b))

a = 89
b = a
print(b)
print(a is b)
print(a == b)
print(id(a))
print(id(b))

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)
print(id(l1))
print(id(l2))

l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
print(l1 is l2)
l1.append(4)
print(l2)
l1 = l1 + [4]
print(l2)
print(l1)

def increment(n):
    n += 1

a = 1
print(increment(a))
print(a)

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

#!/usr/bin/python3
"""Unittest  module for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_empty_list(self):
        """Test for an empty list []"""
        self.assertEqual(max_integer([]), None)
    
    def test_no_args(self):
        """Tests for supplying no argument to function"""
        self.assertIsNone(max_integer())
    
    def test_list_with_one_integer(self):
        """Test for supplying only one number in list"""
        self.assertEqual(max_integer([1]), 1)
    
    def test_list_with_multiple_integers(self):
        """Tests for supplying multiple arguments"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
    
    def test_list_with_one_negative_integer(self):
        """Tests for one negative number in list"""
        self.assertEqual(max_integer([100, 50, 5, -7, 14, 60]), 200)
    
    def test_list_with_negative_integers(self):
        """Tests for supplying negative integers only"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)
    
    def test_list_with_positive_max_at_begin(self):
        """Tests for positive max integer at beginning of list"""
        self.assertEqual(max_integer([200, 10, 8, 36, 14, 50], 200))
    
    def test_list_with_positive_max_at_middle(self):
        """Tests for positive max integer in middle of list"""
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)
    
    def test_list_with_positive_max_at_end(self):
        """Tests for positive max integer at end of list"""
        self.assertEqual(max_integer([2, 10, 8, 36, 14, 50]), 50)
    
    def test_list_none_argument(self):
        """Test for supplying none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def test_list_with_non_integer_argument(self):
        """Tests for a type non-int in list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "Hello", 4, 5])

if __name__ == "__main__":
    unittest.main()
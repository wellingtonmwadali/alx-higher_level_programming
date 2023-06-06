#!/usr/bin/python3
"""Example of Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list."""
        ordered = [2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Test an unordered list."""
        unordered = [1, 5, 4, 3]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_begginning(self):
        """Test a list with a starting max value."""
        max_at_beginning = [5, 4, 3, 2]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a one element."""
        one_element = [8]
        self.assertEqual(max_integer(one_element), 8)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.43, 7.33, -8.123, 14.2, 5.0]
        self.assertEqual(max_integer(floats), 14.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.73, 14.5, -8, 13, 5]
        self.assertEqual(max_integer(ints_and_floats), 14.5)

    def test_string(self):
        """Test a string."""
        string = "tony"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["tony", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

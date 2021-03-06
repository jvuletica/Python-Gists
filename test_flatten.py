#! /usr/bin/env python3
import unittest, flatten_nested_array

class FlattenNestedArrayTests(unittest.TestCase):
    def setUp(self):
        nested_array = [1,2,[3,4,[5]],6]
        self.test_instance = second.FlattenNestedArray(nested_array)
    def test_flattenArrayResultType(self):
        flat_array = self.test_instance.flattenArray()
        assert type(flat_array) is list
    def test_flattenArrayResultElementsType(self):
        flat_array = self.test_instance.flattenArray()
        for element in flat_array:
            assert type(element) is int

if __name__ == "__main__":
    unittest.main()

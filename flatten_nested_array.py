#! /usr/bin/env python3
class FlattenNestedArray:
    def __init__(self, nested_array):
        self.nested_array = nested_array
    def flattenArray(self, nested_array = None, flat_array = []):
        if nested_array is None:
            nested_array = self.nested_array
        for element in nested_array:
            if type(element) is int:
                flat_array.append(element)
            elif type(element) is list:
                self.flattenArray(element, flat_array)
        #to ensure return on only first level of recursion
        if nested_array is self.nested_array:
            return flat_array

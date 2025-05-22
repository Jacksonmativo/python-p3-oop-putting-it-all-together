#!/usr/bin/env python3

# lib/shoe.py
class Shoe:
    def __init__(self, brand="Unknown", size=0):
        self._brand = brand
        self._size = size
        self._condition = None

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("brand must be a string")

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        self._condition = condition

    condition = property(get_condition, set_condition)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

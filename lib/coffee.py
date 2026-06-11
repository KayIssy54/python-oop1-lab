#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        valid_sizes = ["Small", "Medium", "Large"]

        if isinstance(size, str) and size.strip().capitalize() in valid_sizes:
            self.size = size.strip().capitalize()
        else:
            print("size must be Small, Medium, or Large")
            self.size = None

        self.price = price

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1
#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # validate size
        if size in ["Small", "Medium", "Large"]:
            self.size = size
        else:
            print("size must be Small, Medium, or Large")
            self.size = None

        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
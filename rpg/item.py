#!/usr/bin/env python3

"""
An item in a game with damage, magic, description, etc.
"""


class Item:

    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.magic = None
        self.properties = None
        self.location = None

    def getDescription(self):
        description = f"{self.name}: Damage = {self.damage}, Magic: {self.magic}, Properties: {self.properties}."
        return description

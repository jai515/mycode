#!/usr/bin/env python3

"""
Define a class called room to be used in a text based adventure game.
"""


class Room:

    def enter(self):
        print(self.description)

    def __init__(self, location):
        self.location = location
        self.moves = {
            'north': None,
            'east': None,
            'south': None,
            'west': None,
            'up': None,
            'Down': None
        }
        self.description = None
        self.contents = None

    def move(self, direction):
        if self.moves[direction] is None:
            print("You can't move that direction.")
            return False
        else:
            print(f'You move to the {direction}.')
            return self.moves[direction]

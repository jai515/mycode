#!/usr/bin/env python3
"""
Player for the rpg based game
"""


class Character:

    def getName(self):
        return self.name

    def getInventory(self):
        for item in self.inventory:
            print(item.getDescription())

    def getHealth(self):
        return self.health

    def getLocation(self):
        return self.location.enter()

    def __init__(self, name, location):
        self.name = name
        self.inventory = []
        self.health = 100
        self.location = location

    def move(self):
        response = False
        while response is False:
            move_direction = input("Where would you like to go? ").lower().strip()
            response = self.location.move(move_direction)
        self.location = response
        self.location.enter()

    def search(self):
        contents = self.location.contents
        if contents is not None:
            print(f"You found a {contents.getDescription()}")
            self.inventory.append(contents)
        else:
            print("There is nothing of value here")


    def get_action(self):
        print("You can enter: inventory, move, search")
        action = input("What do you want to do? ").lower().strip()
        if action == "move":
            self.move()
        elif action == 'search':
            self.search()
        elif action == 'inventory':
            print(f"Here is your inventory: ")
            self.getInventory()
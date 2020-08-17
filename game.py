#!/usr/bin/env python3

from rpg.item import Item
from rpg.room import Room
from rpg.character import Character

frontDoor = Room("Front Door")
frontDoor.description = "You stand in front of a door to a house. There is a courtyard behind you to the north."

hall = Room("Hall")
hall.description = "You are in a hallway. There are doors to the north, east, south and west."

courtyard = Room("Courtyard")
courtyard.description = "A pleasant courtyard with trees."
apples = Item("A delicious bushel of apples.")
apples.properties = "Delicious Fuji apples"
apples.damage = 1
apples.magic = "Restore 20 Health Points"


kitchen = Room("Kitchen")
kitchen.description = "A modern kitchen with kitchen things."

bedroom = Room("Bedroom")
bedroom.description = "A nice bedroom with bedroom things"

basement = Room("Basement")
basement.description = "A Basement. It's scary in here."

library = Room('Library')
library.description = "A library with books n' things."

courtyard.moves['south'] = frontDoor

frontDoor.moves['north'] = courtyard
frontDoor.moves['south'] = hall

hall.moves['north'] = frontDoor
hall.moves['south'] = library
hall.moves['east'] = kitchen
hall.moves['west'] = bedroom
hall.moves['down'] = basement

kitchen.moves['west'] = hall
sword = Item("Sword of Pointiness")
sword.properties = "Very pointy"
sword.damage = 100
kitchen.contents = sword

bedroom.moves['east'] = hall

library.moves['north'] = hall


playerOne = Character("One", frontDoor)
goblin = Character("Goblin", hall)

playerOne.getLocation()
while playerOne.health > 0:
    playerOne.get_action()


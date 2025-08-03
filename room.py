# Group:
# Who worked on this class:

import random

class Room:
    """Represents different locations in the your world"""
    
    def __init__(self, name, description):
        """Required attributes, as well as any additional ones"""
        ### YOUR CODE HERE ###
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.npcs = []
        self.visited = False

    
    def describe(self):
        """Display room description and contents (items, NPCs)"""
        ### YOUR CODE HERE ###

    
    def add_item(self, item):
        """Add an item to the room"""
        ### YOUR CODE HERE ###

    
    def remove_item(self, item_name):
        """Remove an item from the room"""
        ### YOUR CODE HERE ###

    
    def get_exit(self, direction):
        """Return the room connected in that direction"""
        ### YOUR CODE HERE ###

    
    def add_npc(self, npc):
        """Add an NPC to this room"""
        ### YOUR CODE HERE ###
        
# Group: 
# Who worked on this class:

import random

class NPC:
    """Represents non-player characters"""
    
    def __init__(self, name, description):
        """Required attributes, as well as any additional ones"""
        ### YOUR CODE HERE ###
        self.name = name
        self.description = description
        self.location = None
        self.dialogue = {
            "greeting": f"Hello, traveler! I am {name}",
            "farewell": "Safe travels!",
            "quest": "I need help with a task.",
            "item": "I have something for you."
        }
        self.inventory = []
        self.friendly = True
    
    def talk(self, topic="greeting"):
        """Return dialogue response based on topic"""
        ### YOUR CODE HERE ###
        return self.dialogue.get(topic, self.dialogue["greeting"])

    def give_item(self, item_name):
        """Give an item to the player"""
        ### YOUR CODE HERE ###
    
    def describe(self):
        """Return NPC's appearance"""
        ### YOUR CODE HERE ###
        return f"{self.name} is {self.description}"

    def interact(self):
        """Main method for player-NPC interaction"""
        ### YOUR CODE HERE ###
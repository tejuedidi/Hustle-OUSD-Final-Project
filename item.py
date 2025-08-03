# Group: 
# Who worked on this class:

import random

class Item:
    """Represents objects players can interact with"""
    
    def __init__(self, name, description, usable=True):
        """Required attributes, as well as any additional ones"""
        ### YOUR CODE HERE ###
        self.name = name
        self.description = description
        self.usable = usable

    
    def use(self):
        """What happens when the item is used"""
        ### YOUR CODE HERE ###
        return f"You used {self.name}."

    
    def examine(self):
        """Detailed description when player examines item"""
        ### YOUR CODE HERE
        return f"Examining... This is: {self.description}"

# if __name__ == "__main__":
#     # init testing
#     item = Item("Magic Wand", "A wand that casts spells.")
#     print("Testing item name:", item.name)
#     print("Testing item description:", item.description)
#     print("Testing item usability:", item.usable)

#     print("Testing item use:", item.use())
#     print("Testing item examination:", item.examine())
#     print("All tests passed!")
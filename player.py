# Group:
# Who worked on this class:

import random
from item import Item

class Player:
    """Represents the player character."""
    
    def __init__(self, name):
        """Required attributes, as well as any additional ones"""
        ### YOUR CODE HERE ###
        #required attributes
        self.name = name
        self.current_location = None
        self.health = 100
        self.inventory = []
       
        
    def move(self, direction):
        """Move to a different room"""
        ### YOUR CODE HERE ###

    
    def take_item(self, item_name):
        """Add an item to inventory"""
        ### YOUR CODE HERE ###

    
    def use_item(self, item_name):
        """Use an item from inventory"""
        ### YOUR CODE HERE ###
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.usable:
                    result = item.use()
                    if "consumed" in result.lower():
                        self.inventory.remove(item)
                    return result
                else:
                    return f"You can't use {item.name} right now."
        return f"You don't have {item_name} in your inventory."

    
    def display_status(self):
        """Show player's current status"""
        ### YOUR CODE HERE ###
        status = f"\n=== {self.name}'s Status ===\n"
        status += f"Location: {self.current_location}\n"
        status += f"Energy: {self.health}/100\n"
        
        if self.inventory:
            status += f"Inventory: {', '.join([item.name for item in self.inventory])}\n"
        else:
            status += "Inventory: Empty\n"
            
        return status

# if __name__ == "__main__":
#     # create player and item
#     player = Player("SpiderMan")
#     web_shooter = Item("Web Shooter", "A device that shoots webs.", usable=True)

#     # testing player attributes
#     print("Testing player name:", player.name)
#     print("Testing player energy:", player.health)

#     player.current_location = "New York City"
#     player.inventory.append(web_shooter)
#     print("Testing player location:", player.current_location)
#     for i in player.inventory:
#         print("Testing player inventory:", i.name)

#     # testing player methods
#     print("Testing player status display:", player.display_status())
#     print("Testing item use:", player.use_item("Web Shooter"))
#     print("Testing item take:", player.take_item("Web Shooter"))
#     print("Testing item use not in inventory:", player.use_item("climbing gear"))
#     print("All tests passed!")

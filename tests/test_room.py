import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from room import Room

@pytest.fixture
def room():
    r = Room("Sorcery Room", "Room to cast spells.")
    r.exits = {
        "north": "Library",
        "south": "Dungeon",
        "east": "Alchemy Lab",
        "west": "Hall of Mirrors"
    }
    r.items = ["Magic Wand", "Spell Book"]
    r.npcs = ["Wizard", "Ghost"]
    r.visited = True
    return r

def test_room_name(room):
    print("\n == Room Name:", room.name)
    assert room.name == "Sorcery Room"

def test_room_description(room):
    print("== Room Description:", room.description)
    assert room.description == "Room to cast spells."

def test_room_exits(room):
    print("== Room Exits:", room.exits)
    assert room.exits == {
        "north": "Library",
        "south": "Dungeon",
        "east": "Alchemy Lab",
        "west": "Hall of Mirrors"
    }

def test_room_items(room):
    print("== Room Items:", room.items)
    assert "Magic Wand" in room.items
    assert "Spell Book" in room.items

def test_room_npcs(room):
    print("== Room NPCs:", room.npcs)
    assert "Wizard" in room.npcs
    assert "Ghost" in room.npcs 

def test_room_visited(room):
    print("== Room Visited:", room.visited)
    assert room.visited is True


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from npc import NPC

@pytest.fixture
def npc():
    non_impt = NPC("Teju", "A techincal instructor that haunts students.")
    non_impt.location = "behind you"
    non_impt.dialogue = {
            "greeting": f"Hello, traveler! I am {non_impt.name}",
            "farewell": "Safe travels!",
            "quest": "I need help with a task.",
            "item": "I have something for you."
        }
    non_impt.inventory = ["laptop", "notebook"]
    non_impt.friendly = False
    return non_impt

def test_npc_name(npc):
    print("\n == NPC Name:", npc.name)
    assert npc.name == "Teju"

def test_npc_description(npc):
    print("== NPC Description:", npc.description)
    assert npc.description == "A techincal instructor that haunts students."

def test_npc_location(npc):
    print("== Where is Teju?:", npc.location)
    assert npc.location == "behind you"

def test_npc_dialogue(npc):
    print("== Dialogue Test:", npc.dialogue["item"])
    assert npc.dialogue["item"] == "I have something for you."

def test_npc_friendly(npc):
    print("== Is Teju friendly?:", npc.friendly)
    assert npc.friendly is False

def test_npc_talk(npc):
    print("== NPC Talk Test:", npc.talk("greeting"))
    assert npc.talk("greeting") == "Hello, traveler! I am Teju"
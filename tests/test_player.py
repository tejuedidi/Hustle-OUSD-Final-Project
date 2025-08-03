import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from player import Player
from item import Item

@pytest.fixture
def player():
    p = Player("Sydney")
    p.current_location = "LA"
    p.health = 350
    p.inventory.append(Item("Web Shooter", "A device that shoots webs.", usable=True))
    p.inventory.append(Item("Ammo", "Ammo for a weapon.", usable=True))
    return p

def test_player_name(player):
    print("\n == Player Name:", player.name)
    assert player.name == "Sydney"

def test_player_location(player):
    print("== Player Location:", player.current_location)
    assert player.current_location == "LA"

def test_player_health(player):
    print("== What is player's health:", player.health)
    assert player.health == 350

def test_display(player):
    print("== Player Status Display:", player.display_status())

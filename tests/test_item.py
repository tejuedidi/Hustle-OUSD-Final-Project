import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from item import Item

@pytest.fixture
def item():
    return Item("Magic Wand", "A wand that casts spells.", usable=True)

def test_item_name(item):
    print("\n == Item Name:", item.name)
    assert item.name == "Magic Wand"

def test_item_description(item):
    print("== Item Description:", item.description)
    assert item.description == "A wand that casts spells."

def test_item_usability(item):
    print("== Is the item usable (t or f):", item.usable)
    assert item.usable is True

def test_item_use(item):
    result = item.use()
    print("== Using item test:", result)
    assert "You used Magic Wand." in result

def test_item_examine(item):
    result = item.examine()
    print("== Examining item test:", result)
    assert "Examining... This is: A wand that casts spells." in result

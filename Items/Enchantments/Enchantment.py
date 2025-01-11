from ..Item import Item
from ..Tags import *

class Enchantment(Item):
    """
        Enchantments are like Spells or Abilities
        but can only be used outside the battle.
        They can only affect any other type of item.
    """
    
    tags = {ENCHANTMENT}


from random import randint

from .Armor import Armor

class Shoes(Armor):
    LIFE_PER_LEVEL = 110
    PROTECTION_PER_LEVEL = 4
    DAMAGE_PART = 1.1

    def __init__(self, owner, level:int=None, life:int=None, protection:int=None):
        self.name = "Shoes armor"

        super().__init__(owner, owner.level if level is None else level, life, protection)
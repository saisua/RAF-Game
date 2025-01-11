from .Armor import Armor
from ..Tags import *

class Chest(Armor):
    LIFE_PER_LEVEL = 100
    PROTECTION_PER_LEVEL = 5
    DAMAGE_PART = 1.2

    def __init__(self, owner=None, level:int=None, life:int=None, protection:int=None):
        self.name = "Chest armor"

        super().__init__(owner, owner.level if level is None else level, life, protection)

        
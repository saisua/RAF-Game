from random import randint

from .Armor import Armor
from ..Tags import *

class Shield(Armor):
    LIFE_PER_LEVEL = 80
    PROTECTION_PER_LEVEL = 4
    DAMAGE_PART = 0.7

    def __init__(self, owner=None, level:int=None, life:int=None, protection:int=None):
        self.name = "Shield"

        super().__init__(owner, owner.level if level is None else level, life, protection)
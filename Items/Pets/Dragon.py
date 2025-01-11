from random import randint

from .Pet import Pet
from ..Tags import *

class Dragon(Pet):
    LIFE_PER_LEVEL = 30
    DAMAGE_PER_LEVEL = 20
    PROTECTION_PER_LEVEL = 15
     
    tags:set = (Pet.tags |
            {OFFENSIVE, DEFENSIVE, SLOW,
            RANGED, ADAPTIVE}
        )

    MIN_SPEED:int = 10
    MAX_SPEED:int = 15

    MIN_ATTACKSPEED:int = 5
    MAX_ATTACKSPEED:int = 10

    def __init__(self, owner, level:int=None, life:int=None, damage:int=None):
        self.name = "dragon"
        self.attack_form = "distance"

        super().__init__(owner, owner.level if level is None else level, life, damage)


    def new_positioning(self):
        return "back" if randint(0,2) else "next" if randint(0,1) else "front"
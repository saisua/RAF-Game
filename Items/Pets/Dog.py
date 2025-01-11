from random import randint

from .Pet import Pet
from ..Tags import *

class Dog(Pet):
    LIFE_PER_LEVEL = 40
    DAMAGE_PER_LEVEL = 15
    PROTECTION_PER_LEVEL = 15
     
    tags:set = (Pet.tags |
            {OFFENSIVE, DEFENSIVE,
            PHYSICAL, MELEE, ADAPTIVE}
        )

    MIN_SPEED:int = 15
    MAX_SPEED:int = 25

    MIN_ATTACKSPEED:int = 10
    MAX_ATTACKSPEED:int = 25

    def __init__(self, owner, level:int=None, life:int=None, damage:int=None):
        self.name = "dog"
        self.attack_form = "melee"

        super().__init__(owner, owner.level if level is None else level, life, damage)


    def new_positioning(self):
        return "next" if randint(0,10) else "front"
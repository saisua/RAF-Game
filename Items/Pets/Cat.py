from random import randint

from .Pet import Pet
from ..Tags import *

class Cat(Pet):
    LIFE_PER_LEVEL = 25
    DAMAGE_PER_LEVEL = 10
    PROTECTION_PER_LEVEL = 10
     
    tags:set = (Pet.tags |
            {OFFENSIVE, FAST, PHYSICAL,
            MELEE, ADAPTIVE}
        )

    MIN_SPEED:int = 25
    MAX_SPEED:int = 35

    MIN_ATTACKSPEED:int = 25
    MAX_ATTACKSPEED:int = 35

    MIN_EVASION:int=10
    MAX_EVASION:int=30

    def __init__(self, owner, level:int=None, life:int=None, damage:int=None):
        self.name = "cat"
        self.attack_form = "melee"
        
        super().__init__(owner, owner.level if level is None else level, life, damage)

    def new_positioning(self):
        return "back" if randint(0,10) else "next"
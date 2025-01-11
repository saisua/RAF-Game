from random import randint

from .Pet import Pet
from ..Tags import *

class Turtle(Pet):
    LIFE_PER_LEVEL = 80
    DAMAGE_PER_LEVEL = 10
    PROTECTION_PER_LEVEL = 15
     
    tags:set = (Pet.tags |
            {DEFENSIVE, MELEE, PHYSICAL,
            SLOW, HEAVY, ADAPTIVE}
        )

    MIN_SPEED:int = 10
    MAX_SPEED:int = 15

    MIN_ATTACKSPEED:int = 5
    MAX_ATTACKSPEED:int = 10

    def __init__(self, owner, level:int=None, life:int=None, damage:int=None):
        self.name = "turtle"
        self.attack_form = "melee"

        super().__init__(owner, owner.level if level is None else level, life, damage)


    def new_positioning(self):
        return "front" if randint(0,10) else "next" 
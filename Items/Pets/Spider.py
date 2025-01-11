from random import randint

from .Pet import Pet
from ..Effects.Effect import Effect
from ..Effects.Poison import Poison
from ..Tags import *

class Spider(Pet):
    LIFE_PER_LEVEL = 1
    DAMAGE_PER_LEVEL = 10
    PROTECTION_PER_LEVEL = 10

    tags:set = (Pet.tags |
            {OFFENSIVE, MELEE, PHYSICAL,
            SLOW, STATUS}
        )

    PROB_POISON = 4 # 1/value
    MAX_POISON_TURNS = 3

    MIN_SPEED:int = 0
    MAX_SPEED:int = 0

    MIN_ATTACKSPEED:int = 5
    MAX_ATTACKSPEED:int = 10

    MIN_PRECISSION = 90
    MAX_PRECISSION = 100

    def __init__(self, owner, level:int=None, life:int=None, damage:int=None):
        self.name = "spider"
        self.attack_form = "melee"
        self.positioning = "back"

        super().__init__(owner, owner.level if level is None else level, life, damage)

    def attack(self, enemy, *, can_call=None):
        if(not randint(0, self.PROB_POISON)):
            enemy.add_effect(Poison(
                max_damage=self.strength//2,
                min_damage=self.level
                ))

        return super().attack(enemy)
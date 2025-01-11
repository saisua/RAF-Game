from random import randint

from .Spell import Spell
from ..Tags import *

class Ice(Spell):
    tags:set = (Spell.tags |
            {OFFENSIVE, STATUS}
        )

    MIN_DAMAGE:int = 10
    MAX_DAMAGE:int = 30

    MIN_MAGIC:int = 10
    MAX_MAGIC:int = 25

    MAX_TARGETS:int = 1

    FREEZE_PROBABILITY = 10 # 1/value
    FREEZE_MAX_TURNS = 3

    def __init__(self, owner=None, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Ice"
        super().__init__(owner, damage, magic, targets, attack_form)

    def attack(self, enemy, attack_to, combatter):
        after = ''
        if(not randint(0,self.FREEZE_PROBABILITY)):
            frozen_turns = randint(1, self.FREEZE_MAX_TURNS)
            enemy.add_cc(frozen_turns, "frozen", 
                            f"for {frozen_turns} turns because of {self.owner.name}'s spell")


        return super().attack(enemy, attack_to, combatter, after=after)
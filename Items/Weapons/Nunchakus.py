from random import randint

from .Weapon import Weapon
from ..Tags import *

class Nunchakus(Weapon):
    LIFE_PER_LEVEL:int=25
    DAMAGE_PER_LEVEL:int=50

    tags:set = (Weapon.tags |
            {MELEE, FAST, LIGHT, PHYSICAL}
        )

    MAX_TARGETS:int=1

    MAX_CHARGES:int=15

    MAX_HITS:int=1

    def __init__(self, owner=None, level:int=None, damage:int=None, life:int=None):
        self.name = "Nunchakus"
        self.attack_form = "melee"
        self.reload_turns = 0

        targets = 1
        charges = 10

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life, targets, charges)

    def attack(self, enemy, attack_to, combatter):
        
        super().attack(enemy, attack_to, combatter)

        if(len(enemy.held_items) and randint(0,100) < combatter.attributes.knock):
            weapon = enemy.held_items.pop(randint(0,len(enemy.held_items)-1))

            print(f"\n {enemy.name} also dropped his {weapon.name}!")
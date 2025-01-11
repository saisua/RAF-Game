from .Weapon import Weapon
from ..Tags import *

class Dagger(Weapon):
    LIFE_PER_LEVEL:int=30
    DAMAGE_PER_LEVEL:int=15

    tags:set = (Weapon.tags |
            {MELEE, FAST, LIGHT, PHYSICAL, MULTI_ATTACK}
        )

    MAX_TARGETS:int=1

    MAX_CHARGES:int=30

    MAX_HITS:int=3

    def __init__(self, owner=None, level:int=None, damage:int=None, life:int=None):
        self.name = "Dagger"
        self.attack_form = "melee"
        self.reload_turns = 0

        targets = 1
        charges = 10

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life, targets, charges)
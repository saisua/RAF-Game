from .Weapon import Weapon
from ..Tags import *

class Spear(Weapon):
    LIFE_PER_LEVEL:int=25
    DAMAGE_PER_LEVEL:int=35

    tags:set = (Weapon.tags |
            {MELEE, RANGED, PHYSICAL, LIGHT, ADAPTIVE, MULTI_ATTACK}
        )

    MAX_TARGETS:int=1

    MAX_CHARGES:int=10

    MAX_HITS:int=2

    def __init__(self, owner=None, level:int=None, damage:int=None, life:int=None):
        self.name = "Spear"
        self.attack_form = "any"
        self.reload_turns = 0

        targets = 1
        charges = 10

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life, targets, charges)
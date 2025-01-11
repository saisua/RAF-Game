from .Weapon import Weapon
from ..Tags import *

class Wand(Weapon):
    LIFE_PER_LEVEL:int=25
    DAMAGE_PER_LEVEL:int=35

    tags:set = (Weapon.tags |
            {RANGED, LIGHT, MAGICAL, MULTI_TARGET}
        )

    MAX_TARGETS:int=3

    MAX_CHARGES:int=4

    MAX_HITS:int=1

    def __init__(self, owner=None, level:int=None, damage:int=None, life:int=None):
        self.name = "Wand"
        self.attack_form = "any"
        self.reload_turns = 0

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life)
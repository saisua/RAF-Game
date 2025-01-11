from .Weapon import Weapon
from ..Tags import *

class Bow(Weapon):
    LIFE_PER_LEVEL:int=50
    DAMAGE_PER_LEVEL:int=45

    tags:set = (Weapon.tags |
            {RANGED, PHYSICAL, MULTI_TARGET, LIGHT}
        )

    MAX_TARGETS:int=2

    MAX_CHARGES:int=10

    MAX_HITS:int=1

    def __init__(self, owner=None, level:int=None, damage:int=None, life:int=None):
        self.name = "Bow"
        self.attack_form = "distance"
        self.reload_turns = 0

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life)
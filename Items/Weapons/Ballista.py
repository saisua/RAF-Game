from .Weapon import Weapon
from ..Tags import *

class Ballista(Weapon):
    LIFE_PER_LEVEL:int=50
    DAMAGE_PER_LEVEL:int=65

    tags:set = (Weapon.tags |
            {RANGED, PHYSICAL, MULTI_TARGET, HEAVY, MULTI_ATTACK}
        )

    MAX_TARGETS:int=2

    MAX_CHARGES:int=10

    MAX_HITS:int=2

    def __init__(self, owner=None, level:int=None, damage:int=None, life:int=None):
        self.name = "Ballista"
        self.attack_form = "distance"
        self.reload_turns = 1

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life)
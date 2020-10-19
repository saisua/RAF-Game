from .Weapon import Weapon

class Bow(Weapon):
    LIFE_PER_LEVEL:int=50
    DAMAGE_PER_LEVEL:int=45

    MAX_TARGETS:int=2

    MAX_CHARGES:int=10

    MAX_HITS:int=1

    def __init__(self, owner, level:int=None, damage:int=None, life:int=None):
        self.name = "Bow"
        self.attack_form = "distance"
        self.reload_turns = 0

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life)
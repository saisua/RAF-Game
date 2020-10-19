from .Weapon import Weapon

class Sword(Weapon):
    LIFE_PER_LEVEL:int=30
    DAMAGE_PER_LEVEL:int=45

    MAX_TARGETS:int=1

    MAX_CHARGES:int=10

    MAX_HITS:int=1

    def __init__(self, owner, level:int=None, damage:int=None, life:int=None):
        self.name = "Sword"
        self.attack_form = "melee"
        self.reload_turns = 0

        targets = 1
        charges = 10

        super().__init__(owner, owner.level if level is None else level, damage, 
                        life, targets, charges)
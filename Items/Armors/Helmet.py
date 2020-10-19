from random import randint

from .Armor import Armor

class Helmet(Armor):
    LIFE_PER_LEVEL = 100
    PROTECTION_PER_LEVEL = 4
    DAMAGE_PART = 1.5

    def __init__(self, owner, level:int=None, life:int=None, protection:int=None):
        self.name = "Helmet armor"

        super().__init__(owner, owner.level if level is None else level, life, protection)

    def receive_hit(self, combatter, damage, attacker):
        result = super().receive_hit(combatter, damage, attacker)

        if(randint(0,100) < attacker.attributes.stun):
            combatter.add_cc(1, "stunned")

        return result
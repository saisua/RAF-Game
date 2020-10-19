from random import randint

from .Armor import Armor

class Gloves(Armor):
    LIFE_PER_LEVEL = 60
    PROTECTION_PER_LEVEL = 2
    DAMAGE_PART = 1.1

    def __init__(self, owner, level:int=None, life:int=None, protection:int=None):
        self.name = "Gloves armor"

        super().__init__(owner, owner.level if level is None else level, life, protection)

    def receive_hit(self, combatter, damage, attacker):
        after = ''
        if(len(combatter.held_items) and randint(0,100) < attacker.attributes.knock):
            weapon = combatter.held_items.pop(randint(0,len(combatter.held_items)-1))

            after = f"\n {self.owner.name} also dropped his {weapon.name}!"

        return super().receive_hit(combatter, damage, attacker)
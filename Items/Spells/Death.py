from .Spell import Spell
from ..Tags import *

class Death(Spell):
    tags = (Spell.tags |
            {OFFENSIVE}
        )
    MIN_DAMAGE:int = 10
    MAX_DAMAGE:int = 20

    MIN_MAGIC:int = 20
    MAX_MAGIC:int = 30

    MAX_TARGETS:int = 1

    def __init__(self, owner=None, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Death"
        super().__init__(owner, damage, magic, targets, attack_form)

    def attack(self, enemy, attack_to, combatter, after='', attack=True):
        p = True
        for e in enemy.combat.participants[enemy.team_name]:
            if(not super().attack(e, attack_to, combatter, after=after, attack=attack, once=p)):
                print(f"{self.owner.name} missed the spell!")
            p = False

        return True
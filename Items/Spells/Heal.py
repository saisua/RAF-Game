from random import choice

from .Spell import Spell
from ..Tags import *

class Heal(Spell):
    tags:set = (Spell.tags |
            {DEFENSIVE, HEALING}
        )
    MIN_DAMAGE:int = 10
    MAX_DAMAGE:int = 30

    MIN_MAGIC:int = 30
    MAX_MAGIC:int = 50

    MAX_TARGETS:int = 1

    def __init__(self, owner=None, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Life"
        super().__init__(owner, damage, magic, targets, attack_form)

    def attack(self, enemy, attack_to, combatter, after=''):
        ally = choice(combatter.combat.participants[combatter.team_name])

        healing_life = self.damage+combatter.attributes.magic_strength
        ally_life = ally._static.attributes.life - ally.attributes.life

        if(not ally_life): return False

        after = f"{self.owner.name} healed {ally.name} ({ally.life}hp -> "
        ally.attributes.life += healing_life if healing_life < ally_life else ally_life
        after += f"{ally.life}hp)"

        return super().attack(ally, attack_to, combatter, after=after, attack=False)
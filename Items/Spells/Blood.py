from random import randint

from .Spell import Spell
from ..Tags import *

class Blood(Spell):
    tags:set = (Spell.tags |
            {OFFENSIVE, HEALING, ABSORPTION}
        )

    MIN_DAMAGE:int = 10
    MAX_DAMAGE:int = 20

    MIN_MAGIC:int = 10
    MAX_MAGIC:int = 30

    MIN_ABSORB:int = 3 # value/10
    MAX_ABSORB:int = 10 # value/10

    MAX_TARGETS:int = 1

    absortion:float

    def __init__(self, owner=None, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Blood"
        self.absortion = randint(self.MIN_ABSORB, self.MAX_ABSORB) / 10

        super().__init__(owner, damage, magic, targets, attack_form)

        self.quality = self._qualities[int(((self.damage*self.targets)+
                        (self.MAX_MAGIC-self.magic-self.MIN_MAGIC))
                        * (self.absortion*10/self.MAX_ABSORB)
                        * (len(self._qualities)-1)
                        / (1+self.MAX_DAMAGE*self.MAX_TARGETS+(self.MAX_MAGIC-self.MIN_MAGIC)))]

    def attack(self, enemy, attack_to, combatter, after='', attack=True, once=True):
        enemy_lost_hp = enemy.attributes.life
        if(not super().attack(enemy, attack_to, combatter, after=after, attack=attack, once=once)):
            return False
        enemy_lost_hp -=  enemy.attributes.life if enemy.attributes.life > 0 else 0

        enemy_lost_hp *= self.absortion

        print(f"{self.owner.name} soaked {combatter.name} ({combatter.life}hp -> ", end='')
        combatter_life = combatter._static.attributes.life - combatter.attributes.life
        combatter.attributes.life += enemy_lost_hp if enemy_lost_hp < combatter_life else combatter_life
        print(f"{combatter.life}hp)")
        return True

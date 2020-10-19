from random import randint

from .Pet import Pet
from ..Effects.Effect import Effect

class Spider(Pet):
    LIFE_PER_LEVEL = 1
    DAMAGE_PER_LEVEL = 10
    PROTECTION_PER_LEVEL = 10

    PROB_POISON = 4 # 1/value
    MAX_POISON_TURNS = 3

    MIN_SPEED:int = 0
    MAX_SPEED:int = 0

    MIN_ATTACKSPEED:int = 5
    MAX_ATTACKSPEED:int = 10

    MIN_PRECISSION = 90
    MAX_PRECISSION = 100

    def __init__(self, owner, level:int=None, life:int=None, damage:int=None):
        self.name = "spider"
        self.attack_form = "melee"
        self.positioning = "back"

        super().__init__(owner, owner.level if level is None else level, life, damage)

        self.poison_damage = randint(1, self.strength//2)

    def attack(self, enemy, *, can_call=None):
        return super().attack(enemy)

        if(not randint(0, self.PROB_POISON)):
            enemy.add_effect(Effect(self.name, [self.each_turn], [{}], 
                    self.start, self.end, randint(1, self.MAX_POISON_TURNS)))


    def each_turn(self, combatter):
        print(f"{combatter.name} got hurt by poison ({combatter.life} -> ", end='')
        combatter.attributes.life -= self.poison_damage
        print(f"{combatter.life})")

    def start(self, combatter):
        print(f"{combatter.name} got poisoned!")
        self.each_turn(combatter)

    def end(self, combatter):
        print(f"{combatter.name} has recovered from the poison")
from .Spell import Spell
from ..Tags import *

class Wind(Spell):
    tags:set = (Spell.tags |
            {OFFENSIVE}
        )

    MIN_DAMAGE:int = 10
    MAX_DAMAGE:int = 20

    MIN_MAGIC:int = 10
    MAX_MAGIC:int = 20

    MAX_TARGETS:int = 1

    def __init__(self, owner=None, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Wind"
        super().__init__(owner, damage, magic, targets, attack_form)
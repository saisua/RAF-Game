from .Spell import Spell
from ..Tags import *

class Fire(Spell):
    tags = (Spell.tags |
            {OFFENSIVE}
        )

    MIN_DAMAGE:int = 20
    MAX_DAMAGE:int = 30

    MIN_MAGIC:int = 20
    MAX_MAGIC:int = 30

    MAX_TARGETS:int = 1

    def __init__(self, owner=None, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Fire"
        super().__init__(owner, damage, magic, targets, attack_form)
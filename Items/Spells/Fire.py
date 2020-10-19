from .Spell import Spell

class Fire(Spell):
    MIN_DAMAGE:int = 20
    MAX_DAMAGE:int = 30

    MIN_MAGIC:int = 20
    MAX_MAGIC:int = 30

    MAX_TARGETS:int = 1

    def __init__(self, owner, damage=None, magic=None, 
                        targets:int=None, attack_form:str=None):
        self.element = "Fire"
        super().__init__(owner, damage, magic, targets, attack_form)
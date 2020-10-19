from random import choice

from .Ballista import Ballista
from .Bow import Bow
from .Dagger import Dagger
from .Hammer import Hammer
from .Nunchakus import Nunchakus
from .Spear import Spear
from .Sword import Sword
from .Wand import Wand

_by_name_melee = {
    "Dagger":Dagger, 
    "Hammer":Hammer, 
    "Nunchakus":Nunchakus, 
    "Spear":Spear, 
    "Sword":Sword
}

_by_name_distance = {
    "Ballista":Ballista, 
    "Bow":Bow, 
    "Wand":Wand
}

_by_name = {**_by_name_melee, **_by_name_distance}

def Random_weapon(owner:"Character", name:str=None):
        return _by_name.get(name, choice(list(_by_name.values()))
                )(owner, owner.level)

def Random_melee_weapon(owner:"Character", name:str=None):
        return _by_name_melee.get(name, choice(list(_by_name_melee.values()))
                )(owner, owner.level)

def Random_distance_weapon(owner:"Character", name:str=None):
        return _by_name_distance.get(name, choice(list(_by_name_distance.values()))
                )(owner, owner.level)
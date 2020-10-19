from random import choice

from .Fire import Fire
from .Ice import Ice
from .Wind import Wind
from .Heal import Heal
from .Death import Death
from .Blood import Blood

_by_name = {
    "Fire":Fire, 
    "Ice":Ice, 
    "Wind":Wind,
    "Heal":Heal,
    "Death":Death,
    "Blood":Blood
}

def Random_spell(owner:"Character", name:str=None):
    return _by_name.get(name, choice(list(_by_name.values()))
            )(owner)

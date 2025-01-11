from random import choice

from .Sharpen import Sharpen

_by_name = {
    "Sharpen":Sharpen
}

def Random_enchantment(owner:"Character", name:str=None):
    return _by_name.get(name, choice(list(_by_name.values()))
            )(owner, owner.level)

from random import choice

from .Attack_speed import Attack_speed
from .Defense import Defense
from .Evasion import Evasion
from .Magic import Magic
from .Regenerate import Regenerate
from .Double_turn import Double_turn
from .Strength import Strength

_by_name = {
    "Attack_speed":Attack_speed,
    "Defense":Defense,
    "Evasion":Evasion,
    "Magic":Magic,
    "Regenerate":Regenerate,
    "Double_turn":Double_turn,
    "Strength":Strength
}

def Random_ability(owner:"Character", name:str=None):
    return _by_name.get(name, choice(list(_by_name.values()))
            )(owner, owner.level)

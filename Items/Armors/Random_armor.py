from random import choice

from .Chest import Chest
from .Gloves import Gloves
from .Helmet import Helmet
from .Shield import Shield
from .Shoes import Shoes
from .Trousers import Trousers

_by_name = {
    "Chest":Chest, 
    "Gloves":Gloves, 
    "Helmet":Helmet, 
    "Shield":Shield, 
    "Shoes":Shoes, 
    "Trousers":Trousers
}

armor_types = len(_by_name)
    
def Random_armor(owner:"Character", name:str=None):
        return _by_name.get(name, choice(list(_by_name.values()))
                )(owner, owner.level)
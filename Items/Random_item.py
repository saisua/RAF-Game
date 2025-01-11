from random import choice

from utils.dict_flatten import flatten

"""
from .Armors.Random_armor import Random_armor, _by_name as armors
from .Pets.Random_pet import Random_pet, _by_name as pets
from .Weapons.Random_weapon import Random_weapon, _by_name as weapons
from .Spells.Random_spell import Random_spell, _by_name as spells
from .Abilities.Random_ability import Random_ability, _by_name as abilities
from .Enchantments.Random_enchantment import Random_enchantment, _by_name as enchantments
"""
from .Armors import Random_armor as Rar
from .Pets import Random_pet as Rp
from .Weapons import Random_weapon as Rw
from .Spells import Random_spell as Rs
from .Abilities import Random_ability as Rab
from .Enchantments import Random_enchantment as Re

_by_name = {
    "Armor":Rar.Random_armor,
    "Pet":Rp.Random_pet,
    "Weapon":Rw.Random_weapon,
    "Spell":Rs.Random_spell,
    "Ability":Rab.Random_ability,
    "Enchantment":Re.Random_enchantment
}

_groups = {
    "Armor":Rar._by_name,
    "Pet":Rp._by_name,
    "Weapon":Rw._by_name,
    "Spell":Rs._by_name,
    "Ability":Rab._by_name,
    "Enchantment":Re._by_name
}

_all = flatten(_groups)

"""
from .Armors.Armor import Dummy as Dummy_armor
from .Pets.Pet import Dummy as Dummy_pet
from .Weapons.Weapon import Dummy as Dummy_weapon
from .Spells.Spell import Dummy as Dummy_spell
from .Abilities.Ability import Dummy as Dummy_ability

_dummies = {
    "Armor":Dummy_armor,
    "Pet":Dummy_pet,
    "Weapon":Dummy_weapon,
    "Spell":Dummy_spell,
    "Ability":Dummy_ability
}
"""

def Random_item(owner:"Character", name:str=None):
        return _by_name.get(name, choice(list(_by_name.values()))
                )(owner, owner.level)
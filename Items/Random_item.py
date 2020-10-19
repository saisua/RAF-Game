from random import choice

from .Armors.Random_armor import Random_armor, _by_name as armors
from .Pets.Random_pet import Random_pet, _by_name as pets
from .Weapons.Random_weapon import Random_weapon, _by_name as weapons
from .Spells.Random_spell import Random_spell, _by_name as spells
from .Abilities.Random_ability import Random_ability, _by_name as abilities


_by_name = {
    "Armor":Random_armor,
    "Pet":Random_pet,
    "Weapon":Random_weapon,
    "Spell":Random_spell,
    "Ability":Random_ability
}

_groups = {
    "Armor":armors,
    "Pet":pets,
    "Weapon":weapons,
    "Spell":spells,
    "Ability":abilities
}

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
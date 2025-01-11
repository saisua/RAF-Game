
from Items.Tags import MELEE, OFFENSIVE, PHYSICAL
from .Enchantment import Enchantment

class Sharpen(Enchantment):
    tags = (Enchantment.tags |
        {OFFENSIVE, MELEE, PHYSICAL}
    )
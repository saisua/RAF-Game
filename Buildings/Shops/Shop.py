from typing import Callable
from typing import Callable

from ..Building import Building


class Shop(Building):
    refill:Callable

    # Shops are specialized based of
    # their own probabilities +
    # the earnings per item class


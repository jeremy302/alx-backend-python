#!/usr/bin/env python3
''' TODO project doc later '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' TODO project doc later '''
    return lambda x: x * multiplier

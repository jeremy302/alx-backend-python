#!/usr/bin/env python3
''' 8-make_multiplier.py '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(v: float) -> float:
        return v * multiplier
    return multiply

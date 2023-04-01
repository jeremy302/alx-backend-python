#!/usr/bin/env python3
''' 7-to_kv.py '''
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    ''' sample procedure '''
    return (k, v**2)

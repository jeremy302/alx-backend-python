#!/usr/bin/env python3
''' TODO project doc later '''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' TODO project doc later '''
    return (k, float(v**2))

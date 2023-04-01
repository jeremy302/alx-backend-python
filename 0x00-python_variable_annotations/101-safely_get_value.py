#!/usr/bin/env python3
''' safely_get_value.py '''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
DType = Union[T | None]
RType = T | Any


def safely_get_value(dct: Mapping, key: Any, default: DType = None) -> RType:
    ''' safely gets value '''
    if key in dct:
        return dct[key]
    else:
        return default

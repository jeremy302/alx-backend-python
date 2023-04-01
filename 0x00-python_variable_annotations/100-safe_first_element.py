#!/usr/bin/env python3
''' 100-safe_first_element.py '''
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence) -> Any | None:
    ''' get's the first element in a sequence '''
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
''' TODO project doc later '''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' TODO project doc later '''
    return [(i, len(i)) for i in lst]

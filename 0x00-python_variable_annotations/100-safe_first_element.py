#!/usr/bin/env python3
''' TODO project doc later '''
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' get's the first element in a sequence '''
    if lst:
        return lst[0]
    else:
        return None

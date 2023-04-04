#!/usr/bin/env python3
''' async comprehension '''
import random
import asyncio
from typing import Any, List

async_generator: Any = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' async comprehension '''
    return [i async for i in async_generator()]

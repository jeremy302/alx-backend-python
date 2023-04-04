#!/usr/bin/env python3
''' async generator '''
import random
import asyncio
from typing import Any


async def async_generator() -> Any:
    ''' async generator '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

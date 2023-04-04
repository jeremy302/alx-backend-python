#!/usr/bin/env python3
''' measure runtime '''
import random
import asyncio
from typing import Any, List
import time

async_comprehension: Any = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure runtime '''
    tasks: List[asyncio.Task] = [
        asyncio.create_task(async_comprehension()) for i in range(4)]
    t: float = time.perf_counter()
    await asyncio.gather(*tasks)
    return time.perf_counter() - t

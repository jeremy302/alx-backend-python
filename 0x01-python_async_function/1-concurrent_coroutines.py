#!/usr/bin/env python3
''' wait_n module '''
import asyncio
from typing import List, Callable, Any

wait_random: Callable[[int], Any] = __import__(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' spaws `n` wait_random(max_delay), and returns the delays'''
    delays: List[float] = []
    tasks: List[asyncio.Task] = [
        asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    for delay in asyncio.as_completed(tasks):
        delays.append(await delay)
    return delays

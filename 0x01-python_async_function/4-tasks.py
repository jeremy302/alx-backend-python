#!/usr/bin/env python3
''' measure_time module '''
import asyncio
from typing import List, Callable, Any

task_wait_random: Callable[[int], asyncio.Task] = __import__(
    '3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    ''' spaws `n` wait_random(max_delay), and returns the delays'''
    delays: List[float] = []
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for i in range(n)]
    for delay in asyncio.as_completed(tasks):
        delays.append(await delay)
    return delays

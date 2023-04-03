#!/usr/bin/env python3
''' wait_random module '''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' waits a random amount of time '''
    duration: float = random.random() * max_delay
    await asyncio.sleep(duration)
    return duration

#!/usr/bin/env python3
''' wait_random module '''
import asyncio
import random


async def wait_random(max_delay=10):
    ''' waits a random amount of time '''
    duration = random.random() * max_delay
    await asyncio.sleep(duration)
    return duration

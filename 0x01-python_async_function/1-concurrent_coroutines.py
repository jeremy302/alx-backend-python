#!/usr/bin/env python3
''' wait_n module '''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    ''' spaws `n` wait_random(max_delay), and returns the delays'''
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    for delay in asyncio.as_completed(tasks):
        delays.append(await delay)
    return delays

#!/usr/bin/env python3
''' measure_time module '''
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    ''' spaws `n` wait_random(max_delay), and returns the delays'''
    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for delay in asyncio.as_completed(tasks):
        delays.append(await delay)
    return delays

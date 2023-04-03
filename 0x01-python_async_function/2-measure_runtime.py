#!/usr/bin/env python3
''' measure_time module '''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    t = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - t)/n

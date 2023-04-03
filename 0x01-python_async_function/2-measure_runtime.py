#!/usr/bin/env python3
''' measure_time module '''
import asyncio
import time
from typing import List, Callable, Any

wait_n: Callable[[int, int], Any] = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    t: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - t)/n

#!/usr/bin/env python3
''' task_wait_random module '''
import asyncio
import time
from typing import List, Callable, Any

wait_random: Callable[[int], Any] = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' creates a task '''
    return asyncio.create_task(wait_random(max_delay))

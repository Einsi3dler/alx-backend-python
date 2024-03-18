#!/usr/bin/env python3
"""
This module contains an async function
that returns a sorted list of random delays.

Functions
    task_wait_n(n: int, max_delay: int) -> list:
        Takes in two integers, n and max_delay, and returns
        a sorted list of n random delays between 0 and max_delay.
"""

import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes in two integers, n and max_delay,
    and returns a sorted list of n random delays between 0 and max_delay.

    Args:
        n (int): The number of random delays to generate.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        List[float]: A sorted list of n random
        delays between 0 and max_delay.
    """
    resArr = []
    for val in range(n):
        bisect.insort(resArr, await wait_random(max_delay))
    task_wait_random(max_delay)
    return resArr

#!/usr/bin/env python3
"""
This module contains an asynchronous function 'wait_n'
that takes in two arguments:
n: an integer that represents the number of times
'wait_random' function will be called
max_delay: an integer that represents the maximum value of
the delay (inclusive) for each 'wait_random' call.
The function returns a sorted list of delays in ascending order.
"""
import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Documentation for method
    """
    resArr = []
    y = 0
    while y < n:
        bisect.insort(resArr, await wait_random(max_delay))
        y = y + 1
    return resArr

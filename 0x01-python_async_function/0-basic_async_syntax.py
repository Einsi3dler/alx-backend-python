#!/usr/bin/env python3

import asyncio
import random

"""
This module contains an asynchronous coroutine that
waits for a random delay between 0 and max_delay seconds,
then returns the delay time as a float.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds,
    then returns the delay time as a float.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The actual number of seconds waited.
    """
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return (val)

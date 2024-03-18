#!/usr/bin/env python3
import asyncio
import random

"""
This Module contains a function that runs afer a random time
with the default set at 10
"""


async def wait_random(max_delay: int = 10) -> int:
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return (val)

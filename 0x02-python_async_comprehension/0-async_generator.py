#!/usr/bin/env python3
import asyncio
import random

"""
This module contains an async generator that yields random float values
between 0 and 10 with a 1 second delay between each yield.
"""

async def async_generator():
    """
    An async generator that yields random float values between 0 and 10
    with a 1 second delay between each yield.
    """
    for i in range(10):
        val = random.uniform(0, 10)
        yield(val)
        await asyncio.sleep(1)
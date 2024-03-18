#!/usr/bin/env python3
"""
Module for creating asyncio tasks.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task that waits for a random amount of time.

    Args:
        max_delay (int): The maximum amount of time to wait.

    Returns:
        An asyncio task that waits for a random amount of time.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))

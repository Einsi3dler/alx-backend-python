#!/usr/bin/env python3
"""
Module for measuring the average runtime of a coroutine.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of a coroutine.

    Args:
        n (int): The number of times to run the coroutine.
        max_delay (int): The maximum delay for each individual coroutine.

    Returns:
        float: The average runtime of the coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return (execution_time/n)

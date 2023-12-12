import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    This function measures the runtime of four calls to async_comprehension() using asyncio.gather().

    Returns:
        float: The execution time of the four calls to async_comprehension() in seconds.
    """
    start_time = time.perf_counter()
    res1, res2, res3, res4 = await asyncio.gather(async_comprehension(),async_comprehension(),async_comprehension(),async_comprehension())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time
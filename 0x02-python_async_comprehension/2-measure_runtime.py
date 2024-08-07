#!/usr/bin/env python3
'''Module that defines functions to run async comprehensions and measure runtime.

This module includes:
- `async_comprehension`: A coroutine to collect 10 random numbers.
- `measure_runtime`: A coroutine to measure the runtime of running `async_comprehension`
  four times in parallel.
'''

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    '''Measures the total runtime of executing async_comprehension four times in parallel.

    The function calculates the total time taken to execute four instances of the
    `async_comprehension` coroutine concurrently using `asyncio.gather`.

    Returns:
        float: The total runtime in seconds.
    '''
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    # Calculate and return the total runtime
    return end_time - start_time

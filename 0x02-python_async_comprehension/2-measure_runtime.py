#!/usr/bin/env python3
'''Module that defines a coroutine to measure runtime of parallel async tasks.
'''

import asyncio
import time
from previous_module import async_comprehension  # Replace 'previous_module' with the actual filename

async def measure_runtime() -> float:
    '''Measures the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    '''
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    # Calculate and return the total runtime
    return end_time - start_time

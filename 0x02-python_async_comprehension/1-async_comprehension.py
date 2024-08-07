#!/usr/bin/env python3
'''Module that defines a coroutine to collect values from an async generator.
'''

from typing import List
from previous_module import async_generator  # Replace 'previous_module' with the actual filename

async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers collected from async_generator.
    '''
    # Collect 10 random numbers from async_generator using async comprehension
    return [number async for number in async_generator()]

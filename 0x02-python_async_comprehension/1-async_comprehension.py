#!/usr/bin/env python3
'''Module that defines a coroutine to collect values from an async generator.

This module includes:
- `async_comprehension`: A coroutine to collect 10 random numbers
  from `async_generator`.
'''

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehension over async_generator.

    The coroutine uses an asynchronous comprehension to collect 10 random numbers
    generated by `async_generator`, and returns them as a list.

    Returns:
        List[float]: A list of 10 random numbers collected from async_generator.
    '''
    return [number async for number in async_generator()]

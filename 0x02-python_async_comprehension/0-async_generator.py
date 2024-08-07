#!/usr/bin/env python3
'''Module that defines an asynchronous generator coroutine.

This module includes:
- `async_generator`: A coroutine that yields 10 random numbers,
  each after waiting for 1 second.
'''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Yields a sequence of random numbers asynchronously.

    The coroutine will loop 10 times. Each time, it will asynchronously wait for
    1 second and then yield a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


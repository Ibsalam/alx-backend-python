#!/usr/bin/env python3
'''Module that defines an async generator coroutine.
'''

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    '''Asynchronously generates a sequence of random numbers.

    The coroutine will loop 10 times, each time asynchronously waiting for 1 second,
    and then yielding a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    '''
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)

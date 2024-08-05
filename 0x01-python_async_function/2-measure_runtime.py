#!/usr/bin/env python3
'''Module that defines a function to measure the runtime of wait_n.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Make an asynchronous task for wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))

#!/usr/bin/env python3
"""
Module description: This module defines
a coroutine async_generator that yields random numbers.
"""

import asyncio
import random


async def async_generator() -> int:
    """
    Coroutine that generates random numbers asynchronously.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

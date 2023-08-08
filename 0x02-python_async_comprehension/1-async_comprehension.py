#!/usr/bin/env python3
"""
Module description: This module defines a coroutine
async_comprehension that collects random numbers.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers asynchronously
    using async comprehension.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [number async for number in async_generator()]

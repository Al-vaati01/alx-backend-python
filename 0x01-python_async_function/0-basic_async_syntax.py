#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) that waits for a random delay between 0
and max_delay (inclusive and float value) seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that simulates a random delay and returns the delay time.

    Args:
        max_delay (int): The maximum delay time in seconds (default is 10).

    Returns:
        float: The random delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

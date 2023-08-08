#!/usr/bin/env python3
"""
This module defines an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
It spawns wait_random n times with the specified max_delay.
"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay time for wait_random.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    values: List[float] = []

    for _ in range(n):
        values.append(await wait_random(max_delay))

    for i in range(1, len(values)):
        key: float = values[i]
        j: int = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key

    return values

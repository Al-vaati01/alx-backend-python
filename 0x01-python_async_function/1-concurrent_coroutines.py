#!/usr/bin/env python3
"""
an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified
max_delay.
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    wait_n that takes in 2 int arguments
    return the list of all the delays (float values).
    """

    values: list[float] = []
    i: int
    for i in range(n):
        values.append(await wait_random(max_delay))

    for i in range(1, len(values)):
        key: float = values[i]
        j: int = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values

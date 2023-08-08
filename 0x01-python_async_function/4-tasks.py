#!/usr/bin/env python3
"""
a new function task_wait_n.
task_wait_random is being called.
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random(max_delay) n times with
    specified max_delay which is a task.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay time for wait_random.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    values: List[float] = []

    for _ in range(n):
        values.append(await task_wait_random(max_delay))

    for i in range(1, len(values)):
        key: float = values[i]
        j: int = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key

    return values

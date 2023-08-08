#!/usr/bin/env python3
"""
Module description: This module defines a function task_wait_random that takes an integer
max_delay and returns an asyncio.Task.
"""

import asyncio

random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        asyncio.Task: An asyncio Task that runs the wait_random coroutine.
    """
    return asyncio.create_task(random(max_delay))

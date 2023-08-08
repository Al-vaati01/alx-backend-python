#!/usr/bin/env python3
"""
Module description: This module defines a coroutine
measure_runtime that measures the total runtime.
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime

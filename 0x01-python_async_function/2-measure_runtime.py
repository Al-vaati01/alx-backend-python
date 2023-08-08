#!/usr/bin/env python3
"""
Function with integers n and max_delay as arguments
that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay time for wait_n.

    Returns:
        float: Average execution time per call to wait_n.
    """
    start_time = time.time()

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(wait_n(n, max_delay))
    event_loop.close()

    finish_time = time.time()
    total_time = finish_time - start_time

    return total_time / n

#!/usr/bin/env python3

"""
A function to calculate the floor value of a float number.
"""

import math


def floor(n: float) -> int:
    """
    floor: A function to calculate the floor value of a float number.

    Args:
        n (float): The input float number.

    Returns:
        int: The floor value of the input number.
    """
    fl: int = math.floor(n)
    return fl

#!/usr/bin/env python3
import math
"""
floor: A function to calculate the floor value of a float number.
"""


def floor(n: float) -> int:
    """
    Returns the floor of a float number.

    Args:
    n (float): The input float number.

    Returns:
    float: The floor value of the input number.
    """
    fl: int = math.floor(n)
    return fl

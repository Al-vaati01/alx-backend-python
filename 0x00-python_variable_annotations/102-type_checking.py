#!/usr/bin/env python3
"""
type-annotated function zoom_array that takes a tuple
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    A function that zooms in on the input tuple by repeating
    each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The zoom factor. Default is 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: List[int] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array: List[int] = (12, 72, 91)
zoom_2x: List[int] = zoom_array(array)
zoom_3x: List[int] = zoom_array(array, 3)

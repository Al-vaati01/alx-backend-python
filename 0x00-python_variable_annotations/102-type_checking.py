#!/usr/bin/env python3
"""
type-annotated function zoom_array that takes a tuple
"""
from typing import List, Tuple


def zoom_array(lst: Tuple,
               factor: int = 2
               ) -> List:
    """
    takes a tuple lst and returns a tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3.0)

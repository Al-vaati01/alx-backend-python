#!/usr/bin/env python3
"""
type-annotated function zoom_array that takes a tuple
"""
from typing import Iterable, SupportsInt, Union


def zoom_array(lst: Iterable[SupportsInt],
               factor: Union[SupportsInt, float] = 2
               ) -> Iterable[SupportsInt]:
    """
    takes a tuple lst and returns a tuple
    """
    zoomed_in: Iterable[SupportsInt] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

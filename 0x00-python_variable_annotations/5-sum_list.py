#!/usr/bin/env python3

"""
A type-annotated function sum_list which takes a list input_list of floats
as an argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as an argument and returns their
    sum as a float.
    """
    _sum: float = 0
    for i in input_list:
        _sum += i
    return _sum

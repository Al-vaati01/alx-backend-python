#!/usr/bin/env python3
"""
a type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    _sum: float = 0
    for i in input_list:
        _sum += i
    return _sum

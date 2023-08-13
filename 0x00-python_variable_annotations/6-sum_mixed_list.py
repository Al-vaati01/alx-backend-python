#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    _sum: float = 0
    for i in mxd_lst:
        _sum += i
    return _sum

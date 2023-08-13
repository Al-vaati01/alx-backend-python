#!/usr/bin/env python3
"""
function type annotations
"""
from typing import Any, Mapping, Union, TypeVar, Optional

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default=Union[T, Optional]) -> Union[Any, T]:
    """The types of the elements"""
    if key in dct:
        return dct[key]
    else:
        return default

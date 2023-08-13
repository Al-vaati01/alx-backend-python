#!/usr/bin/env python3
"""
function annotations
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    advanced annotations
    """
    return [(i, len(i)) for i in lst]

#!/usr/bin/python3
from typing import Sequence, Union, Any
# The types of the elements


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
"""
Parameterized a unit test
"""


import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import List, Dict, Any


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict[str, Any],
            path: List[str],
            expected_result: Any
    ) -> None:
        """ Test access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()

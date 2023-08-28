#!/usr/bin/env python3
"""
Parameterized a unit test
"""


import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import List, Dict, Any

from utils import get_json
from unittest.mock import patch


class TestGetJson(unittest.TestCase):
    """ TestGetJson Class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict[str, bool]
    ) -> None:
        """ Test get json """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict[str, Any],
            path: List[str],
            expected_result: Any
    ) -> None:
        """ Test access nested map exception """
        with self.assertRaises(expected_result):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()

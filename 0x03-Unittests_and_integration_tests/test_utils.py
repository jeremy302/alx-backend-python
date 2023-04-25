#!/usr/bin/env python3
''' test utils '''
from typing import Any, Dict, Tuple, Union


import unittest
from unittest.mock import Mock

import requests

from parameterized import parameterized

import utils
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    ''' tests `access_nested_map` '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str], val: Union[Dict, int]) -> None:
        ''' test `access_nested_map`'''
        self.assertEqual(utils.access_nested_map(nested_map, path), val)

    @parameterized.expand([
        ("", {}, ("a",)),
        ("", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, _: str, nested_map: Dict,
                                         path: Any) -> None:
        ''' test `access_nested_map` exception '''
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' tests `get_json` '''
    @parameterized.expand([
        ("", "http://example.com", {"payload": True}),
        ("", "http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, _, test_url: str, test_payload: Dict) -> None:
        ''' tests `get_json` '''
        mock = Mock()
        mock.json = Mock(return_value=test_payload)
        with unittest.mock.patch('requests.get',
                                 Mock(return_value=mock)) as req:
            self.assertEqual(utils.get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    ''' tests `memoize()` '''

    def test_memoize(self) -> None:
        ''' test `memoize()` '''
        class TestClass:
            def a_method(self) -> int:
                return 42

            @utils.memoize
            def a_property(self) -> int:
                return self.a_method()
        mock = Mock(return_value=42)
        obj = TestClass()
        with unittest.mock.patch.object(obj, 'a_method', mock) as proc:
            self.assertEqual(obj.a_property, 42)
            proc.assert_called_once()
            self.assertEqual(obj.a_property, 42)
            proc.assert_called_once()

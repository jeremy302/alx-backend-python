#!/usr/bin/env python3
''' test client '''
from typing import Dict

import unittest
from unittest import mock
from unittest.mock import Mock, PropertyMock, patch

import requests

from parameterized import parameterized, parameterized_class

import utils
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    ''' test github org client '''

    @parameterized.expand([
        ('google', {'foo': 'bar'}),
        ('abc', {'bar': 'foo'})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, org_res: Dict, proc) -> None:
        ''' test org '''
        proc.return_value = org_res
        obj = client.GithubOrgClient(org_name)
        org = obj.org
        proc.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        org = obj.org
        proc.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(org, org_res)

    def test_public_repos_url(self) -> None:
        ''' test public repos url '''
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as prop:
            prop.return_value = {'foo': 'bar', 'repos_url': 'abc123'}
            obj = client.GithubOrgClient('foo')
            self.assertEqual(obj._public_repos_url, 'abc123')

    @patch('client.get_json')
    def test_public_repos(self, proc: Mock) -> None:
        ''' test public repos '''
        url = 'http://foo.bar'
        proc.return_value = [{'name': 'foo'}, {'name': 'bar'}]

        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=PropertyMock) as prop:
            prop.return_value = url
            obj = client.GithubOrgClient('abc')
            self.assertEqual(obj.public_repos(), ['foo', 'bar'])
            proc.assert_called_once_with(url)
            prop.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict,
                         license_key: str, res: bool) -> None:
        ''' test has license '''
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, license_key), res)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     [
                         (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
                          TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])
                     ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    ''' test integration github org client '''

    @classmethod
    def setUpClass(cls) -> None:
        ''' tests preparation '''
        endpoints = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def json(url) -> Mock:
            m = Mock()
            m.json = Mock(return_value=endpoints.get(url, None))
            return m
        cls.get_patcher = patch('requests.get', side_effect=json)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        ''' tests cleanup'''
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        ''' test public repos '''
        obj = client.GithubOrgClient('google')
        self.assertEqual(obj.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        ''' test public repo with license '''
        obj = client.GithubOrgClient('google')
        self.assertEqual(
            obj.public_repos(license="apache-2.0"), self.apache2_repos)

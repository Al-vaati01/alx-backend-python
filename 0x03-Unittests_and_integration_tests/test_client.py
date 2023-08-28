#!/usr/bin/env python3
"""A GitHub org client"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from requests import HTTPError
from client import GithubOrgClient
from typing import Any, Dict


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Any) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name))

    def test_public_repos_url(self) -> None:
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "World"}
            mock_org.return_value = payload
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url,
                             payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Any) -> None:
        """Test that the list of repos is what you expect from the chosen
        payload.
        Test that the mocked property and the mocked get_json was called once
        """
        payload = [{"name": "Youtube"}, {"name": "Google"}]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/"
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["Youtube", "Google"])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, True),
        ({'license': {'key': 'other_license'}}, True),
    ])
    def test_has_license(self, repo: Dict[str, Any],
                         expected_return: bool) -> None:
        """Test that the result of has_license is the expected one based on
        the mocked payload.
        Test that the mocked get_json was called once
        """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.has_license(repo), expected_return)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient"""
    @parameterized.expand([
        ("org_payload",),
        ("repo_payload",),
        ("expected_repos",),
        ("apache2_repos",),
    ])
    # setupClass
    @classmethod
    def setUpClass(cls) -> None:
        """set up class"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    # tearDownClass
    @classmethod
    def tearDownClass(cls) -> None:
        """tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test that GithubOrgClient.public_repos returns the correct list of
        repos
        """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), [])
        self.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

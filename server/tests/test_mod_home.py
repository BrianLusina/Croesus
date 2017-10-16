"""
Tests for home module. Tests that this module handles responses as expected
"""
import unittest
from tests import BaseTestCase
from app.__meta__ import __project__, __version__,__copyright__

import json


class HomeTestCases(BaseTestCase):
    """
    Test cases for home module. This is the entry point of the application
    Normally will not be hit by the client, but will serve information regarding the server
    that is currently running.
    """
    def test_home_route_can_be_reached(self):
        response = self.client.get("/", follow_redirects=True)
        self.assert200(response)

    def test_home_route_returns_api_info(self):
        response = self.client.get("/home", follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)
        self.assertIsInstance(data["version"], str)
        self.assertIsInstance(data["project"], str)
        self.assertEqual(data["version"], __version__)
        self.assertEqual(data["project"], __project__)
        self.assertEqual(data["copyright"], __copyright__)


if __name__ == '__main__':
    unittest.main()

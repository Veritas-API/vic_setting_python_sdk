# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """ SettingsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.settings_api.SettingsApi()

    def tearDown(self):
        pass

    def test_get_settings(self):
        """
        Test case for get_settings

        Get settings
        """
        pass


if __name__ == '__main__':
    unittest.main()

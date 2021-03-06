"""Note: Suggested as pre-commit hook, to block credentials being published."""

import unittest

from openVulnQuery import config

CLIENT_ID = ''
CLIENT_SECRET = ''
REQUEST_TOKEN_URL = "https://cloudsso.cisco.com/as/token.oauth2"
API_URL = "https://api.cisco.com/security/advisories"


class ConfigTest(unittest.TestCase):
    def test_config_api_reference_ok(self):
        self.assertEqual(config.API_URL, API_URL)

    def test_config_token_reference_ok(self):
        self.assertEqual(config.REQUEST_TOKEN_URL, REQUEST_TOKEN_URL)

    def test_config_client_id_empty(self):
        self.assertEqual(config.CLIENT_ID, CLIENT_ID)

    def test_config_client_secret_empty(self):
        self.assertEqual(config.CLIENT_SECRET, CLIENT_SECRET)

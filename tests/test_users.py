import unittest
import sys  # fix import errors
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.base_config_tests import ConfigTestCase


class UserEndpoint(ConfigTestCase):
    """This class represents user test cases"""

    def test_change_username(self):
        """Test API can change username"""
        username = {"username": "admin2"}
        res = self.client().put('/api/v3/auth/user/test_user@gmail.com', data=json.dumps(username),
                                headers=self.user_header, content_type='application/json')
        self.assertIn("username changed", str(res.data))

    def test_reset_password(self):
        """Test API can change password"""
        password = {"password": "admin2018"}
        res = self.client().put('/api/v3/auth/user/test_user@gmail.com', data=json.dumps(password),
                                headers=self.user_header, content_type='application/json')
        self.assertIn("password changed!", str(res.data))

        # invalid email
        res1 = self.client().put('/api/v3/auth/user/chris_user@gmail.com', data=json.dumps(password),
                                 headers=self.user_header, content_type='application/json')
        self.assertIn("Email is not available", str(res1.data))



if __name__ == '__main__':
    unittest.main()

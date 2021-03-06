import unittest
import sys  # fix import errors
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.base_config_tests import ConfigTestCase

class SignUpEndpoint(ConfigTestCase):
    """This class represents sign up test case"""

    def test_successful_sign_up(self):
        """Test API can register user successfully"""

        user = {"username": 'teddy', "email": 'teddy@gmail.com', "password": '123456789'}

        response = self.client().post('/api/v3/register', data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("You have been successfully added", str(response.data))

    def test_successful_driver_sign_up(self):
        """Test API can register driver successful"""

        driver = {"username": 'Mark', "email": 'mark@gmail.com', "password": '123456789', "is_driver": "True"}
        driver_response = self.client().post('/api/v3/register', data=json.dumps(driver), content_type='application/json')
        self.assertEqual(driver_response.status_code, 201)
        self.assertIn("You have been successfully added", str(driver_response.data))

    def test_empty_field(self):
        """Test API for empty field"""

        user = {"username": '', "email": 'teddy@gmail.com', "password": '123456789'}
        response = self.client().post('/api/v3/register', data=json.dumps(user), content_type='application/json')
        self.assertIn("Field cannot be empty", str(response.data))

    def test_available_email(self):
        """Test API can detect"""
        user = {"username": "driver", "email": "test_driver@gmail.com", "password": '123456789'}
        response = self.client().post('/api/v3/register', data=json.dumps(user), content_type='application/json')
        self.assertIn("email already exist", str(response.data))


if __name__ == '__main__':
    unittest.main()
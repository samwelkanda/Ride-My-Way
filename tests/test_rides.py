import unittest
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.base_config_tests import ConfigTestCase

class RidesEndpoint(ConfigTestCase):
    """This class represents rides test cases"""

    def test_get_all_rides(self):
        """Test API can get all rides"""

        res = self.client().get('/api/v1/rides')
        self.assertEqual(res.status_code, 200)
        self.assertIn("Syokimau - Nairobi", str(res.data))

    def test_get_ride(self):
        """Test API can get a ride"""

        res = self.client().get('/api/v1/rides/1', headers=self.user_header)
        self.assertEqual(res.status_code, 200)
        self.assertIn("Syokimau - Nairobi", str(res.data))

    def test_get_invalid_ride(self):
        """Test API for invalid ride"""

        res = self.client().get('/api/v1/rides/105', headers=self.user_header)
        self.assertIn("invalid ride_id", str(res.data))

        res_del = self.client().delete('/api/v1/driver/rides/100')
        self.assertIn("invalid ride_id", str(res_del.data))



    def test_request_ride(self):
        """Test API can request a ride"""

        res = self.client().patch('/api/v1/users/rides/1/request', headers=self.user_header)
        self.assertIn("You have successfully requested a ride", str(res.data))
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
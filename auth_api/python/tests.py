import unittest
from methods import Token, Restricted
from api import app
import json

class TestTokenMethods(unittest.TestCase):

    def setUp(self):
        self.token = Token()

    def test_generate_token_valid(self):
        # Test a valid login request
        self.assertEqual(self.token.generate_token('admin', 'secret'), 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiJ9.bWUzyXuV7BpUTbL00D7anm_2GmV0rJ_Yzkg0fJ1C_bM')

    def test_generate_token_invalid(self):
        # Test an invalid login request
        with self.assertRaises(ValueError):
            self.token.generate_token('admin', 'invalid')

    def test_generate_token_missing_username(self):
        # Test a missing username in login request
        with self.assertRaises(TypeError):
            self.token.generate_token(password='secret')

    def test_generate_token_missing_password(self):
        # Test a missing password in login request
        with self.assertRaises(TypeError):
            self.token.generate_token(username='admin')


class TestRestrictedMethods(unittest.TestCase):

    def setUp(self):
        self.restricted = Restricted()

    def test_access_data_valid(self):
        # Test a valid JWT token
        auth_token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiJ9.bWUzyXuV7BpUTbL00D7anm_2GmV0rJ_Yzkg0fJ1C_bM'
        self.assertEqual(self.restricted.access_data(auth_token), 'You are under protected data')

    def test_access_data_missing_token(self):
        # Test missing JWT token
        with self.assertRaises(ValueError):
            self.restricted.access_data(None)

    def test_access_data_invalid_token(self):
        # Test an invalid JWT token
        with self.assertRaises(ValueError):
            self.restricted.access_data('Bearer invalid_token')


if __name__ == '__main__':
    unittest.main()

import json
import unittest

from flask_api.exceptions import AuthenticationFailed
from flask_login import current_user
from app.mod_auth.exceptions import UserAlreadyExists, CredentialsRequired
from tests import BaseTestCase


class RegistrationTestCases(BaseTestCase):
    """Registration test cases"""

    def test_registration_returns_200_on_get_request(self):
        """Test registration page returns response of 200 for GET request"""
        response = self.client.get('auth/register/', follow_redirects=True)
        self.assert200(response)

    def test_registration_returns_200_on_post_request(self):
        """Test POST request to registration route returns 200"""
        response = self.client.post("auth/register/", follow_redirects=True)
        self.assert200(response)

    def test_registration_returns_201_when_user_data_is_posted(self):
        """Test POST request with data to registration returns 201 response"""
        user = {'username': 'user3', 'password': 'user3_password', "email": "user3_email",
                "first_name": "user3_first_name", "last_name": "user3_last_name"}
        req = self.client.post('/auth/register/', data=user)
        self.assertEqual(req.status_code, 201)

    def test_registration_raises_exception_when_user_exists(self):
        """Test registration route raises Exception when user already exists"""
        user = {'username': 'user2', 'password': 'user2_password', "email": "user2_email"}
        with self.assertRaises(UserAlreadyExists) as context:
            self.client.post('/auth/register/', data=user)
            self.assertTrue(UserAlreadyExists.detail in context.exception)


class LoginTestCases(BaseTestCase):
    """ Tests correct user login"""

    def test_correct_logging_in_returns_200(self):
        """Test login route returns 200"""
        response = self.login()
        self.assert200(response)

    def test_get_request_raises_credentials_required_error(self):
        """Test GET request to login without credentials raises error"""
        with self.assertRaises(CredentialsRequired) as context:
            self.client.get("/auth/login/")
            self.assertTrue(CredentialsRequired.detail in context.exception)

    def test_get_request_with_correct_credentials_returns_response(self):
        """Test GET request with correct credentials returns correct response"""
        response = self.login()
        self.assertIn(b'You have logged in successfully', response.data)

    def test_incorrect_logging_in_returns_401(self):
        """Tests incorrect user login will raise error"""
        wrong_req = self.client.post('/auth/login/', data=dict(username="itsme",
                                                               email="noclue@example.com",
                                                               password="i have no idea"))
        self.assert401(wrong_req)

    def test_incorrect_credentials_raises_error(self):
        """Tests incorrect user credentials raises error"""
        with self.assertRaises(AuthenticationFailed) as context:
            self.client.post('/auth/login/', data=dict(username="user1",
                                                       email="user1@example.com",
                                                       password="i have no idea"))
            self.assertEqual(AuthenticationFailed.detail, context.exception)

    def test_correct_credentials_logs_in_user_with_flask_login(self):
        """Test correct credentials logs in user with flask login"""
        with self.client:
            self.login()
            self.assertIsNotNone(current_user)
            self.assertTrue(current_user.is_active)
            self.assertTrue(current_user.is_authenticated)

    def test_log_out_with_valid_jwt_token(self):
        """Test user can correctly log out when passing JWT token in header"""
        with self.client:
            response = self.login()
            json_response = json.loads(response.data.decode("utf-8"))
            jwt_token = json_response.get("token")
            headers = {'Authorization': 'Bearer {0}'.format(jwt_token)}
            logout_response = self.client.get("/auth/logout/", headers=headers)
            self.assertIn('You have logged out successfully', logout_response.data.decode("utf-8"))

    def test_correct_token_generation(self):
        """Tests correct token generation"""
        rv = self.client.post("/auth/login/", data={'username': 'its-me', 'password': 'i have no idea'})
        res_json = json.loads(rv.data.decode("utf-8"))
        jwt_token = res_json.get('token')
        self.assertIsNone(jwt_token)


if __name__ == "__main__":
    unittest.main()
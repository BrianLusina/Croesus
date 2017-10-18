import json
import unittest
from unittest.mock import patch
from flask_api.exceptions import AuthenticationFailed, NotFound
from flask_login import current_user
from app.mod_auth.exceptions import UserAlreadyExists, CredentialsRequired
from tests import BaseTestCase
from app.mod_auth.tasks import send_mail_async
from app.mod_auth.models import UserAccount
from flask import url_for


class RegistrationTestCases(BaseTestCase):
    """Registration test cases"""

    def test_registration_returns_200_on_get_request(self):
        """Test registration page returns response of 200 for GET request"""
        response = self.client.get('auth/register/', follow_redirects=True)
        self.assert200(response)

    @patch.object(send_mail_async, "delay")
    def test_registration_returns_201_when_user_data_is_posted(self, mock_send_email_task):
        """Test POST request with data to registration returns 201 response"""
        user_data = dict(email="doge@woof.com", first_name="doge", last_name="doge",
                         password="ihatecats", username="dogewoof")
        req = self.client.post('/auth/register/', data=user_data)
        self.assertEqual(req.status_code, 201)

    def test_registration_raises_exception_when_user_exists(self):
        """Test registration route raises Exception when user already exists"""
        user = {'username': 'user2', 'password': 'user2_password',
                "email": "user2@example.com"}
        with self.assertRaises(UserAlreadyExists) as context:
            self.client.post('/auth/register/', data=user)
            self.assertTrue(UserAlreadyExists.detail in context.exception)


class LoginTestCases(BaseTestCase):
    """ Tests correct user login"""

    def test_correct_log_in_returns_200(self):
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

    def test_correct_token_generation(self):
        """Tests correct token generation"""
        rv = self.client.post("/auth/login/", data={'username': 'its-me', 'password': 'i have no idea'})
        res_json = json.loads(rv.data.decode("utf-8"))
        jwt_token = res_json.get('token')
        self.assertIsNone(jwt_token)


class LogoutTestCases(BaseTestCase):
    """
    logout test cases
    """

    def test_log_out_with_valid_jwt_token(self):
        """Test user can correctly log out when passing JWT token in header"""
        with self.client:
            response = self.login()
            json_response = json.loads(response.data.decode("utf-8"))
            jwt_token = json_response.get("token")
            headers = {'Authorization': 'Bearer {0}'.format(jwt_token)}
            logout_response = self.client.get("/auth/logout/", headers=headers)
            self.assertIn('You have logged out successfully', logout_response.data.decode("utf-8"))
            self.assert200(logout_response)

    # def test_anonymous_user_logout_raises_error(self):
    #     """Test that anonymous user logout raises error"""
    #     with self.assertRaises(NotFound) as ctx:
    #         self.client.get("/auth/logout/")
    #         self.assertIn(NotFound.detail, ctx.exception)
    #         self.assertEqual(NotFound.status_code, 404)


class AuthBackgroundTasks(BaseTestCase):
    """Tests that background tasks are executed"""

    @patch.object(send_mail_async, "delay")
    def test_registration_sends_email_to_user(self, mock_send_email_task):
        """Test POST request with data to registration sends email in background"""
        user_data = dict(email="doge@woof.com", first_name="doge", last_name="doge",
                         password="ihatecats", username="dogewoof")
        user_account = UserAccount(email="doge@woof.com", password="ihatecats", username="dogewoof")
        req = self.client.post('/auth/register/', data=user_data)
        self.assertEqual(req.status_code, 201)

        # create a token from the new user account
        token = user_account.generate_confirmation_token()

        # _external adds the full absolute URL that includes the hostname and port
        confirm_url = "http://localhost/auth/confirm/{token}".format(token=token.decode("utf-8"))

        self.assertTrue(mock_send_email_task.called)
        # assert that the task was called once
        # self.assertTrue(mock_send_email_task.assert_called_once_with(to=user_data.get("email"),
        #                                                              subject="Please confirm your email",
        #                                                              template="auth.confirm_email.html",
        #                                                              confirm_url=confirm_url))


if __name__ == "__main__":
    unittest.main()
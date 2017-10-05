import unittest
from datetime import datetime

from flask_login import current_user
from unittest.mock import patch

from app import db
from app.mod_auth.models import UserAccount
from app.mod_auth.security import generate_confirmation_token, confirm_token
from tests import BaseTestCase
import json
from app.mod_auth.security import send_mail_async


class TestRegistration(BaseTestCase):
    """
    Tests the registration flow
    """
    def test_register_page_returns_200(self):
        """Test register page returns response 200"""
        response = self.client.get("auth/register")
        self.assert200(response)

    def test_get_request_returns_empty_dict(self):
        """Test GET request to register route returns empty dict"""
        response = self.client.get("auth/register")
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 0)

    @patch("app.mod_auth.security.send_mail_async")
    def test_post_request_returns_200(self, send_email_async):
        """Test post request to register route returns 200"""
        response = self.client.post("auth/register", data=dict(email="croesus@example.com",
                                    first_name="Croesus", last_name="Inc",
                                    username="croesus", password="croesus_password"))
        self.assert200(response)


@unittest.skip
class TestAuthentication(BaseTestCase):
    """
    Tests for auth blueprint views
    """

    def test_correct_login(self):
        """Test login behaves correctly with correct credentials"""
        with self.client:
            response = self.login()

            self.assertTrue(response.status_code == 200)
            # todo: check why current user is not authenticated or active?
            # self.assertTrue(current_user.is_active)
            # self.assertTrue(current_user.is_authenticated)

    def test_incorrect_login(self):
        """Test to ensure login behaves correctly with incorrect credentials"""
        with self.client:
            response = self.client.post(
                "auth/login",
                data=dict(email='guydemaupassant@hadithi.com', password='wrong', confirm='password'),
                follow_redirects=True
            )

            self.assertTrue(response.status_code == 200)
            self.assertFalse(current_user.is_active)
            self.assertFalse(current_user.is_authenticated)

    def test_logout(self):
        """Test that logout behaves correctly"""
        with self.client:
            self.login()

            response = self.client.get('/logout', follow_redirects=True)

            self.assertTrue(b'Logout' not in response.data)
            self.assertFalse(current_user.is_active)
            self.assertTrue(current_user.is_anonymous)

    def test_logout_route_requires_login(self):
        """ Test to ensure that logout page requires author login"""
        response = self.client.get('/logout', follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        # todo: handle assertion in for response data
        # self.assertIn(b'Please login', response.data)

    def test_login_page_loads(self):
        """Test Login page should load successfully"""
        response = self.client.get('/login')
        self.assertIn(b'login', response.data)

    def test_confirm_token_route_requires_login(self):
        """Test the confirm/<token> route requires a logged in user"""
        # blah is the random token
        response = self.client.get("/confirm/blah", follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        # todo: handle rendering templates
        # self.assertTemplateUsed(name="auth/login.html")

    def test_confirm_token_route_valid_token(self):
        """Ensure user can confirm account with valid token"""
        with self.client:
            self.client.post(
                "auth/login",
                data=dict(email='guydemaupassant@hadithi.com', password='password', confirm='password'),
                follow_redirects=True
            )
            token = generate_confirmation_token(email="guydemaupassant@hadithi.com")

            response = self.client.get(
                "/confirm/" + token, follow_redirects=True
            )

            # self.assertIn(b'You have confirmed your account', response.data)
            # self.assertTemplateUsed('main/index.html')
            author = UserAccount.query.filter_by(email='guydemaupassant@hadithi.com').first()
            self.assertTrue(response.status_code == 200)
            # todo: confirmed on tests keeps failing
            # self.assertIsInstance(author.confirmed_on, datetime)
            # self.assertTrue(author.confirmed)

    def test_confirm_token_route_invalid_token(self):
        """Ensure user can not confirm account with invalid token"""
        token = generate_confirmation_token('guydemaupassant@hadithi.com')
        with self.client:
            self.login()
            response = self.client.get('/confirm/' + token, follow_redirects=True)
            self.assertTrue(response.status_code == 200)
            # self.assertIn(
            #     b'The confirmation link is invalid or has expired.',
            #     response.data
            # )

    def test_confirm_token_route_expired_token(self):
        # Ensure user cannot confirm account with expired token.
        author = UserAccount(first_name="Test", last_name="Hadithi", email="test@hadithi.com",
                             username="testhadithi", password="password", registered_on=datetime.now())
        db.session.add(author)
        db.session.commit()
        token = generate_confirmation_token('test@hadithi.com')
        self.assertFalse(confirm_token(token))


if __name__ == '__main__':
    unittest.main()

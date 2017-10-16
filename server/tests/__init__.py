import unittest
from datetime import datetime
from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError
import json
from app import create_app, db, app_logger
from app.mod_auth.models import UserAccount, UserProfile


class ContextTestCase(TestCase):
    render_templates = True

    def create_app(self):
        app = create_app("testing")
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app

    def _pre_setup(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def __call__(self, result=None):
        try:
            self._pre_setup()
            super(ContextTestCase, self).__call__(result)
        finally:
            self._post_teardown()

    def _post_teardown(self):
        if getattr(self, '_ctx', None) and self._ctx is not None:
            self._ctx.pop()
            del self._ctx


class BaseTestCase(ContextTestCase):
    """
    Base test case for application
    """

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db

        db.create_all()

        self.create_accounts()

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @staticmethod
    def create_user_profiles():
        """
        Creates user profiles
        :return: tuple of user profiles
        """

        user1_profile = UserProfile(first_name="user1", last_name="user1Lastname",
                                    email="user1@example.com")

        user2_profile = UserProfile(first_name="user2", last_name="user2LastName",
                                    email="user2@example.com")
        db.session.add(user1_profile)
        db.session.add(user2_profile)
        db.session.commit()

        return user1_profile, user2_profile

    def create_accounts(self):
        """
        Creates accounts with users bucket lists and bucket list items
        :return: dictionary with the 2 new unique users to test
        """
        user1_profile, user2_profile = self.create_user_profiles()

        user1_account = UserAccount(username="user1", email="user1@example.com",
                                    password="user1_pass",
                                    registered_on=datetime.now(),
                                    user_profile_id=user1_profile.id)

        user2_account = UserAccount(username="user2", email="user2@example.com",
                                    password="user2_pass", registered_on=datetime.now(),
                                    user_profile_id=user2_profile.id)

        try:
            db.session.add(user2_account)
            db.session.add(user1_account)
            db.session.commit()
        except IntegrityError as ie:
            app_logger.exception("Encountered error creating values {}".format(ie))
            db.session.rollback()

        return user1_account, user2_account

    def login(self):
        """
        Login in the user to the testing app
        :return: The authenticated user for the test app
        """
        return self.client.post(
            "/auth/login/", data=dict(email='user1@example.com', username="user1",
                                      password='user1_pass'), follow_redirects=True
        )

    def get_jwt_token(self):
        """
        Gets JWT(JSON Web Token) token from the login response
        :return: JWT token
        :rtype: str
        """
        login_response = self.login()
        login_data = json.loads(login_response.data.decode("utf-8"))
        jwt_token = login_data.get("token")
        return jwt_token

    def get_headers(self):
        """Returns headers to be used in POST requests"""
        return {"Authorization": "Bearer {0}".format(self.get_jwt_token())}


if __name__ == "__main__":
    unittest.main()
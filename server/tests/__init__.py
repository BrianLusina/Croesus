import unittest
from app import create_app, db
from app.mod_auth.models import UserAccount, UserAccountStatus, UserProfile
from sqlalchemy.exc import IntegrityError
from flask import url_for
from datetime import datetime
from flask_testing import TestCase


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

        self.create_user_accounts()
        # self.add_story()

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @staticmethod
    def create_user_accounts():
        """
        Creates new users for testing follow feature
        :return: 2 new unique users to test follow and unfollow feature
        """

        user_account1 = UserAccount(first_name="test1", last_name="hadithi1",
                                    username="test1hadithi",
                                    email="test1hadithi@hadithi.com",
                                    password="password", registered_on=datetime.now())

        user_account2 = UserAccount(first_name="test2", last_name="hadithi2",
                                    username="test2hadithi",
                                    email="test2hadithi@hadithi.com",
                                    password="password", registered_on=datetime.now())

        user_account3 = UserAccount(first_name="Guy De", last_name="Maupassant",
                                    username="guydemaupassant",
                                    email="guydemaupassant@hadithi.com",
                                    password="password", registered_on=datetime.now())

        user_account4 = UserAccount(first_name="brian", last_name="lusina",
                                    username="lusinabrian", email="lusinabrian@hadithi.com",
                                    password="password", registered_on=datetime.now())
        try:
            db.session.add(user_account1)
            db.session.add(user_account2)
            db.session.add(user_account3)
            db.session.add(user_account4)
            db.session.commit()
        except IntegrityError as ie:
            print("Integrity Error: ", ie)
            db.session.rollback()

        return user_account1, user_account2, user_account3, user_account4

    def login(self):
        """
        Login in the user to the testing app
        :return: The authenticated user for the test app
        """
        return self.client.post(
            "auth/login",
            data=dict(email='guydemaupassant@hadithi.com', password='password', confirm='password'),
            follow_redirects=True
        )

        # def add_story(self):
        #     """
        #     Adds a dummy story to the database
        #     :return:
        #     """
        #     user_account1, user_account2, user_account3, user_account4 = self.create_user_accounts()
        #     story = Story.query.filter_by(user_account_id=user_account1.id).first()
        #     if story is None:
        #         try:
        #             story = Story(title="Gotham in flames", tagline="Dark city catches fire",
        #                           category="Fiction", content="", user_account_id=user_account1.id)
        #             db.session.add(story)
        #         except IntegrityError as e:
        #             print(e)
        #             db.session.rollback()
        #     return story
        # 
        # def save_user_story(self, story_id):
        #     return self.client.get(
        #         url_for("story.save_story", app_id=story_id),
        #         follow_redirects=True)


if __name__ == "__main__":
    unittest.main()

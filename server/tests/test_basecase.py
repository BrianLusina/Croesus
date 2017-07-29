import unittest
import uuid
from flask import current_app, url_for
from sqlalchemy.exc import IntegrityError
from app.mod_auth.models import UserAccount, UserAccountStatus, UserProfile
from app import create_app, db


class ContextTestCase(unittest.TestCase):
    def __call__(self, result=None):
        try:
            self._pre_setup()
            super(ContextTestCase, self).__call__(result)
        finally:
            self._post_teardown()

    def _pre_setup(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()

    def _post_teardown(self):
        if getattr(self, '_ctx') and self._ctx is not None:
            self._ctx.pop()
        del self._ctx


class BaseTestCase(ContextTestCase):
    """
    Base test case for Hadithi
    """

    def create_author_account(self):
        author = UserAccount.query.filter_by(email="johndoe@example.com").first()
        if author is None:
            try:
                author = UserAccount(fname="John", lname="Doe", email="johndoe@example.com", password="password")
                db.session.add(author)
            except IntegrityError as ie:
                print(ie)
                db.session.rollback()
        return author

    def setUp(self):
        db.create_all()

        self.create_author_account()

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

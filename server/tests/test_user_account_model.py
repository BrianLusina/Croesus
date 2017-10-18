from tests import BaseTestCase
import unittest
from unittest.mock import patch
from app.mod_auth.tasks import send_mail_async
from app.mod_auth.models import UserAccount
from datetime import datetime
import time
from werkzeug.security import check_password_hash
from app import db


class UserAccountModelTests(BaseTestCase):
    """
    Tests for user account model
    """
    @patch.object(send_mail_async, "delay")
    def test_on_user_register_a_new_account_is_created(self, mock_send_email_async):
        """Test that new registration creates a new user account"""
        with self.client:
            self.client.post("/auth/register/", data=dict(email="johndoe@example.com",
                                                          username="johndoe",
                                                          password="johndoe",
                                                          first_name="john",
                                                          last_name="doe"),
                             follow_redirects=True)
            user_account = UserAccount.query.filter_by(email="johndoe@example.com").first()
            self.assertIsNotNone(user_account)
            self.assertEqual(user_account.email, "johndoe@example.com")

    def test_password_setter(self):
        """Test that password is set on registration of a new user"""
        user_account = UserAccount(password="cat")
        self.assertIsNotNone(user_account.password_hash)

    def test_password_getter(self):
        """Test that user password can not be retrieved"""
        user_account = UserAccount(password="cat")
        with self.assertRaises(AttributeError) as ctx:
            user_account.password
            self.assertIn("Password is not a readable attribute", ctx.exception)

    def test_check_password(self):
        """Ensure given password is correct after un-hashing"""
        user_account = UserAccount.query.filter_by(email='user1@example.com').first()
        self.assertFalse(user_account.verify_password('user2_pass'))
        self.assertFalse(user_account.verify_password('another_admin'))
        self.assertTrue(check_password_hash(user_account.get_password, "user1_pass"))
        self.assertFalse(check_password_hash(user_account.get_password, "foobar"))

    def test_password_verification(self):
        """Test password verification"""
        user_account = UserAccount(password="dog")
        self.assertTrue(user_account.verify_password("dog"))
        self.assertFalse(user_account.verify_password("cat"))

    def test_password_salts_are_random(self):
        """Test that password salts are always random for 2 users"""
        user_account = UserAccount(password="doge")
        user_account_1 = UserAccount(password="doge")
        self.assertNotEqual(user_account.password_hash, user_account_1.password_hash)

    def test_valid_confirmation_token(self):
        """Test generated token for a user can be confirmed to belong to them"""
        u = UserAccount(email="johndoe@example.com", username="johndoe", password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token()
        self.assertTrue(u.confirm_token(token))

    def test_invalid_confirmation_token(self):
        """Test one user token can not confirm another user's token"""
        u1 = UserAccount(email="sinistercat@meow.com", username="cat_mack", password='cat')
        u2 = UserAccount(email="doge@woof.com", username="doge_wow", password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_confirmation_token()
        self.assertFalse(u2.confirm_token(token))

    def test_expired_confirmation_token(self):
        """Test a user can not confirm their token when expiration elapses"""
        u = UserAccount(username="johndoe", email="johndoe@example.com", password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token(1)
        time.sleep(2)
        self.assertFalse(u.confirm_token(token))

    def test_valid_reset_token(self):
        """Test a user can reset their password given a valid reset token"""
        u = UserAccount(username="doge", email="doge@woof.com", password='coco')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertTrue(u.reset_password(token, 'dog'))
        self.assertTrue(u.verify_password('dog'))

    def test_invalid_reset_token(self):
        """Test that valid reset token from one user can not reset another users password"""
        u1 = UserAccount(username="cat", email="cat@woof.com", password='cat')
        u2 = UserAccount(username="doge", email="doge@woof.com", password='doge')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_reset_token()
        self.assertFalse(u2.reset_password(token, "horse"))
        self.assertTrue(u2.verify_password("doge"))

    def test_valid_email_change_token(self):
        """Test valid email change token allows user to change their email"""
        u1 = UserAccount(username="dogcat", email="dogecat@woofmeow.com", password='catdoge')
        db.session.add(u1)
        db.session.commit()
        token = u1.generate_email_change_token("doge@woof.com")
        self.assertTrue(u1.change_email(token))
        self.assertEqual(u1.email, "doge@woof.com")

    def test_invalid_email_change_token(self):
        """Test valid email change token from 1 user can not update another users email"""
        u1 = UserAccount(username="cat", email="cat@meow.com", password='catdoge')
        u2 = UserAccount(username="ratatat", email="ratus@squeek.com", password='rat')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u2.generate_email_change_token("rodent@rodents.com")
        self.assertFalse(u1.change_email(token))
        self.assertEqual(u1.email, "cat@meow.com")

    def test_duplicate_email_change_token(self):
        """Test user can not change their current email to that of another existing email"""
        u1 = UserAccount(username="john", email='john@example.com', password='cat')
        u2 = UserAccount(username="susan", email='susan@example.org', password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u2.generate_email_change_token('john@example.com')
        self.assertFalse(u2.change_email(token))
        self.assertTrue(u2.email == 'susan@example.org')

    def test_timestamps(self):
        """Test member since attribute is updateed when a user registers"""
        u = UserAccount(username="cat", email="cat@meow.com", password='cat')
        db.session.add(u)
        db.session.commit()
        self.assertTrue((datetime.now() - u.member_since).total_seconds() < 3)
        # self.assertTrue((datetime.now() - u.last_seen).total_seconds() < 3)

    def test_ping(self):
        """Test pinging a user updates their last seen timestamp"""
        u = UserAccount(email="cat@wow.com", username="cat", password='cat')
        db.session.add(u)
        db.session.commit()
        time.sleep(2)
        last_seen_before = u.last_seen
        u.ping()
        self.assertTrue(u.last_seen > last_seen_before)

    def test_to_json(self):
        u = UserAccount(username="johndoe", email='john@example.com', password='cat')
        db.session.add(u)
        db.session.commit()
        json_user = u.to_json()
        expected_keys = ["id", 'uuid', 'username', 'member_since', 'last_seen',
                         'profile_id', 'account_status_id', 'email', "date_created",
                         "date_modified", "registered_on", "confirmed", "confirmed_on"]
        self.assertEqual(sorted(json_user.keys()), sorted(expected_keys))


if __name__ == "__main__":
    unittest.main()

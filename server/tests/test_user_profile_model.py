from tests import BaseTestCase
import unittest
from app.mod_auth.models import UserProfile
from app import db


class UserProfileModelTests(BaseTestCase):
    """Test cases for user profile"""

    def test_on_user_register_a_new_profile_is_created(self):
        """Test that new registration creates a new user account"""
        with self.client:
            self.client.post("/auth/register/", data=dict(email="johndoe@example.com",
                                                          username="johndoe",
                                                          password="johndoe",
                                                          first_name="john",
                                                          last_name="doe"),
                             follow_redirects=True)
            user_profile = UserProfile.query.filter_by(email="johndoe@example.com").first()
            self.assertIsNotNone(user_profile)
            self.assertEqual(user_profile.email, "johndoe@example.com")

    def test_user_profile_to_json(self):
        """test user profile email is unique"""
        user_profile = UserProfile(first_name="john", last_name="doe",
                                   email="johndoe@example.com")
        db.session.add(user_profile)
        db.session.commit()
        json_profile = user_profile.to_json()
        expected_keys = ["id", 'first_name', 'last_name', "date_created", "email",
                         "accept_terms_of_service", "date_modified"]
        self.assertListEqual(sorted(expected_keys), sorted(json_profile.keys()))


if __name__ == "__main__":
    unittest.main()
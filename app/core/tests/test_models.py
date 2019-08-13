from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfully(self):
        """Test creating a new user with email is successful"""
        email = "test@daniel.com"
        password = "test12344"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that a new user email is normalized"""
        email = "test@daniel.COM"
        user = get_user_model().objects.create_user(email, "test1234")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that a new user invalid email is flagged"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test12334")
        # user = get_user_model().objects.create_user("", "test12334")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser("daniel@test.com",
                                                         "test1234")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

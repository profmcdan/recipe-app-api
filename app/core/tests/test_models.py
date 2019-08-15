from django.test import TestCase
from django.contrib.auth import get_user_model
from .. import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class UserModelTests(TestCase):
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


class OtherModelTests(TestCase):
    """Test Tags Model"""

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name='Vegan')
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and Muchroom Sauce',
            price=23.40,
            time_minutes=5
        )
        self.assertEqual(str(recipe), recipe.title)

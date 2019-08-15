from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Recipe
from ..serializers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


def sample_recipe(user, **params):
    """Create and return a sample recipe"""
    default = {
        'title': 'Sample recipe',
        'time_minutes': 10,
        'price': 5.00
    }
    default.update(params)
    return Recipe.objects.create(user=user, **default)


class PublicRecipeApiTests(TestCase):
    """Test the public api"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test login is required to access this endpoint"""
        res = self.client.get(RECIPE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """Test the public api"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='test@test.com', password='testpass')
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes"""
        sample_recipe(user=self.user)
        sample_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)
        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipes_limited_to_user(self):
        """Test retrived recipes are for the user"""
        user2 = create_user(email='test2@test2.com', password='testpass2')
        sample_recipe(user=user2)
        sample_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

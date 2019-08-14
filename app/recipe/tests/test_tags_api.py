from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Tag
from ..serializers import TagSerializer

TAGS_URL = reverse('recipe:tag-list')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicTagApiTests(TestCase):
    """Test the tag api (public)"""

    def setup(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for the given task"""
        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagApiTests(TestCase):
    """Test the authorized tag api (public)"""

    def setup(self):
        self.user = get_user_model().objects.create_user('test@test.com', 'testpass')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retriving tags"""
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Dessert')

        res = self.client.get(TAGS_URL)
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test that the tags returned are for the authenticated user"""
        user2 = create_user(email='other@test.com', password='testpass2')
        tag = Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=user2, name='Comfy')

        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

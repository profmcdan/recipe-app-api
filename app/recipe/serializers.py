from rest_framework import serializers
from core import models


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the tag object"""
    class Meta:
        model = models.Tag
        fields = ('id', 'name',)
        read_only_field = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient object"""
    class Meta:
        model = models.Ingredient
        fields = ('id', 'name')
        read_only_field = ('id',)

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


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe object"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Tag.objects.all()
    )

    class Meta:
        model = models.Recipe
        fields = ('id', 'title', 'price', 'link',
                  'time_minutes', 'tags', 'ingredients')
        read_only_field = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

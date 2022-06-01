from titles.models import Category, Genre, Title
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title


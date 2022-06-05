from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import User, Titles, Genres, Categories, Reviews, Comments


class Registration(serializers.Serializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        required=True
    )

    def validate(self, attrs):
        if attrs.get('username') == 'me':
            raise serializers.ValidationError('Недопустимое имя.')
        if User.objects.filter(
                username=attrs.get('username')
        ).exists():
            raise serializers.ValidationError('Имя уже существует.')
        if User.objects.filter(
                email=attrs.get('email')
        ).exists():
            raise serializers.ValidationError('Почта уже существует.')
        return attrs

    class Meta:
        fields = ('username', 'email')
        model = User


class Confirmation(serializers.Serializer):
    username = serializers.CharField(
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=200,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username',
            'bio', 'email', 'role',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ('id', 'review', 'author')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'category', 'genre')
        model = Titles


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('id', 'title', 'author')


from django.contrib.auth import get_user_model
from django.db import models

# TODO: remove when user model is defined
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=64)
    year = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='title', null=True)
    genre = models.ManyToManyField(Genre, through='GenreTitle')


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

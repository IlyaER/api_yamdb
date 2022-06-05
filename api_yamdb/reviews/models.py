import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)   


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    USERROLES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin')
    ]
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=USERROLES,
        default=USER
    )


class Categories(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)


class Genres(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)


class Titles(models.Model): 
    name = models.CharField(max_length=64)
    year = models.IntegerField(
        validators=[MinValueValidator(1000), max_value_current_year])
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, related_name='title', null=True)
    genre = models.ManyToManyField(Genres, through='GenreTitle')


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)


class Reviews(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    text = models.TextField()
    title = models.ForeignKey(
        Titles, on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField(
        default=None,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ]
    )
    pub_date = models.DateTimeField(
        'Дата добавления отзыва', auto_now_add=True, db_index=True
    )
    
    class Meta:
        unique_together = ['title', 'author']


class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    review = models.ForeignKey(
        Reviews, on_delete=models.CASCADE
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления комментария', auto_now_add=True, db_index=True
    )

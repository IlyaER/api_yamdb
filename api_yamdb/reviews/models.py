from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass


class Titles(models.Model):
    pass


class Categories(models.Model):
    pass


class Genres(models.Model):
    pass


class Review(models.Model):
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


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления комментария', auto_now_add=True, db_index=True
    )

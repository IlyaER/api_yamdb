from django.contrib.auth.models import AbstractUser
from django.db import models


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

from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, verbose_name=("ФИО"))
    phone_number = models.CharField(
        max_length=30, unique=True, null=True, verbose_name="Номер телефона"
    )
    is_superuser = models.BooleanField("Админ", default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    def __str__(self) -> str:
        return self.username

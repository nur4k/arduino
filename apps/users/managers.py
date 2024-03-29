from typing import Any, Union

from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(
        self, username: str, password: Union[str, None] = None, **extra_fields: Any
    ) -> Any:
        if not username:
            raise ValueError("Введите никнейм!")

        username = self.model.normalize_username(username)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, username: str, password: Union[str, None] = None, **extra_fields: Any
    ) -> Any:
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        user = self.create_user(username=username, password=password, **extra_fields)
        return user

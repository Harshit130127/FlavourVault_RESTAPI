"""
Models for the FlavourVault application."""

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(
        self, email, password=None, **extra_fields
    ):  # it is built in method
        """Create and save a new user."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(
            email=email, **extra_fields
        )  # not passowrd because it needs to be hashed
        user.set_password(password)  # hash the password
        user.save(
            using=self._db
        )  # using self._db to support multiple databases

        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser."""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # assign the custom user manager

    USERNAME_FIELD = "email"  # Use email for authentication

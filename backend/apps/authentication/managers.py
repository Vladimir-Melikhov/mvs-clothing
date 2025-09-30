from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom manager for User model with email as the unique identifier.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.

        Args:
            email: User email address
            password: User password
            **extra_fields: Additional user fields

        Returns:
            User instance
        """
        if not email:
            raise ValueError(_("The Email field must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given email and password.

        Args:
            email: User email address
            password: User password
            **extra_fields: Additional user fields

        Returns:
            User instance
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_email_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        """
        Get user by email (natural key).

        Args:
            email: User email address

        Returns:
            User instance
        """
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": email})

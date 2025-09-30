from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from apps.core.utils import generate_random_string, send_email
from apps.core.exceptions import AuthenticationError, ValidationError, NotFoundError
from .models import User, PasswordResetToken, EmailVerificationToken


class AuthenticationService:
    """
    Service class for handling authentication business logic.
    """

    @staticmethod
    def register_user(validated_data):
        """
        Register a new user and send verification email.

        Args:
            validated_data: Validated user data

        Returns:
            Tuple of (user, tokens)
        """
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            tokens = AuthenticationService.generate_tokens(user)
            AuthenticationService.send_verification_email(user)

        return user, tokens

    @staticmethod
    def login_user(email, password, ip_address=None):
        """
        Authenticate user and generate tokens.

        Args:
            email: User email
            password: User password
            ip_address: Client IP address

        Returns:
            Tuple of (user, tokens)
        """
        user = authenticate(email=email, password=password)

        if user is None:
            raise AuthenticationError("Invalid email or password")

        if not user.is_active:
            raise AuthenticationError("Account is deactivated")

        if ip_address:
            user.last_login_ip = ip_address
            user.save(update_fields=["last_login_ip", "last_login"])

        tokens = AuthenticationService.generate_tokens(user)
        return user, tokens

    @staticmethod
    def generate_tokens(user):
        """
        Generate JWT access and refresh tokens for user.

        Args:
            user: User instance

        Returns:
            Dictionary with access and refresh tokens
        """
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    @staticmethod
    def change_password(user, old_password, new_password):
        """
        Change user password after validating old password.

        Args:
            user: User instance
            old_password: Current password
            new_password: New password
        """
        if not user.check_password(old_password):
            raise ValidationError("Current password is incorrect")

        user.set_password(new_password)
        user.save(update_fields=["password"])

    @staticmethod
    def request_password_reset(email):
        """
        Create password reset token and send reset email.

        Args:
            email: User email address
        """
        try:
            user = User.objects.get(email__iexact=email, is_active=True)
        except User.DoesNotExist:
            return

        token = generate_random_string(64)
        expires_at = timezone.now() + timedelta(hours=24)

        PasswordResetToken.objects.create(user=user, token=token, expires_at=expires_at)

        AuthenticationService.send_password_reset_email(user, token)

    @staticmethod
    def reset_password(token, new_password):
        """
        Reset user password using reset token.

        Args:
            token: Password reset token
            new_password: New password
        """
        try:
            reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            raise NotFoundError("Invalid or expired reset token")

        if not reset_token.is_valid():
            raise ValidationError("Token has expired or already been used")

        user = reset_token.user
        user.set_password(new_password)
        user.save(update_fields=["password"])

        reset_token.mark_as_used()

    @staticmethod
    def send_verification_email(user):
        """
        Send email verification link to user.

        Args:
            user: User instance
        """
        token = generate_random_string(64)
        expires_at = timezone.now() + timedelta(days=7)

        EmailVerificationToken.objects.create(
            user=user, token=token, expires_at=expires_at
        )

        # TODO: Implement email template and sending
        # send_email(
        #     subject='Verify your email address',
        #     recipient_list=[user.email],
        #     template_name='authentication/email_verification.html',
        #     context={'user': user, 'token': token}
        # )

    @staticmethod
    def verify_email(token):
        """
        Verify user email using verification token.

        Args:
            token: Email verification token
        """
        try:
            verification_token = EmailVerificationToken.objects.get(token=token)
        except EmailVerificationToken.DoesNotExist:
            raise NotFoundError("Invalid or expired verification token")

        if not verification_token.is_valid():
            raise ValidationError("Token has expired or already been used")

        user = verification_token.user
        user.is_email_verified = True
        user.save(update_fields=["is_email_verified"])

        verification_token.mark_as_used()

    @staticmethod
    def send_password_reset_email(user, token):
        """
        Send password reset email to user.

        Args:
            user: User instance
            token: Password reset token
        """
        # TODO: Implement email template and sending
        # send_email(
        #     subject='Reset your password',
        #     recipient_list=[user.email],
        #     template_name='authentication/password_reset.html',
        #     context={'user': user, 'token': token}
        # )
        pass

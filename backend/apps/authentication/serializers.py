from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import User
from .validators import validate_phone_number


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    password_confirm = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "password_confirm",
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_email(self, value):
        """
        Validate that the email is unique.

        Args:
            value: Email address

        Returns:
            Validated email
        """
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return value.lower()

    def validate_phone_number(self, value):
        """
        Validate phone number format.

        Args:
            value: Phone number

        Returns:
            Validated phone number
        """
        if value:
            validate_phone_number(value)
        return value

    def validate(self, attrs):
        """
        Validate that passwords match.

        Args:
            attrs: Serializer attributes

        Returns:
            Validated attributes
        """
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        """
        Create a new user instance.

        Args:
            validated_data: Validated data

        Returns:
            Created user instance
        """
        validated_data.pop("password_confirm")
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True, write_only=True, style={"input_type": "password"}
    )

    def validate_email(self, value):
        """
        Normalize email to lowercase.

        Args:
            value: Email address

        Returns:
            Normalized email
        """
        return value.lower()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile data.
    """

    full_name = serializers.CharField(source="get_full_name", read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
            "date_of_birth",
            "is_email_verified",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "email",
            "is_email_verified",
            "created_at",
            "updated_at",
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user profile.
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "date_of_birth"]

    def validate_phone_number(self, value):
        """
        Validate phone number format.

        Args:
            value: Phone number

        Returns:
            Validated phone number
        """
        if value:
            validate_phone_number(value)
        return value


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing user password.
    """

    old_password = serializers.CharField(
        required=True, write_only=True, style={"input_type": "password"}
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    new_password_confirm = serializers.CharField(
        required=True, write_only=True, style={"input_type": "password"}
    )

    def validate(self, attrs):
        """
        Validate that new passwords match.

        Args:
            attrs: Serializer attributes

        Returns:
            Validated attributes
        """
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError(
                {"new_password": "Passwords do not match"}
            )
        return attrs


class PasswordResetRequestSerializer(serializers.Serializer):
    """
    Serializer for password reset request.
    """

    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        """
        Normalize email to lowercase.

        Args:
            value: Email address

        Returns:
            Normalized email
        """
        return value.lower()


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for password reset confirmation.
    """

    token = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    new_password_confirm = serializers.CharField(
        required=True, write_only=True, style={"input_type": "password"}
    )

    def validate(self, attrs):
        """
        Validate that new passwords match.

        Args:
            attrs: Serializer attributes

        Returns:
            Validated attributes
        """
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError(
                {"new_password": "Passwords do not match"}
            )
        return attrs


class EmailVerificationSerializer(serializers.Serializer):
    """
    Serializer for email verification.
    """

    token = serializers.CharField(required=True)

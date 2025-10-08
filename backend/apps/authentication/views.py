from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView
from apps.core.responses import success_response, error_response, created_response
from apps.core.utils import get_client_ip
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
    EmailVerificationSerializer,
)
from .services import AuthenticationService
from .permissions import IsAccountOwner


class UserRegistrationView(APIView):
    """
    API view for user registration.
    """

    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        """
        Register a new user.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, tokens = AuthenticationService.register_user(serializer.validated_data)

        return created_response(
            data={"user": UserSerializer(user).data, "tokens": tokens},
            message="User registered successfully. Please verify your email",
        )


class UserLoginView(APIView):
    """
    API view for user login.
    """

    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        """
        Authenticate user and return tokens.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        ip_address = get_client_ip(request)
        user, tokens = AuthenticationService.login_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
            ip_address=ip_address,
        )

        return success_response(
            data={"user": UserSerializer(user).data, "tokens": tokens},
            message="Login successful",
        )


class UserProfileView(generics.RetrieveAPIView):
    """
    API view for retrieving user profile.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        """
        Return the current authenticated user.
        """
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve user profile data.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success_response(
            data=serializer.data, message="Profile retrieved successfully"
        )


class UserUpdateView(generics.UpdateAPIView):
    """
    API view for updating user profile.
    """

    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        """
        Return the current authenticated user.
        """
        return self.request.user

    def update(self, request, *args, **kwargs):
        """
        Update user profile data.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return success_response(
            data=UserSerializer(instance).data, message="Profile updated successfully"
        )


class ChangePasswordView(APIView):
    """
    API view for changing user password.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        """
        Change user password.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthenticationService.change_password(
            user=request.user,
            old_password=serializer.validated_data["old_password"],
            new_password=serializer.validated_data["new_password"],
        )

        return success_response(message="Password changed successfully")


class PasswordResetRequestView(APIView):
    """
    API view for requesting password reset.
    """

    permission_classes = [AllowAny]
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        """
        Send password reset email to user.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthenticationService.request_password_reset(
            email=serializer.validated_data["email"]
        )

        return success_response(
            message="If an account exists with this email, a password reset link has been sent"
        )


class PasswordResetConfirmView(APIView):
    """
    API view for confirming password reset.
    """

    permission_classes = [AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        """
        Reset user password using token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthenticationService.reset_password(
            token=serializer.validated_data["token"],
            new_password=serializer.validated_data["new_password"],
        )

        return success_response(message="Password reset successfully")


class EmailVerificationView(APIView):
    """
    API view for email verification.
    """

    permission_classes = [AllowAny]
    serializer_class = EmailVerificationSerializer

    def post(self, request):
        """
        Verify user email using token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthenticationService.verify_email(token=serializer.validated_data["token"])

        return success_response(message="Email verified successfully")


class ResendVerificationEmailView(APIView):
    """
    API view for resending verification email.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Resend verification email to user.
        """
        user = request.user

        if user.is_email_verified:
            return error_response(
                message="Email is already verified",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        AuthenticationService.send_verification_email(user)

        return success_response(message="Verification email sent successfully")

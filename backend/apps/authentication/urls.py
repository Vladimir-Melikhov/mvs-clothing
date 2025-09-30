from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserUpdateView,
    ChangePasswordView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    EmailVerificationView,
    ResendVerificationEmailView,
)

app_name = "authentication"

urlpatterns = [
    # Authentication endpoints
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # User profile endpoints
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="profile-update"),
    # Password management endpoints
    path("password/change/", ChangePasswordView.as_view(), name="password-change"),
    path(
        "password/reset/request/",
        PasswordResetRequestView.as_view(),
        name="password-reset-request",
    ),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
    # Email verification endpoints
    path("email/verify/", EmailVerificationView.as_view(), name="email-verify"),
    path("email/resend/", ResendVerificationEmailView.as_view(), name="email-resend"),
]

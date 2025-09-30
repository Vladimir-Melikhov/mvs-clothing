from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """Configuration class for the authentication application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.authentication"
    verbose_name = "Authentication"

    def ready(self):
        """Import signal handlers when the app is ready."""
        import apps.authentication.signals

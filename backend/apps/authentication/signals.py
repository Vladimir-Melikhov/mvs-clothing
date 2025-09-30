from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for User post-save events.

    Args:
        sender: Model class
        instance: User instance
        created: Boolean indicating if instance was created
        **kwargs: Additional keyword arguments
    """
    if created:
        # Perform actions after user creation
        # For example: create user profile, send welcome email, etc.
        pass

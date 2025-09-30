import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    """
    Validate phone number format.

    Args:
        value: Phone number string

    Raises:
        ValidationError: If phone number format is invalid
    """
    phone_regex = re.compile(r"^\\+?1?\\d{9,15}$")

    if not phone_regex.match(value):
        raise ValidationError(
            _(
                'Phone number must be entered in the format: "+999999999". '
                "Up to 15 digits allowed."
            )
        )


def validate_age(date_of_birth):
    """
    Validate that user is at least 13 years old.

    Args:
        date_of_birth: User's date of birth

    Raises:
        ValidationError: If user is under 13 years old
    """
    from datetime import date

    today = date.today()
    age = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )

    if age < 13:
        raise ValidationError(_("You must be at least 13 years old to register"))

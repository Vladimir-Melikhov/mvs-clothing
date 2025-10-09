import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_phone_number_format(value):
    """
    Validate phone number format (e.g., +1234567890, 1234567890).
    """
    cleaned_value = re.sub(r'[\s\-\(\)]', '', value)
    phone_regex = re.compile(r'^\+?\d{9,15}$')
    if not phone_regex.match(cleaned_value):
        raise ValidationError(
            _(
                'Phone number must be entered in the format: "+999999999". '
                'Up to 15 digits allowed.'
            )
        )


def validate_age(date_of_birth):
    """
    Validate that user is at least 13 years old.
    """

    today = date.today()
    age = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )

    if age < 13:
        raise ValidationError(_("You must be at least 13 "
                                "years old to register"))

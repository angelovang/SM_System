from django.core import validators
from django.db import models

from tools.validators import first_char_capital_validator, is_letter_validator, phone_validator


class Client(models.Model):
    use_in_migration = True

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    PHONE_MAX_LENGTH = 12
    PHONE_MIN_LENGTH = 9

    email = models.EmailField(
        unique=True,
        validators={validators.EmailValidator},
        blank=True,
        null=True
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            is_letter_validator,
            first_char_capital_validator,
        ),
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            is_letter_validator,
            first_char_capital_validator,
        ),
        blank=False,
        null=False,
    )

    phone_number = models.CharField(
        max_length=PHONE_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(PHONE_MIN_LENGTH),
            phone_validator,
        ),
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('-pk',)

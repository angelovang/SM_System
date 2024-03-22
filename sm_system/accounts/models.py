from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from tools.validators import is_letter_validator, first_char_capital_validator, phone_validator, validate_file_size


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]

    @classmethod
    def max_len(cls):
        return max(len(x) for x, _ in cls.choices())


class Type(ChoicesMixin, Enum):
    receptionist = 'Receptionist'
    technician = 'Technician'
    manager = 'Manager'


class SmsUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    PHONE_MAX_LENGTH = 12
    PHONE_MIN_LENGTH = 9

    email = models.EmailField(
        unique=True,
        validators={validators.EmailValidator},
        blank=False,
        null=False
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
        unique=True,
        validators=(
            validators.MinLengthValidator(PHONE_MIN_LENGTH),
            phone_validator,
        ),
        blank=False,
        null=False,
    )

    user_type = models.CharField(
        choices=Type.choices(),
        max_length=Type.max_len(),
        blank=True,
        null=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        validators=(
            validate_file_size,
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('pk',)
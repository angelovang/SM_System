from datetime import datetime

from django.core.exceptions import ValidationError


def phone_validator(value):
    error_messages = []
    if value[0] != '0' and value[:3] != '359':
        error_messages.append("Phone number must start with '359' or '0' !")
    for v in value:
        if not v.isdigit():
            error_messages.append('Phone number must contain only digits !')

    if error_messages:
        raise ValidationError('\n'.join(error_messages))


def is_letter_validator(value):
    is_letter = value.isalpha()
    if not is_letter:
        raise ValidationError('Name should contain only letters!')


def first_char_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def first_char_capital_validator(value):
    ch_asii = ord(value[0])
    if ch_asii < 65 or ch_asii > 90:
        raise ValidationError('Your name must start with a capital letter!')


def date_in_the_past(date):
    if date < datetime.now().date():
        raise ValidationError('The date cannot be in the past!')


def alfa_num_validator(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def least_one_digit_validator(value):
    have_digit = value.isalnum()
    if not have_digit:
        raise ValidationError('The password must contain at least 1 digit!')

def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")

# Generated by Django 5.0.3 on 2024-03-22 19:55

import django.core.validators
import tools.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_smsuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsuser',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.MinLengthValidator(9), tools.validators.phone_validator]),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-22 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smsuser',
            options={'ordering': ('pk',)},
        ),
    ]

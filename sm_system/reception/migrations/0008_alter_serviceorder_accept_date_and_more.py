# Generated by Django 5.0.3 on 2024-03-26 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_options'),
        ('reception', '0007_alter_serviceorder_client_alter_serviceorder_so_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='accept_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='client',
            field=models.ForeignKey(default=(), on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='so_id',
            field=models.CharField(default='15306d84', editable=False, max_length=20, unique=True),
        ),
    ]

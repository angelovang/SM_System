# Generated by Django 5.0.3 on 2024-04-08 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_options'),
        ('reception', '0019_alter_serviceorder_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershistory',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reception.serviceorder'),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='client',
            field=models.ForeignKey(default=(), on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client'),
        ),
    ]

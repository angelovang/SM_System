# Generated by Django 5.0.3 on 2024-04-08 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_options'),
        ('reception', '0020_alter_ordershistory_order_alter_serviceorder_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordershistory',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='client',
            field=models.ForeignKey(default=(), on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client'),
        ),
    ]

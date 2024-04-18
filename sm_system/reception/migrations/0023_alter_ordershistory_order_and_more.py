# Generated by Django 5.0.3 on 2024-04-13 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_options'),
        ('reception', '0022_alter_serviceorder_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershistory',
            name='order',
            field=models.ForeignKey(on_delete=models.SET(-1), to='reception.serviceorder'),
        ),
        migrations.AlterField(
            model_name='ordershistory',
            name='technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='client',
            field=models.ForeignKey(on_delete=models.SET('-1'), to='clients.client'),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
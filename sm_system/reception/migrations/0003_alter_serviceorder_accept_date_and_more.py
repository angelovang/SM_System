# Generated by Django 5.0.3 on 2024-03-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_alter_serviceorder_accept_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='accept_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='so_id',
            field=models.CharField(default='a0652e0c', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='serviceorder',
            name='so_pass',
            field=models.CharField(default='a78c6c12', max_length=8, unique=True),
        ),
    ]

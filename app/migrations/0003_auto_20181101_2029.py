# Generated by Django 2.1.3 on 2018-11-01 20:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_game_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='points',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
    ]
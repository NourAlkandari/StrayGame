# Generated by Django 2.2 on 2019-04-24 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190424_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstate',
            name='hunger',
            field=models.IntegerField(default=50, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]

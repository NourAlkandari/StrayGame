# Generated by Django 2.2 on 2019-04-29 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190425_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(default='Doggo', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='petstate',
            name='bladder',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='petstate',
            name='fun',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='petstate',
            name='hunger',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='petstate',
            name='sleep',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='petstate',
            name='social',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]

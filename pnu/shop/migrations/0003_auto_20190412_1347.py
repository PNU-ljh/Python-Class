# Generated by Django 2.1.8 on 2019-04-12 04:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]

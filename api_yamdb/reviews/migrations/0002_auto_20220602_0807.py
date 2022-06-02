# Generated by Django 2.2.16 on 2022-06-02 08:07

import django.core.validators
from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), reviews.models.max_value_current_year]),
        ),
    ]

# Generated by Django 2.2.16 on 2022-06-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

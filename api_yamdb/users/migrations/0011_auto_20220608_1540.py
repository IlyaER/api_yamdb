# Generated by Django 2.2.16 on 2022-06-08 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220531_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('pk',)},
        ),
    ]
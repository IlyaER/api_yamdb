# Generated by Django 2.2.16 on 2022-06-05 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220605_1221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterModelOptions(
            name='titles',
            options={'ordering': ('pk',)},
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-07 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_year',
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_remove_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_now_playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='is_watched',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movie_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_watched',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_year', models.PositiveIntegerField()),
                ('director', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('poster_image', models.ImageField(upload_to='movie_posters/')),
                ('backdrop_image', models.ImageField(upload_to='movie_backdrops/')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('runtime_minutes', models.PositiveIntegerField()),
                ('release_date', models.DateField()),
                ('genres', models.CharField(max_length=255)),
                ('synopsis', models.TextField()),
            ],
        ),
    ]

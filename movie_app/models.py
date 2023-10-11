from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    tagline = models.TextField(max_length=500)
    synopsis = models.TextField()
    poster_image = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    backdrop_image = models.ImageField(upload_to='movie_backdrops/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    runtime_minutes = models.PositiveIntegerField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    is_watched = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_now_playing = models.BooleanField(default=False)
    watch_list = models.BooleanField(default=True)
    trailer = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
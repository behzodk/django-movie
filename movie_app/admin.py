from django.contrib import admin
from .models import *

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'rating')
    list_filter = ('release_date', 'director', 'rating')
    search_fields = ('title', 'director')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_genres(self, obj):
        # Get the genre names associated with the movie
        genre_names = obj.genres.all().values_list('name', flat=True)
        return genre_names
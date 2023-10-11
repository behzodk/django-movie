from rest_framework import generics
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getGenres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGenre(request, pk):
    genre = Genre.objects.get(id=pk)
    serializer = GenreSerializer(genre, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMovies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMovie(request,pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)

class PopularMovieList(generics.ListAPIView):
    queryset = Movie.objects.filter(is_popular=True)
    serializer_class = MovieSerializer

class LiveMovieList(generics.ListAPIView):
    queryset = Movie.objects.filter(is_now_playing=True)
    serializer_class = MovieSerializer

class WatchListMovieList(generics.ListAPIView):
    queryset = Movie.objects.filter(watch_list=True)
    serializer_class = MovieSerializer

class WatchedMovieList(generics.ListAPIView):
    queryset = Movie.objects.filter(is_watched=True)
    serializer_class = MovieSerializer

class TenImages(generics.ListAPIView):
    queryset = Movie.objects.order_by('-release_date').all()[:10]
    serializer_class = MovieSerializer

class OrderRank(generics.ListAPIView):
    queryset = Movie.objects.order_by('-rating').all()
    serializer_class = MovieSerializer

@api_view(['POST'])
def createMovie(request):
    data = request.data
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
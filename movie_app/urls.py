from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.getGenres, name='genre-list'),
    path('genres/<int:pk>/', views.getGenre, name='genre-detail'),
    path('movies/', views.getMovies, name='get-movie'),
    path('movies/create/', views.createMovie, name='create-movie'),
    path('movies/<int:pk>/', views.getMovie, name='movie-detail'),
    path('movies/popular/', views.PopularMovieList.as_view(), name='popular-movie-list'),
    path('movies/live/', views.LiveMovieList.as_view(), name='live-movie-list'),   
    path('movies/watch_list/', views.WatchListMovieList.as_view(), name='watchlist-movie-list'),
    path('movies/watched/', views.WatchedMovieList.as_view(), name='watched-movie-list'),
    path('movies/ten/', views.TenImages.as_view(), name='ten_images'),
    path('movies/rated/', views.OrderRank.as_view(), name='rank'),
]
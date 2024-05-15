from django.urls import path

from coding_challenge.movies.views.movie_list import MovieDetail, MovieList
from movies.views import MovieListView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path('<int:id>/', MovieDetail.as_view(), name='movie-detail'),
    path('api/movies/', MovieList.as_view(), name='movie-list'),
]

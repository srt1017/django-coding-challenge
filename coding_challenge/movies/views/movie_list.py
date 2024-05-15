from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView


from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieList(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        min_runtime = self.request.query_params.get('min_runtime')
        max_runtime = self.request.query_params.get('max_runtime')

        if min_runtime is not None:
            queryset = queryset.filter(runtime__gte=int(min_runtime))
        if max_runtime is not None:
            queryset = queryset.filter(runtime__lte=int(max_runtime))

        return queryset

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

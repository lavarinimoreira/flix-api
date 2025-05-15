from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    """
    Router: movies/
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: movier/<int:fk>
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

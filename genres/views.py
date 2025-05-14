from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    """
    Router: genres/
    """
    queryset = Genre.objects.all() 
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: genres/<int:pk>/
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

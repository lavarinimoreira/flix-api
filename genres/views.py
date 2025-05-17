from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreModelSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    """
    Router: genres/
    """
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all() 
    serializer_class = GenreModelSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: genres/<int:pk>/
    """
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

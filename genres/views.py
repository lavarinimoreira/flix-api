from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreModelSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    """
    Router: genres/
    """
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all() 
    serializer_class = GenreModelSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: genres/<int:pk>/
    """
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

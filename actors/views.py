from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    """
    Router: actors/
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: actors/<int:pk>
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

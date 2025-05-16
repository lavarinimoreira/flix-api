from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorModelSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    """
    Router: actors/
    """
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: actors/<int:pk>
    """
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer

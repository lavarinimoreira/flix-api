from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    """
    Router: reviews/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: reviews/<int:pk>/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

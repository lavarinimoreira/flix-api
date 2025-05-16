from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewModelSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    """
    Router: reviews/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Router: reviews/<int:pk>/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer

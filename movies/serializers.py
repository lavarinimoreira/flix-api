from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if not rate:
            return None
        return round(rate, 1)

    def validate_release_date(self, value):
        if value.year < 1885:
            raise serializers.ValidationError('The release date can\'t be less than 1885.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('The resume can\'t have more than 500 characteres.')
        return value

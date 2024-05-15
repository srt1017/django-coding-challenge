from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie



class MovieSerializer(serializers.ModelSerializer):
    
    runtime_formatted = serializers.SerializerMethodField()
    
    def get_runtime_formatted(self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return f"{hours}:{minutes:02}"
    
    # from .serializers import ReviewSerializer
    # reviews = ReviewSerializer(many=True, read_only=True)
    # avg_rating = serializers.SerializerMethodField()
    
    # def get_avg_rating(self, obj):
    #     result = obj.reviews.aggregate(Avg('rating'))
    #     return result['rating__avg']

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            # "avg_rating",
        )
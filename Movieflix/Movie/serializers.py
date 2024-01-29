from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category_name')
    def get_category_name(self, obj):
        if obj.category:
            return obj.category.name
        return ""

    class Meta:
        model = Movie
        fields = ['title', 'slug', 'short_synopsis', 'full_synopsis', 'rating', 'movie_quality', 'duration', 'year_released', 'image', 'youtube_url', 'netflix_url', 'prime_url', 'genre', 'category']
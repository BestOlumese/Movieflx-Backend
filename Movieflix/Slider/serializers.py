from rest_framework import serializers
from .models import Slider
from Movie.models import Movie
from django.http import JsonResponse

class SliderSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField('get_movie_data')
    def get_movie_data(self, obj):
        if obj.movie:
            return {
                "title": obj.movie.title,
                "movie_quality": obj.movie.movie_quality,
                "genre": obj.movie.genre,
                "rating": obj.movie.rating,
                "year_released": obj.movie.year_released,
                "duration": obj.movie.duration,
                "youtube_url": obj.movie.youtube_url
            }

    class Meta:
        model = Slider
        fields = ['title', 'slug', 'slider_image', 'movie']
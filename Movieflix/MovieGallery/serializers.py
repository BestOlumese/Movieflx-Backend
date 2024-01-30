from rest_framework import serializers
from .models import MovieGallery
from django.http import JsonResponse

class MovieGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGallery
        fields = ['title', 'gallery_image']
from django.http import JsonResponse
from .models import MovieGallery
from .serializers import MovieGallerySerializer
from rest_framework.generics import ListAPIView


# Create your views here.

class ApiMovieGalleryListView(ListAPIView):
    queryset = MovieGallery.objects.all().order_by('-date_created')
    serializer_class = MovieGallerySerializer
    pagination_class = None
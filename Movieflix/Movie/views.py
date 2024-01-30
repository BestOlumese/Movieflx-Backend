from django.http import JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ApiMovieListView(ListAPIView):
    queryset = Movie.objects.all().order_by('-date_created')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = PageNumberPagination

class ApiMovieSearchListView(ListAPIView):
    queryset = Movie.objects.all().order_by('-date_created')
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre']

class ApiMovieCinemaMovieListView(ListAPIView):
    queryset = Movie.objects.filter(showtype=3).order_by('-date_created')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = PageNumberPagination

class ApiMovieStreamingNowListView(ListAPIView):
    queryset = Movie.objects.filter(showtype=2).order_by('-date_created')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = PageNumberPagination

class ApiMovieComingSoonListView(ListAPIView):
    queryset = Movie.objects.filter(showtype=1).order_by('-date_created')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = PageNumberPagination

class ApiMovieRandomListView(ListAPIView):
    queryset = Movie.objects.all().order_by('?')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = PageNumberPagination

class ApiMovieDetailListView(ListAPIView):
    
    def get_object(self, slug):
        try:
            return Movie.objects.get(slug=slug)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = MovieSerializer(snippet)
        return Response(serializer.data)

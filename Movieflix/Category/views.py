from django.http import JsonResponse
from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import ListAPIView


# Create your views here.

class ApiCategoryListView(ListAPIView):
    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer
    pagination_class = None
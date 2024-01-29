from django.http import JsonResponse
from .models import Slider
from .serializers import SliderSerializer
from rest_framework.generics import ListAPIView


# Create your views here.

class ApiSliderListView(ListAPIView):
    queryset = Slider.objects.all().order_by('-date_created')
    serializer_class = SliderSerializer
    pagination_class = None
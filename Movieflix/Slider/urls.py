from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiSliderListView.as_view()),
]
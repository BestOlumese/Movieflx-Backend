from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiCategoryListView.as_view()),
]
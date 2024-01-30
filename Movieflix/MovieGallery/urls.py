from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiMovieGalleryListView.as_view()),
]
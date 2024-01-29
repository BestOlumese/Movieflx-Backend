from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiMovieListView.as_view()),
    path('search', views.ApiMovieSearchListView.as_view()),
    path('random', views.ApiMovieRandomListView.as_view()),
    path('<str:slug>', views.ApiMovieDetailListView.as_view()),
]
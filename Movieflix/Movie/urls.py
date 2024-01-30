from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiMovieListView.as_view()),
    path('cinema-movie/', views.ApiMovieCinemaMovieListView.as_view()),
    path('streaming-now/', views.ApiMovieStreamingNowListView.as_view()),
    path('coming-soon/', views.ApiMovieComingSoonListView.as_view()),
    path('search', views.ApiMovieSearchListView.as_view()),
    path('random', views.ApiMovieRandomListView.as_view()),
    path('<str:slug>', views.ApiMovieDetailListView.as_view()),
]
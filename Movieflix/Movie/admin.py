from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'year_released', 'genre']

admin.site.register(Movie, MovieAdmin)
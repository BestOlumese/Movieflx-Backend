from django.contrib import admin
from .models import MovieGallery

# Register your models here.
class MovieGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'gallery_image']

admin.site.register(MovieGallery, MovieGalleryAdmin)

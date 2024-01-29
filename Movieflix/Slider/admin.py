from django.contrib import admin
from .models import Slider

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'slider_image']

admin.site.register(Slider, SliderAdmin)

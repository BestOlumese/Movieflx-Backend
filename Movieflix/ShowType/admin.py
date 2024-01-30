from django.contrib import admin
from .models import ShowType

# Register your models here.
class ShowTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'];

admin.site.register(ShowType, ShowTypeAdmin)
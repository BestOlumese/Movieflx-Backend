from django.db import models
from Movie.models import Movie
from django.utils.crypto import get_random_string

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    slider_image = models.ImageField(upload_to='uploads/slider/', max_length=500)
    movie = models.ForeignKey(Movie, related_name='movie', on_delete=models.CASCADE)
    date_created = models.DateField()

    def save(self, *args, **kwargs):
        unique_id = get_random_string(length=32)
        self.slug = unique_id
        super(Slider, self).save(*args, **kwargs)

    def __str__(self):
        return self.title  

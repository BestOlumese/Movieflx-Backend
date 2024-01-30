from django.db import models

# Create your models here.
class MovieGallery(models.Model):
    title = models.CharField(max_length=500)
    gallery_image = models.ImageField(upload_to='uploads/gallery/', max_length=500)
    date_created = models.DateField()

    def __str__(self):
        return self.title  

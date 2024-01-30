from django.db import models

# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string 

# Create your models here.
class ShowType(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    created_at = models.DateField()

    def save(self, *args, **kwargs):
        unique_id = get_random_string(length=32)
        self.slug = unique_id
        super(ShowType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name    

    class Meta:
        verbose_name_plural = "ShowTypes"
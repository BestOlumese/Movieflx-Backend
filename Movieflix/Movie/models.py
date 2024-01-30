from django.db import models
from Category.models import Category
from ShowType.models import ShowType
from django.utils.crypto import get_random_string

# Create your models here.
class Movie(models.Model):

    QUALITY_CHOICES = [
        ("720p", "720p"),
        ("1080p", "1080p"),
        ("2k", "2k"),
        ("4k", "4k"),
    ]

    RATING = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG13", "PG13"),
        ("13+", "13+"),
        ("PG16", "PG16"),
        ("16+", "16+"),
        ("17+", "17+"),
        ("PG18", "PG18"),
        ("18+", "18+"),
    ]


    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    short_synopsis = models.TextField(max_length=500)
    full_synopsis = models.TextField(max_length=500)
    rating = models.CharField(max_length=500, choices=RATING)
    movie_quality = models.CharField(max_length=500, choices=QUALITY_CHOICES)
    duration = models.CharField(max_length=500)
    year_released = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/movies/', max_length=500)
    youtube_url = models.CharField(max_length=500)
    netflix_url = models.CharField(max_length=500, blank=True)
    prime_url = models.CharField(max_length=500, blank=True)
    genre = models.CharField(max_length=500)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    showtype = models.ForeignKey(ShowType, related_name='showtype', on_delete=models.CASCADE)
    date_created = models.DateTimeField()

    def save(self, *args, **kwargs):
        unique_id = get_random_string(length=32)
        self.slug = unique_id
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title  

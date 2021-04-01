from django.db import models

# Create your models here.

class Post(models.Model):
    listing_title = models.CharField(max_length = 200, unique = True)
    listing_slug = models.SlugField(max_length = 200, unique = True)

    def __str__(self):
        return self.listing_title



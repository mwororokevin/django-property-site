from django.db import models
# from ..locations import Locations

# Create your models here.

class Post(models.Model):
    listing_title   = models.CharField(max_length = 200, unique = True)
    listing_content = models.TextField(null = True)

    def __str__(self):
        return self.listing_title



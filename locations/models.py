from django.db import models

# Create your models here.

class Locations(models.Model):
    location_title = models.CharField(max_length = 50, unique = True)
    location_content = models.TextField()

    def __str__(self):
        return self.location_title
from django.db import models
# from ..locations import Locations

# Create your models here.

LOCATION = (
    ('Nairobi', 'Nairobi'),
    ('Kisumu', 'Kisumu'),
    ('Mombasa', 'Mombasa'),
    ('Thika', 'Thika'),
    ('Nakuru', 'Nakuru')
)

class Listing(models.Model):
    listing_title   = models.CharField(max_length = 200, unique = True)
    listing_content = models.TextField(null = True)

    listing_location = models.CharField(
        max_length = 50,
        choices = LOCATION, 
        default = "", null = 
        False
    )

    def __str__(self):
        return self.listing_title



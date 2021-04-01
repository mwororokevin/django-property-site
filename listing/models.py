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

LISTING_STATUS = (
    ('Rented', 'Rented'),
    ('Sold', 'Sold'),
    ('For Rent', 'For Rent'),
    ('For Sale', 'For Sale'),
    ('Pending', 'Pending')
)

class Listing(models.Model):
    listing_title   = models.CharField(max_length = 200, unique = True)
    listing_content = models.TextField(null = True)

    listing_location = models.CharField(
        max_length = 50,
        choices = LOCATION, 
        default = "Nairobi", 
        null = False
    )

    listing_status = models.CharField(
        max_length = 15,
        choices = LISTING_STATUS,
        null = False,
        default = "For Rent"
    )

    def __str__(self):
        return self.listing_title



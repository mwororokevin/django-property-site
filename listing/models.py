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

LISTING_TYPE = (
    ('Apartments', 'Apartments'),
    ('Houses', 'Houses'),
    ('Commercial', 'Commercial'),
    ('Hotels & Lodges', 'Hotels & Lodges'),
    ('Land/Plots', 'Land/Plots'),
    ('Other', 'Other')
)

FURNISHED_STATUS = (
    ('Furnished', 'Yes'),
    ('Unfurnished', 'No')
)

class Listing(models.Model):
    listing_title   = models.CharField(
        max_length = 500, unique = True,
        help_text = 'Add the title of this listing.'
    )
    
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

    listing_type = models.CharField(
        max_length = 15,
        choices = LISTING_TYPE,
        default = 'Apartments',
        help_text = 'Select the correct type that represents this listing.'
    )

    number_of_bedrooms = models.IntegerField(
        blank = False,
        null = False,
        default = 0,
        help_text = 'Enter the total number of Bedrooms in this listing.'
    )

    number_of_bathrooms = models.IntegerField(
        blank = False,
        null = False,
        default = 0,
        help_text = 'Enter the total number of bathrooms in this listing.'
    )

    furniture = models.CharField(
        max_length = 15,
        choices = FURNISHED_STATUS,
        default = 'Yes'
    )

    service_fee = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing have a service fee?'
    )

    air_conditioning = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing have an AC unit or similar?'
    )

    garden = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing come with a garden?'
    )

    swimming_pool = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing include a swimming pool?'
    )

    balcony_or_terrace = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing include a balcony or a terrace?'
    )

    gym = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing include a gym?'
    )

    internet = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Is there a pre-existing internet connection in this listing?'
    )

    dstv_or_cable = models.CharField(
        max_length = 100,
        blank = True,
        help_text = 'Does this listing come with a DSTV / Cable connection?'
    )

    water_information = models.CharField(
        max_length = 100,
        blank = False,
        default = 'Available',
        help_text = 'Enter information about the water supply.'
    )

    power_information = models.CharField(
        max_length = 100,
        blank = False,
        default = 'Available',
        help_text = 'Enter information about the power/energy supply.'
    )

    security_information = models.CharField(
        max_length = 100,
        blank = False,
        default = 'Adequate',
        help_text = 'Enter information about the security situation.'
    )

    parking_information = models.CharField(
        max_length = 100,
        blank = False,
        default = 'Ample Parking',
        help_text = 'Enter information about the parking situation.'
    )

    kitchen_appliances = models.CharField(
        max_length = 50,
        blank = True,
        help_text = 'Select the appliances that are available in the current listing.'
    )

    def __str__(self):
        return self.listing_title

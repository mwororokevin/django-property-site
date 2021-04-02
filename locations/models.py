from django.db import models

# Create your models here.

class Location(models.Model):
    location_title = models.CharField(max_length = 50, unique = True)
    location_content = models.TextField()
    featured_image = models.ImageField(null = True)
    header_title = models.CharField(
        max_length = 50, null = True, unique = False,
        help_text = "If you don't want to use the main title in the page header, enter a new one here."
    )
    header_caption = models.CharField(
        max_length = 200, null = True, unique = False,
        help_text = "If you wish to display a caption under the title, enter it here."
    )

    def __str__(self):
        return self.location_title
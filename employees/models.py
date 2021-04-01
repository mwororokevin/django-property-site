from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(
        max_length = 100, 
        unique = False, 
        null = False,
        help_text = "Enter the Name of the Employee."
    )
    position = models.CharField(
        max_length = 50, 
        unique = False, 
        null = True, 
        help_text = "The position held by the Employee."
    )
    phone_number = models.CharField(
        max_length = 25, 
        unique = False, 
        null = False,
        help_text = "Enter the Employee's Phone Number."
    )
    email = models.CharField(
        unique = True,
        max_length = 50,
        null = False,
        help_text = "Enter the Employee's Email Address."
    )
    featured_image = models.ImageField(null = True)

    def __str__(self):
        return self.employee_name
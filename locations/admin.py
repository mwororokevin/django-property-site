from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_title', 'header_title', 'header_caption')

admin.site.register(Location, LocationAdmin)
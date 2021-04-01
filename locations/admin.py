from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_title', 'title', 'sub_title')

admin.site.register(Location, LocationAdmin)
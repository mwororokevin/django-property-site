from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'listing_title',
        'listing_location',
        'listing_status',
    )

admin.site.register(Listing, ListingAdmin)
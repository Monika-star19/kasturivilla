from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('check_in', 'check_out', 'adults', 'children')
    list_filter = ('check_in', 'check_out')  # Adds filters for check-in and check-out dates
    search_fields = ('adults', 'children')  # Allows searching by number of adults or children


from django.contrib import admin
from .models import Vendor, VendorAvailability, Booking

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'rating', 'price', 'location']
    list_filter = ['service_type', 'location']
    search_fields = ['name', 'service_type']

@admin.register(VendorAvailability)
class VendorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'is_available']
    list_filter = ['is_available', 'date']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'vendor', 'event_date', 'status', 'total_cost']
    list_filter = ['status', 'event_date']

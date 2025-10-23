from rest_framework import serializers
from .models import Vendor, VendorAvailability, Booking

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAvailability
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'

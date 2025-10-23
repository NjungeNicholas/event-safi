from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Vendor, VendorAvailability, Booking
from .serializers import VendorSerializer, BookingSerializer

class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

@api_view(['POST'])
def search_vendors(request):
    service_type = request.data.get('service_type')
    event_date = request.data.get('event_date')
    budget_max = request.data.get('budget_max')
    location = request.data.get('location')
    
    vendors = Vendor.objects.all()
    
    if service_type:
        vendors = vendors.filter(service_type__iexact=service_type)
    
    if budget_max:
        vendors = vendors.filter(price__lte=budget_max)
    
    if location:
        vendors = vendors.filter(location__icontains=location)
    
    if event_date:
        # Filter vendors available on the event date
        available_vendors = VendorAvailability.objects.filter(
            date=event_date, 
            is_available=True
        ).values_list('vendor_id', flat=True)
        vendors = vendors.filter(id__in=available_vendors)
    
    vendors = vendors.order_by('-rating')
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def check_availability(request):
    vendor_id = request.data.get('vendor_id')
    event_date = request.data.get('event_date')
    
    try:
        availability = VendorAvailability.objects.get(
            vendor_id=vendor_id, 
            date=event_date
        )
        return Response({'available': availability.is_available})
    except VendorAvailability.DoesNotExist:
        return Response({'available': False})

@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        booking = serializer.save()
        
        # Mark vendor as unavailable for that date
        VendorAvailability.objects.update_or_create(
            vendor_id=booking.vendor_id,
            date=booking.event_date,
            defaults={'is_available': False}
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

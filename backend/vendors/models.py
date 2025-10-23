from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    SERVICE_TYPES = [
        ('catering', 'Catering'),
        ('photography', 'Photography'),
        ('venue', 'Venue'),
        ('decoration', 'Decoration'),
        ('mc', 'MC'),
        ('dj', 'DJ'),
        ('transport', 'Transport'),
    ]
    
    name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    reviews_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    portfolio = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.service_type}"

class VendorAvailability(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='availability')
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['vendor', 'date']

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_type = models.CharField(max_length=100)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.vendor.name} - {self.event_date}"

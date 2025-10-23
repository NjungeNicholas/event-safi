from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from vendors.models import Vendor, VendorAvailability
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed database with sample vendors and users'

    def handle(self, *args, **options):
        # Create sample users
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'username': 'mike_wilson', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Wilson'},
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')

        # Create sample vendors
        vendors_data = [
            {
                'name': "Mama's Kitchen",
                'service_type': 'catering',
                'rating': 4.8,
                'reviews_count': 45,
                'price': 80000,
                'location': 'Nairobi',
                'portfolio': '120 events completed',
                'description': 'Premium catering services with authentic Kenyan and international cuisine',
                'phone': '+254700123456',
                'email': 'info@mamaskitchen.co.ke'
            },
            {
                'name': 'Lens Masters',
                'service_type': 'photography',
                'rating': 4.6,
                'reviews_count': 38,
                'price': 50000,
                'location': 'Nairobi',
                'portfolio': '200+ weddings',
                'description': 'Professional wedding and event photography with cinematic style',
                'phone': '+254700234567',
                'email': 'bookings@lensmasters.co.ke'
            },
            {
                'name': 'Garden Paradise',
                'service_type': 'venue',
                'rating': 4.7,
                'reviews_count': 52,
                'price': 60000,
                'location': 'Nairobi',
                'portfolio': 'Premium outdoor venue',
                'description': 'Beautiful garden venue perfect for weddings and corporate events',
                'phone': '+254700345678',
                'email': 'events@gardenparadise.co.ke'
            },
            {
                'name': 'Blooms & Drapes',
                'service_type': 'decoration',
                'rating': 4.5,
                'reviews_count': 29,
                'price': 45000,
                'location': 'Nairobi',
                'portfolio': 'Elegant event styling',
                'description': 'Creative event decoration and styling services',
                'phone': '+254700456789',
                'email': 'hello@bloomsdrapes.co.ke'
            },
            {
                'name': 'Joe the Host',
                'service_type': 'mc',
                'rating': 4.9,
                'reviews_count': 67,
                'price': 30000,
                'location': 'Nairobi',
                'portfolio': 'Professional MC & Host',
                'description': 'Experienced master of ceremonies for all types of events',
                'phone': '+254700567890',
                'email': 'joe@joethehost.co.ke'
            },
            {
                'name': 'SoundWave Pro',
                'service_type': 'dj',
                'rating': 4.4,
                'reviews_count': 41,
                'price': 35000,
                'location': 'Nairobi',
                'portfolio': 'Premium sound & lighting',
                'description': 'Professional DJ services with premium sound and lighting equipment',
                'phone': '+254700678901',
                'email': 'bookings@soundwavepro.co.ke'
            },
            {
                'name': 'Swift Rides',
                'service_type': 'transport',
                'rating': 4.3,
                'reviews_count': 33,
                'price': 25000,
                'location': 'Nairobi',
                'portfolio': 'Luxury transport services',
                'description': 'Premium transport services for weddings and events',
                'phone': '+254700789012',
                'email': 'info@swiftrides.co.ke'
            },
            {
                'name': 'Spice Garden Catering',
                'service_type': 'catering',
                'rating': 4.2,
                'reviews_count': 28,
                'price': 65000,
                'location': 'Mombasa',
                'portfolio': 'Coastal cuisine specialists',
                'description': 'Authentic coastal cuisine and international dishes',
                'phone': '+254700890123',
                'email': 'orders@spicegarden.co.ke'
            },
            {
                'name': 'Crystal Moments',
                'service_type': 'photography',
                'rating': 4.1,
                'reviews_count': 22,
                'price': 40000,
                'location': 'Kisumu',
                'portfolio': 'Creative event photography',
                'description': 'Artistic photography capturing your special moments',
                'phone': '+254700901234',
                'email': 'info@crystalmoments.co.ke'
            },
            {
                'name': 'Lakeside Gardens',
                'service_type': 'venue',
                'rating': 4.0,
                'reviews_count': 18,
                'price': 45000,
                'location': 'Kisumu',
                'portfolio': 'Scenic lakeside venue',
                'description': 'Beautiful lakeside venue with stunning views',
                'phone': '+254701012345',
                'email': 'bookings@lakesidegardens.co.ke'
            }
        ]

        for vendor_data in vendors_data:
            vendor, created = Vendor.objects.get_or_create(
                name=vendor_data['name'],
                defaults=vendor_data
            )
            if created:
                self.stdout.write(f'Created vendor: {vendor.name}')
                
                # Create availability for next 60 days
                start_date = datetime.now().date()
                for i in range(60):
                    date = start_date + timedelta(days=i)
                    VendorAvailability.objects.create(
                        vendor=vendor,
                        date=date,
                        is_available=True
                    )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))

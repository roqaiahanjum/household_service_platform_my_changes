import os
import sys
import django
from django.utils import timezone

# Adjust sys.path to find the Django project modules
sys.path.append(r'c:\Users\Roqaiah Anjum E\Downloads\household_service_platform-main\household_service_platform-main')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'household_services_platform.settings')
django.setup()

from bookings.models import Booking
from accounts.models import User
from services.models import Service

def create_test_data():
    # Get or create customer user
    customer, created = User.objects.get_or_create(
        username='testcustomer',
        defaults={
            'email': 'customer@test.com',
            'first_name': 'Test',
            'last_name': 'Customer',
            'role': 'CUSTOMER'
        }
    )
    if created:
        customer.set_password('password123')
        customer.save()
        print(f"Created Customer: {customer.username}")
    else:
        print(f"Customer already exists: {customer.username}")
        
    # Get any service
    service = Service.objects.first()
    if not service:
        print("No services found! Please run update_prices.py first.")
        return
    print(f"Using Service: {service.name} (price: {service.price_per_unit})")
    
    # Create booking
    booking = Booking.objects.create(
        customer=customer,
        service=service,
        scheduled_datetime=timezone.now() + timezone.timedelta(days=2),
        address="123 Tilakwadi, Belagavi, Karnataka",
        instructions="Please ring the bell upon arrival.",
        total_price=service.price_per_unit,
        payment_status='PENDING'
    )
    print(f"\nSUCCESS! Created Booking ID: {booking.id}")
    print(f"Checkout URL: http://127.0.0.1:8000/payments/checkout/{booking.id}/")

if __name__ == '__main__':
    create_test_data()

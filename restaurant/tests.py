from django.test import TestCase
from .models import Menu, Booking
from django.contrib.auth.models import User
class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Burger", description="Beef burger", price=12.50)
    def test_menu_price(self):
        burger = Menu.objects.get(name="Burger")
        self.assertEqual(float(burger.price), 12.50)
class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="peeruser", password="1234")
        Booking.objects.create(user=self.user, date="2025-12-01", time="18:00", num_guests=2)
    def test_booking_guest_count(self):
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.num_guests, 2)

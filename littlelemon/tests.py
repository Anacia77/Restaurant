from django.test import TestCase
from .models import Menu, Booking
from decimal import Decimal

class MenuModelTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title="Burger", price=Decimal("9.99"), inventory=50)
        Menu.objects.create(title="Pizza", price=Decimal("12.99"), inventory=30)

    def test_menu_item_creation(self):
        burger = Menu.objects.get(title="Burger")
        pizza = Menu.objects.get(title="Pizza")
        
        self.assertEqual(burger.title, "Burger")
        self.assertEqual(burger.price, Decimal("9.99"))
        self.assertEqual(burger.inventory, 50)
        
        self.assertEqual(pizza.title, "Pizza")
        self.assertEqual(pizza.price, Decimal("12.99"))
        self.assertEqual(pizza.inventory, 30)
    
    def test_menu_item_str_representation(self):
        burger = Menu.objects.get(title="Burger")
        pizza = Menu.objects.get(title="Pizza")
        
        self.assertEqual(str(burger), "Burger")
        self.assertEqual(str(pizza), "Pizza")
    
    def test_menu_item_get_item(self):
        burger = Menu.objects.get(title="Burger")
        pizza = Menu.objects.get(title="Pizza")
        
        self.assertEqual(burger.get_item(), "Burger : 9.99")
        self.assertEqual(pizza.get_item(), "Pizza : 12.99")

class BookingModelTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(name="Party", no_of_guests=20)
        Booking.objects.create(name="Meeting", no_of_guests=10)

    def test_booking_item_creation(self):
        party = Booking.objects.get(name="Party")
        meeting = Booking.objects.get(name="Meeting")
        
        self.assertEqual(party.name, "Party")
        self.assertEqual(party.no_of_guests, 20)
        
        self.assertEqual(meeting.name, "Meeting")
        self.assertEqual(meeting.no_of_guests, 10)
    
    def test_booking_item_str_representation(self):
        party = Booking.objects.get(name="Party")
        meeting = Booking.objects.get(name="Meeting")
        
        self.assertEqual(str(party), "Party")
        self.assertEqual(str(meeting), "Meeting")
    
    def test_booking_item_get_item(self):
        party = Booking.objects.get(name="Party")
        meeting = Booking.objects.get(name="Meeting")
        
        self.assertEqual(party.get_item(), "Party : 20")
        self.assertEqual(meeting.get_item(), "Meeting : 10")

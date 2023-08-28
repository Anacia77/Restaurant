from django.test import TestCase
from littlelemonAPI.models import *
# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Jollof", price=30, inventory=80)
        item_str = item.get_item()

        self.assertEqual(item_str, "Jollof : 30")
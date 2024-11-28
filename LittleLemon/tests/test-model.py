from django.test import TestCase
from restaurant.models import MenuItem, Menu, Booking

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Walnut Quesadilla", price=80, inventory=100)
        itemstr = item.__str__()

        self.assertEqual(itemstr, "Walnut Quesadilla : 80")

class MenuItemTest(TestCase): 
        def test_get_item(self):
             items = MenuItem.objects.create(title="the plant based Churger", price=30, inventory=100)
             itemstr = items.get_item()
             
             self.assertEqual(itemstr, "the plant based Churger : 30")






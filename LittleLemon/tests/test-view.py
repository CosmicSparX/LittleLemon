from django.test import TestCase
from restaurant.models import Menu



class MenuViewTest(TestCase):
    def setup(self): 
        menuitems = Menu.objects.create(title = "another vegan chole", price = 21, inventory = 50)
        itemstr = menuitems.__str__()
    
        test_getall = itemstr.get()

        self.assertEqual(test_getall, "another vegan chole : 19")

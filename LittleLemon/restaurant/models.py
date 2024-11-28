from django.db import models

# Create your models here.
class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    bookingdate = models.DateTimeField(blank=True, null=False)

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
    menu_id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length=255) 
    price = models.DecimalField(decimal_places=2, max_digits=10) 
    inventory = models.IntegerField() 

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
  
  
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
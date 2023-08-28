from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def get_item(self):
        return f'{self.name} : {str(self.no_of_guests)}'
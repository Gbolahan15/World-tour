from django.db import models

# Create your models here.
class Tour(models.Model):
    # We need an origin country, destination country, number of nights and price of that tour
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # This is a string representation of the tours
    def __str__(self): # this is to bring a string representation of what you want to display
        return (f"ID:{self.id}: "
                f"From {self.origin_country} to {self.destination_country}, "
                f"{self.number_of_nights} nights costs ${self.price}")


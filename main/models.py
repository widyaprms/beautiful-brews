from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255) 
    amount = models.IntegerField() 
    description = models.TextField() 


# function untuk memeriksa stock produk BeautyBrews Co.
def stock_checking(self):
    output = ""
    if self.amount > 0:
        output = "Stock of " + self.name + " is currently available: " + self.amount + " pcs."
    else:
        output = "Stock of " + self.name + " is currently not available."
    return output

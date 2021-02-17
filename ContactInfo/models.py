from django.db import models
from Partners.models import Customer, Supplier, Brand

# Create your models here.


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="customershipaddress")
    phoneaddress = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phoneaddress

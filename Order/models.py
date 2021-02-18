from django.db import models
from Partners.models import Customer
from Product.models import Product

# Create your models here.

statusChoices = [
    ("delivered", "delivered"), ("pending", "pending"), ("cancelled", "cancelled"),
]


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)

    transaction_id = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(
        max_length=150, choices=statusChoices, default="pending")
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

    @property
    def getordertotalPrice(self):
        sum = 0
        orderitems = self.itemorder.all()
        for item in orderitems:
            sum = sum+item.orderItemTotal
        return sum


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="itemorder", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0, null=True, blank=True)
    product = models.ForeignKey(
        Product, related_name="productorderitem", on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def orderItemTotal(self):
        return self.quantity * int(self.product.price)

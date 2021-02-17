from django.db import models
from Partners.models import Supplier
from Partners.models import Brand
from django.contrib.auth.models import User
from Partners.models import Customer
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    price = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, related_name="productbrand",
                              on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name="productsupplier")
    category = models.ForeignKey(
        "Category", related_name="productcategory", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="productreviews", on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, related_name="customereviews", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField()

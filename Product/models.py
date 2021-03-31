from django.db import models
from Partners.models import Supplier, Brand, Customer
from django.contrib.auth.models import User


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
        Category, related_name="productcategory", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def productcategory(self):
        return self.category.name

    @property
    def averageRating(self):
        reviews = self.productreviews.all()
        count = self.productreviews.all().count()
        sum = 0
        average=0
        for review in reviews:
            sum = sum+int(review.rating)
        if count:
            average = sum/count
        return average


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="productreviews", on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(
        Customer, related_name="customereviews", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField()

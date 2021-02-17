from Product.models import Product, Review, Category
from rest_framework.serializers import ModelSerializer


class productSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class categorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class reviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ["title", "description", "rating"]

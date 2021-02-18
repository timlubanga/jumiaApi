from Product.models import Product, Review, Category
from rest_framework import serializers
from Partners.serializers import CustomerSerializer


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class productSerializer(serializers.ModelSerializer):
    class Meta:
        productcategory = serializers.ReadOnlyField()
        model = Product
        fields = ["id", "price", "name", "brand",
                  "supplier", "image", "productcategory"]


class reviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["title", "description", "rating", "customer", "OrderItem"]

    def validate(self, data):
        item = self.context.get("item", None)
        customer = self.context.get("customer", None)
        review = Review.objects.filter(
            OrderItem=item, customer=customer).exists()
        if review:
            raise serializers.ValidationError({"message":
                "you have already reviewed this item"})
        return data
